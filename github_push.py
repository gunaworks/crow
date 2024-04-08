import streamlit as st
from github import Github

# GitHub credentials
def push(access_token, yaml_content):
    github_token = access_token
    repository_name = "gunaworks/crowci"
    file_name = "config.yaml"

    # Authenticate to GitHub
    g = Github(github_token)
    repo = g.get_repo(repository_name)
    try:
        contents = repo.get_contents(file_name)
        repo.update_file(file_name, "Updated YAML file", yaml_content, contents.sha)
        st.success("YAML file updated successfully!")
    except Exception as e:
        repo.create_file(file_name, "Created YAML file", yaml_content)
        st.success("YAML file created successfully!")