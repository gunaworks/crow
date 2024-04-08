import streamlit as st
from github import Github

# GitHub credentials
github_token = "enter your github token here"
repository_name = "gunaworks/crowci"
file_name = "config.yaml"

# Authenticate to GitHub
g = Github(github_token)
repo = g.get_repo(repository_name)

# Streamlit UI
st.title("GitHub YAML Pusher")

# Text area for YAML content
yaml_content = st.text_area("Paste YAML content here:")

# Button to push YAML to GitHub
if st.button("Push to GitHub"):
    # Create or update file in the repository
    try:
        contents = repo.get_contents(file_name)
        repo.update_file(file_name, "Updated YAML file", yaml_content, contents.sha)
        st.success("YAML file updated successfully!")
    except Exception as e:
        repo.create_file(file_name, "Created YAML file", yaml_content)
        st.success("YAML file created successfully!")