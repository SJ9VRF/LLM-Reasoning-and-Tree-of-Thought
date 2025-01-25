#  ensures that multiple reasoning paths are considered, enhancing the consistency and reliability of the model's answers.

# src/prompts/self_consistency.py

class SelfConsistencyPrompt:
    @staticmethod
    def calculate_costs():
        """Generate a self-consistency prompt to calculate costs using multiple reasoning paths."""
        return (
            "Calculate the total cost of 3 notebooks and 2 pens where each notebook costs $1.50 and each pen costs $0.75. "
            "Use different paths of reasoning to find consistent results. For example, first calculate the cost of notebooks, then pens, and sum them; then, calculate all items together."
        )

