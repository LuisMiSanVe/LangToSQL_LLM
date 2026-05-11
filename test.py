import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./sql-model-merged"  

PROMPT = """\
Write a select query of the invoice table.
"""

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

print("Loading model... (this may take a while)")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",
    ignore_mismatched_sizes=True
)

model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

inputs = tokenizer(PROMPT, return_tensors="pt").to(model.device)

print("\nGenerating response...\n")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.2,
        top_p=0.95,
        do_sample=True,
        repetition_penalty=1.1,
        eos_token_id=tokenizer.eos_token_id
    )

result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("===== MODEL OUTPUT =====\n")
print(result)
print("\n========================")