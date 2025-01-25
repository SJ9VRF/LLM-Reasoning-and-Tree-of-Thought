
from gpt4 import GPT4
from prompts.chain_of_thought import ChainOfThoughtPrompt
from prompts.self_consistency import SelfConsistencyPrompt
from prompts.tree_of_thoughts import TreeOfThoughtsPrompt
from prompts.rag import RAGPrompt
from prompts.art import ARTPrompt

def main():
    # Configuration for GPT-4 API
    api_key = 'your_openai_api_key_here'
    model = 'gpt-4o-mini'
    gpt_instance = GPT4(api_key, model)

    # Using Chain of Thought Prompt
    cot_prompt = ChainOfThoughtPrompt.solve_arithmetic_problem()
    cot_response = gpt_instance.call(cot_prompt)
    print("Chain of Thought Response:", cot_response)

    # Using Self-Consistency Prompt
    sc_prompt = SelfConsistencyPrompt.calculate_costs()
    sc_response = gpt_instance.call(sc_prompt)
    print("Self-Consistency Response:", sc_response)

    # Using Tree of Thoughts Prompt
    tot_prompt = TreeOfThoughtsPrompt.complex_decision_making()
    tot_response = gpt_instance.call(tot_prompt)
    print("Tree of Thoughts Response:", tot_response)

    # Using Retrieval Augmented Generation Prompt
    rag_prompt = RAGPrompt.answer_complex_question()
    rag_response = gpt_instance.call(rag_prompt)
    print("Retrieval Augmented Generation Response:", rag_response)

    # Using Automatic Reasoning and Tool-use Prompt
    art_prompt = ARTPrompt.diagnose_symptoms()
    art_response = gpt_instance.call(art_prompt)
    print("Automatic Reasoning and Tool-use Response:", art_response)

if __name__ == "__main__":
    main()

