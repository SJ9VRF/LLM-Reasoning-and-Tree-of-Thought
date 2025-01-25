# src/prompts/chain_of_thought.py

# handle the creation of prompts that guide the model through a series of logical reasoning steps to solve complex tasks.

class ChainOfThoughtPrompt:
    @staticmethod
    def solve_arithmetic_problem():
        """Generate a Chain of Thought prompt for solving an arithmetic problem with step-by-step reasoning."""
        return (
            "Let's solve a math problem step by step. "
            "Problem: If you have 5 apples and you buy 8 more, how many apples do you have in total? "
            "Think step by step."
        )

