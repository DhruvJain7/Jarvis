from config import GROQ_API_KEY
from model import llama_1_response, llama_2_response, openai_1_response


def llm_test(system_prompt, user_prompt):

    llama_1_result = llama_1_response(system_prompt, user_prompt)
    llama_2_result = llama_2_response(system_prompt, user_prompt)
    openai_1_result = openai_1_response(system_prompt, user_prompt)

    print("Llama_1_reponse:\n", llama_1_result)
    print("Llama_2_response:\n", llama_2_result)
    print("Openai_1_response:\n", openai_1_result)


# calling all llms together
llm_test(
    "You are a helpful assistant. Provide the response as a JSON object with the specified keys. DO NOT return the schema or property definitions. ONLY return the final values.",
    "What is the capital of India?",
)
