from src.gpt4 import GPT4
from src.prompts.zero_shot import ZeroShotPrompt
from src.prompts.few_shot import FewShotPrompt

# Assuming you have set your API key
api_key = "your_openai_api_key"
model = "gpt-4o-mini"

# Initialize the GPT-4 class
gpt = GPT4(api_key, model)

# Create a zero-shot prompt
zero_shot_prompt = ZeroShotPrompt.sentiment_analysis("I love Python programming!")
response = gpt.call(zero_shot_prompt)
print("Zero-shot response:", response)

# Create a few-shot prompt
few_shot_prompt = FewShotPrompt.sentiment_analysis()
response = gpt.call(few_shot_prompt)
print("Few-shot response:", response)
