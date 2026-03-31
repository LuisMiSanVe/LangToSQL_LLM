import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, PeftModel
from trl import SFTTrainer

model_name = "deepseek-ai/deepseek-coder-1.3b-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map={"": "cpu"} # Sets CPU for training, you can change it to use the GPU instead
)

dataset = load_dataset("json", data_files="train.json", split="train")

def format_example(example):
    return {
        "instruction": example["question"],
        "input": "",
        "output": example["query"]
    }

dataset = dataset.map(format_example)

def tokenize(example):
    prompt_ids = tokenizer(
        example["instruction"],
        padding="max_length",
        truncation=True,
        max_length=512
    ).input_ids

    label_ids = tokenizer(
        example["output"],
        padding="max_length",
        truncation=True,
        max_length=512
    ).input_ids

    attention_mask = [1 if id != tokenizer.pad_token_id else 0 for id in prompt_ids]

    return {
        "input_ids": prompt_ids,
        "attention_mask": attention_mask,
        "labels": label_ids
    }

dataset = dataset.map(tokenize, batched=False)

peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

training_args = TrainingArguments(
    output_dir="./sql-model",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=1, # More epochs -> better accuracy but longer training
    logging_steps=10,
    save_strategy="epoch",
    fp16=False
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    args=training_args
)

trainer.train()

trainer.model.save_pretrained("./sql-model")
tokenizer.save_pretrained("./sql-model")

base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map={"": "cpu"}
)
model_merged = PeftModel.from_pretrained(base_model, "./sql-model")
model_merged = model_merged.merge_and_unload()
model_merged.save_pretrained("./sql-model-merged")