from github import Github
import os
import yaml

# GitHub authentication
github_token = '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'
repo_name = 'crowci'
file_name = 'data.yaml'
branch_name = 'main'

# Content to write to YAML file
yaml_content = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3'
}

# Convert dictionary to YAML format
yaml_data = yaml.dump(yaml_content)

# Initialize PyGithub with token
g = Github(github_token)

# Get the repository
repo = g.get_repo(repo_name)

# Create a new branch
branch = repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=repo.get_branch('main').commit.sha)

# Create or update file
try:
    # Attempt to get the file
    contents = repo.get_contents(file_name, ref=branch_name)
    # Update the file
    repo.update_file(contents.path, "committing yaml file", yaml_data, contents.sha, branch=branch_name)
    print(f"File {file_name} updated successfully.")
except Exception as e:
    # Create the file if it doesn't exist
    repo.create_file(file_name, "creating yaml file", yaml_data, branch=branch_name)
    print(f"File {file_name} created successfully.")

# Commit the changes
commit_message = "Updated YAML data"
repo.get_branch(branch_name).commit.commit.create_status(state="success", description="YAML file updated successfully", context="continuous-integration")

# Merge pull request
pull = repo.create_pull(title="Update YAML data", body="Auto-generated pull request to update YAML data", base=branch_name, head="master")
pull.merge()

print("Pull request merged successfully.")
