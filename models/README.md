# 🤖 Models for Coding Assistant AI

This folder does not store large model weights (too big for GitHub).  
Instead, download models directly from Hugging Face:

## Recommended Open-Source Coding Models

1. [DeepSeek-Coder-6.7B-Instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct)  
   - Strong for Python and general coding tasks.  
   - Works well with error-handling prompts.  

2. [CodeLlama-7B-Instruct](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf)  
   - Great for Python + multiple languages.  
   - Lighter and faster than 13B models.  

3. [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b)  
   - Optimized for multi-language coding.  
   - Based on GitHub’s permissive dataset.  

---

## 🔧 How to Download Models

In Python, you don’t need to manually download.  
Just install `transformers` and load them:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "deepseek-ai/deepseek-coder-6.7b-instruct"  # or CodeLlama / StarCoder2
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
