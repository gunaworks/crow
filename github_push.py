"""Module used to push the generated yaml content to directory .github/workflows"""
import re
import streamlit as st
from urllib.parse import urlparse
from github import Github
from github.Repository import Repository
import github

############################################################################
def does_object_exists_in_branch(repo: Repository, branch: str, object_path: str) -> bool:
    """checks whether directory already exists or not"""
    try:
        repo.get_contents(object_path, branch)
        return True
    except github.UnknownObjectException:
        return False

#############################################################################
def link_validator(respository_link):
    """Link Validator"""
    return re.search("https://github.com/[\\w-]+/[\\w-]+$", respository_link)

#############################################################################
def parse_repository(repository_link):
    """Parsing the repository link to get the repository name"""
    parsed_url = urlparse(repository_link)
    path_components = parsed_url.path.split('/')
    repository_name = "/".join(path_components[1:3])
    return repository_name

#############################################################################
def create_config_file(repository, file_name, yaml_content):
    """uses create_file"""
    repository.create_file(file_name, "Created YAML file", yaml_content)
    st.success("YAML file created successfully!")

#############################################################################
def update_config_file(repository, file_name, yaml_content):
    """uses update_file"""
    contents = repository.get_contents(file_name)
    repository.update_file(file_name, "Updated YAML file", yaml_content, contents.sha)
    st.success("YAML file updated successfully!")

#############################################################################
def get_repository(github_token, repository_name):
    """get_repository method"""
    g = Github(github_token)
    repository = g.get_repo(repository_name)
    return repository

##############################################################################
def push_yaml_to_github(access_token, yaml_content, repository_link):
    """Checks for validity of link and repository object and then pushes the yaml"""
    github_token = access_token
    file_name = ".github/workflows/config.yaml"
    if link_validator(repository_link):
        repository_name = parse_repository(repository_link)
        repository = get_repository(github_token, repository_name)
        if does_object_exists_in_branch(repository, "main", file_name):
            update_config_file(repository, file_name, yaml_content)
        else:
            create_config_file(repository, file_name, yaml_content)
    else:
        st.warning("Invalid Repository Link!")
