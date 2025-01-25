# include functions for loading and processing data, which can be particularly useful for managing input/output for the models.

# src/utils/data_processing.py

import json

def load_json(file_path):
    """Load a JSON file and return its contents."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_text(file_path):
    """Load text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

