"""This module is used to generate the yaml file using gpt-3.5-turbo-instruct"""
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model="gpt-3.5-turbo-instruct", api_key=key)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a CI/CD specialist with expertise in writing precise and accurate YAML files for defining CI/CD pipelines. 
Your task is to generate a YAML file strictly based on the user's specific requirements for their GitHub Actions workflow. 
The user will provide their requirements after the colon. 
You have to generate the best possible yaml file given the current user requirements without asking for more details.
If the user provides anything irrelevant you must not entertain it and ask the user to generate correct requirements.
    Your entire response should be in YAML code format.
User Requirements: 
"""),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

def generate(user_input):
    """generate the model response"""
    response = chain.invoke({"input": user_input})
    return response