from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os
from prompts import BASE_PROMPT


class CodingAI:
    def __init__(self, model_name="deepseek-ai/deepseek-coder-6.7b-instruct"):
        print("[INFO] Loading model... this may take some time ⏳")

        # Get token if provided
        hf_token = os.environ.get("HUGGINGFACE_HUB_TOKEN") or os.environ.get("HF_TOKEN")
        token_args = {"use_auth_token": hf_token} if hf_token else {}

        # Load tokenizer and model once
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, **token_args)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto",
            **token_args
        )

    def ask(self, user_input: str) -> str:
        """Generate a response from the AI model."""
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
