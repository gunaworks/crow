import streamlit as st
from urllib.parse import urlparse
from github import Github

##############################################################################################################
def parse_repository(repository_link):
    parsed_url = urlparse(repository_link)
    path_components = parsed_url.path.split('/')
    repository_name = "/".join(path_components[1:3])
    return repository_name

##############################################################################################################
def create_config_file(repository, file_name, yaml_content):
    repository.create_file(file_name, "Created YAML file", yaml_content)
    st.success("YAML file created successfully!")

##############################################################################################################
def update_config_file(repository, file_name, yaml_content):
    contents = repository.get_contents(file_name)
    repository.update_file(file_name, "Updated YAML file", yaml_content, contents.sha)
    st.success("YAML file updated successfully!")

##############################################################################################################
def get_repository(github_token, repository_name):
    g = Github(github_token)
    repository = g.get_repo(repository_name)
    return repository

##############################################################################################################
def push_yaml_to_github(access_token, yaml_content, repository_link):
    github_token = access_token
    file_name = ".github/workflows/config.yaml"
    repository_name = parse_repository(repository_link)
    repository = get_repository(github_token, repository_name)
    try:
        update_config_file(repository, file_name, yaml_content)
    except Exception as e:
        if "Not Found" in str(e):
            create_config_file(repository, file_name, yaml_content)
        else:
            raise e