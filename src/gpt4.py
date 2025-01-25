# handles interactions with the OpenAI API specifically for GPT-4, simplifying the process of sending prompts and receiving responses.
# src/gpt4.py

import requests

class GPT4:
    def __init__(self, api_key, model='gpt-4o-mini', api_url="https://api.openai.com/v1/chat/completions"):
        self.api_key = api_key
        self.model = model
        self.api_url = api_url
        print(f'Initialized GPT4 with model: {self.model}')

    def _prepare_headers(self):
        """Prepare the headers needed for the API request."""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def _prepare_payload(self, prompt, **kwargs):
        """Prepare the JSON payload for the API request."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "max_tokens": kwargs.get('max_tokens', 150)
        }
        return payload

    def call(self, prompt, **kwargs):
        """Send a prompt to the GPT-4 API and return the response."""
        headers = self._prepare_headers()
        payload = self._prepare_payload(prompt, **kwargs)
        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()  # Raises an HTTPError for bad requests
        return response.json()['choices'][0]['text']

