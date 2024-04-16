# import ollama
# import streamlit as st

# def generate(initial_prompt, user_input):
#     prompt = initial_prompt + user_input
#     stream = ollama.generate(
#         model = "codellama",
#         prompt = prompt,
#         stream = True,
#         )
#     for chunk in stream:
#         yield chunk['response']

import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key="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")#, temperature=0.8)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a CI/CD specialist with expertise in writing precise and accurate YAML files for defining pipelines in GitHub Actions workflows. 
Your task is to generate a YAML file strictly based on the user's specific requirements for their GitHub Actions workflow. 
The user will provide their requirements after the colon. 
If the user provides anything irrelevant  you must not entertain it and ask the user to generate correct requirements.
User Requirements: 
"""),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

def generate(user_input):
    response = chain.invoke({"input": user_input})
    return response