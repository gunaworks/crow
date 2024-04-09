import streamlit as st
from urllib.parse import urlparse
from github import Github

# GitHub credentials
def push(access_token, yaml_content, repository_link):
    github_token = access_token
    file_name = "config.yaml"

    #Parse the repository link to get the repository name
    parsed_url = urlparse(repository_link)
    path_components = parsed_url.path.split('/')
    repository_name = "/".join(path_components[1:3])
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