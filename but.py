import streamlit as st
import ollama
from github import Github
from github import InputGitTreeElement

# GitHub credentials
GITHUB_TOKEN = "token_key"
REPO_NAME = "Crowci"
BRANCH_NAME = "main"
FILE_PATH = "config.yaml"

# Create a title for the app
st.title("Project Crow")

# Create a sidebar with input fields for prompts
sidebar = st.sidebar
user_input = sidebar.text_area("User Requirements")
submit_generate_yaml = sidebar.button(label="Generate YAML")
submit_push_to_github = sidebar.button(label="Push to GitHub")

prompt_input = """
You are a CI/CD specialist. You have a specialty in writing yaml files in defining the pipelines. 
You have written over 10000+ yaml files defining the complete pipeline accurately and precisely that have been used by the users directly without any editing. 
After the colon sign the user will explain his/her requirements. Your task is to generate a yaml file for the user based on their specific requirements such that 
it can be used with GitHub actions.
A sample yaml file is given below:
...
# yaml file ends
"""

@st.cache
def generate_yaml(user_input):
    """Generates YAML code based on the provided prompts and returns it as a string."""
    final_prompt = prompt_input + user_input
    response = ollama.generate(model="codellama", prompt=final_prompt)
    yaml_content = "\n".join(response["response"])
    return yaml_content

def push_to_github(file_content):
    """Pushes the generated YAML file to the GitHub repository."""
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    contents = repo.get_contents(FILE_PATH, ref=BRANCH_NAME)
    repo.update_file(FILE_PATH, "Pushing updated YAML file", file_content, contents.sha, branch=BRANCH_NAME)

if submit_generate_yaml:
    # Generate the YAML file based on the prompt and other input
    yaml_file = generate_yaml(user_input)

    # Display the generated YAML code in a code block for clarity
    st.code(yaml_file, language="yaml")

if submit_push_to_github:
    # Push the generated YAML file to the GitHub repository
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    contents = repo.get_contents(FILE_PATH, ref=BRANCH_NAME)
    repo.update_file(FILE_PATH, "Pushing updated YAML file", yaml_file, contents.sha, branch=BRANCH_NAME)
    st.success("YAML file pushed to GitHub successfully!")
