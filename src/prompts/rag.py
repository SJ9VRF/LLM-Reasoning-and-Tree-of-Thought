# Retrieval Augmented Generation Module
# module facilitates the integration of external knowledge sources into the generation process, enhancing the model's factual accuracy.

# src/prompts/rag.py

class RAGPrompt:
    @staticmethod
    def answer_complex_question():
        """Generate a prompt for answering complex questions using external knowledge sources."""
        return (
            "Explain the impact of global warming on Arctic wildlife. "
            "Use retrieved documents that discuss recent changes in ice cover and their effects on polar bears and other native species."
        )
