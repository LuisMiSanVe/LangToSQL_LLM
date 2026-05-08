import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, PeftModel
from trl import SFTTrainer

model_name = "Qwen/Qwen2.5-Coder-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="auto"
)

model.config.pad_token_id = tokenizer.eos_token_id

dataset = load_dataset("json", data_files="train.json", split="train")

def format_example(x):
    messages = [
        {"role": "user", "content": f"Write SQL query for: {x['question']}"},
        {"role": "assistant", "content": x["query"]}
    ]
    return {
        "text": tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=False
        )
    }

dataset = dataset.map(format_example)

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
    fp16=torch.cuda.is_available()
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
    device_map="auto"
)
model = PeftModel.from_pretrained(base_model, "./sql-model")
model = model.merge_and_unload()
model.save_pretrained("./sql-model-clean", safe_serialization=True)
tokenizer.save_pretrained("./sql-model-clean")