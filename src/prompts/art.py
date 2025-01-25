# art.py - Automatic Reasoning and Tool-use Module
# module enables the model to use external tools and data sources in a structured way, simulating real-world reasoning and decision-making processes.

# src/prompts/art.py

class ARTPrompt:
    @staticmethod
    def diagnose_symptoms():
        """Generate a prompt that uses medical databases to diagnose symptoms and suggest treatments."""
        return (
            "Patient presents with fever, cough, and shortness of breath. "
            "Use medical databases to assess the symptoms and propose a diagnosis. "
            "Consider the likelihood of common illnesses such as influenza, COVID-19, and pneumonia. "
            "Summarize the reasoning without suggesting medication directly."
        )
