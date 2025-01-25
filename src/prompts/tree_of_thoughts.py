# structure complex tasks by creating a tree of possible thought processes, guiding the model through systematic exploration and problem-solving.

# src/prompts/tree_of_thoughts.py

class TreeOfThoughtsPrompt:
    @staticmethod
    def complex_decision_making():
        """Generate a Tree of Thoughts prompt for complex decision-making scenarios."""
        return (
            "Imagine you are planning a trip and need to decide on the destination, budget, and itinerary. "
            "Explore different options systematically: "
            "1. If you choose Europe, think about budget options and attractions. "
            "2. If you choose Asia, consider the weather conditions and cultural experiences. "
            "Evaluate each option to find the best overall plan."
        )
