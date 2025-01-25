#  defines a class for creating zero-shot prompts, where the model generates a response based on a single instruction without prior examples.

# src/prompts/zero_shot.py

class ZeroShotPrompt:
    @staticmethod
    def sentiment_analysis(prompt):
        """Generate a zero-shot prompt for sentiment analysis."""
        return f"Classify the sentiment of this text: '{prompt}'. Is it positive, negative, or neutral?"
