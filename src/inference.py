from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from prompts import BASE_PROMPT

class CodingAI:
    def __init__(self, model_name="deepseek-ai/deepseek-coder-6.7b-instruct"):
        print("[INFO] Loading model... this may take some time ⏳")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def ask(self, user_input: str) -> str:
        full_prompt = BASE_PROMPT + "\nUser: " + user_input + "\nAssistant:"
        inputs = self.tokenizer(full_prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_length=512,
            temperature=0.2,
            do_sample=True,
            top_p=0.9
        )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
