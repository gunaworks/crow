import ollama
import streamlit as st

def generate(initial_prompt, user_input):
    prompt = initial_prompt + user_input
    stream = ollama.generate(
        model = "codellama",
        prompt = prompt,
        stream = True,
        )
    for chunk in stream:
        yield chunk['response']