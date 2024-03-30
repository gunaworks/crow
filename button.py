import streamlit as st
import ollama

# Create a title for the app
st.title("Project Crow")

# Create a sidebar with input fields for prompts
sidebar = st.sidebar
user_input = sidebar.text_input("Prompt")
submit = sidebar.button(label="Submit")

# Add a button for uploading YAML files
uploaded_file = st.sidebar.file_uploader("Upload YAML file", type=["yaml"])

prompt_input = """
You are a CI/CD specialist. You have a specialty in writing yaml files in defining the pipelines. 
You have written over 10000+ yaml files defining the complete pipeline accurately and precisely that have been used by the users directly without any editing. 
After the colon sign the user will explain his/her requirements. Your task is to generate a yaml file for the user based on their specific requirements such that 
it can be used with GitHub actions.
A sample yaml file is given below:

# Optional - The name of the workflow as it will appear in the "Actions" tab of the GitHub repository. If this field is omitted, the name of the workflow file will be used instead.
name: learn-github-actions
# Optional - The name for workflow runs generated from the workflow, which will appear in the list of workflow runs on your repository's "Actions" tab. This example uses an expression with the `github` context to display the username of the actor that triggered the workflow run. For more information, see "[AUTOTITLE](/actions/using-workflows/workflow-syntax-for-github-actions#run-name)."
run-name: ${{ github.actor }} is learning GitHub Actions

# Specifies the trigger for this workflow. This example uses the `push` event, so a workflow run is triggered every time someone pushes a change to the repository or merges a pull request.  This is triggered by a push to every branch; for examples of syntax that runs only on pushes to specific branches, paths, or tags, see "[AUTOTITLE](/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)."
on: [push]

# Groups together all the jobs that run in the `learn-github-actions` workflow.
jobs:

# Defines a job named `check-bats-version`. The child keys will define properties of the job.
  check-bats-version:

# Configures the job to run on the latest version of an Ubuntu Linux runner. This means that the job will execute on a fresh virtual machine hosted by GitHub. For syntax examples using other runners, see "[AUTOTITLE](/actions/reference/workflow-syntax-for-github-actions#jobsjob_idruns-on)"
    runs-on: ubuntu-latest

# Groups together all the steps that run in the `check-bats-version` job. Each item nested under this section is a separate action or shell script.
    steps:

# The `uses` keyword specifies that this step will run `v4` of the `actions/checkout` action. This is an action that checks out your repository onto the runner, allowing you to run scripts or other actions against your code (such as build and test tools). You should use the checkout action any time your workflow will use the repository's code.
      - uses: actions/checkout@v4

# This step uses the `actions/setup-node@v4` action to install the specified version of the Node.js. (This example uses version 14.) This puts both the `node` and `npm` commands in your `PATH`.
      - uses: actions/setup-node@v4
        with:
          node-version: '20'

# The `run` keyword tells the job to execute a command on the runner. In this case, you are using `npm` to install the `bats` software testing package.
      - run: npm install -g bats

# Finally, you'll run the `bats` command with a parameter that outputs the software version.
      - run: bats -v
# yaml file ends

Based on this structure and keeping in mind the user's expectations, you have to generate a similar yaml file for the user. User will now give their requirements 
after the colon.
User Requirements: 
"""

def generate_yaml(prompt_input, user_input):
    """Generates YAML code based on the provided prompts and returns it as a string."""
    final_prompt = prompt_input + user_input
    response = ollama.generate(model="codellama", prompt=final_prompt)
    yaml_content = ""
    for line in response["response"]:
        yaml_content += line#.decode("utf-8")
    return yaml_content

if submit:
    # Generate the YAML file based on the prompt and other input
    yaml_file = generate_yaml(prompt_input, user_input)

    # Display the generated YAML code in a code block for clarity
    st.code(yaml_file, language="yaml")

# Process the uploaded file if available
if uploaded_file is not None:
    # Read the content of the file
    file_content = uploaded_file.getvalue()
    # Display the content in a code block
    st.code(file_content, language="yaml")
