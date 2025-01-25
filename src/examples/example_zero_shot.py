# Zero-Shot Prompting involves instructing the model to perform a task without providing examples.

# src/examples/example_zero_shot.py

from src.gpt4 import GPT4
from src.prompts.zero_shot import ZeroShotPrompt

def main():
    your_api_key = 'YOUR_API_KEY_HERE'
    gpt = GPT4(api_key=your_api_key, model='gpt-4o-mini')
    
    text = "I think the vacation is okay."
    prompt = ZeroShotPrompt.classify_sentiment(text)
    
    response = gpt.call(prompt)
    print(f"Sentiment: {response}")

if __name__ == "__main__":
    main()

