# provides additional utility functions that could be used across different parts of the project.

# src/utils/helpers.py

def format_prompt(prompt):
    """Format and clean up prompt text."""
    return prompt.strip()

def concatenate_prompts(*args):
    """Concatenate multiple prompt parts into a single string."""
    return ' '.join(args)

