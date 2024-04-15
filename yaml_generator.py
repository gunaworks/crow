import os
from langchain_openai import OpenAI

os.getenv("OPENAI_API_KEY")


llm = OpenAI(model="gpt-3.5-turbo-0125")#, temperature=0.8)

system_prompt = """
You are a CI/CD specialist with expertise in writing precise and accurate YAML files for defining pipelines in GitHub Actions workflows. 
Your task is to generate a YAML file strictly based on the user's specific requirements for their GitHub Actions workflow. 
The user will provide their requirements after the colon. 
If the user provides anything irrelevant  you must not entertain it and ask the user to generate correct requirements.
User Requirements: 
"""

def generate_yaml(prompt, user_input):
    final_prompt = prompt + user_input
    response = llm(final_prompt)
    return response