from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field

from config import GROQ_API_KEY, llama_1, llama_2, openai_1


# Define JSON output structure
class AIResponse(BaseModel):
    summary: str = Field(description="Summary of the user's message")
    sentiment: int = Field(
        description="Sentiment score from 0 (negative) to 100 (positive)"
    )
    response: str = Field(description="Suggested response to the user")


# JSON output parser
json_parser = JsonOutputParser(pydantic_object=AIResponse)


# Function to intialize the model
def initialize_model(model_Id):
    return ChatGroq(
        model=model_Id,
        temperature=0.2,
        max_tokens=256,
    )


# for each respective model
llama_1 = initialize_model(llama_1)
llama_2 = initialize_model(llama_2)
openai_1 = initialize_model(openai_1)


# prompt templates for each model
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "{system_prompt}\n\n{format_instructions}"),
        ("human", "{user_prompt}"),
    ]
)


def get_ai_response(model, template, system_prompt, user_prompt):
    format_instructions = json_parser.get_format_instructions()
    chain = template | model | json_parser
    return chain.invoke(
        {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "format_instructions": format_instructions,
        }
    )


# Individual functions for each model


def llama_1_response(system_prompt, user_prompt):
    return get_ai_response(llama_1, chat_template, system_prompt, user_prompt)


def llama_2_response(system_prompt, user_prompt):
    return get_ai_response(llama_2, chat_template, system_prompt, user_prompt)


def openai_1_response(system_prompt, user_prompt):
    return get_ai_response(openai_1, chat_template, system_prompt, user_prompt)
