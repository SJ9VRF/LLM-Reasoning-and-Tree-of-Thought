# src/prompts/few_shot.py

class FewShotPrompt:
    @staticmethod
    def sentiment_analysis():
        """Generate a few-shot prompt for sentiment analysis with example contexts."""
        return (
            "Example 1: 'I loved the new Batman movie!' - Positive\n"
            "Example 2: 'I hated the new Batman movie!' - Negative\n"
            "Example 3: 'The new Batman movie was okay.' - Neutral\n"
            "Based on the examples provided, classify the sentiment of the following text: 'I think the vacation was okay.'"
        )

