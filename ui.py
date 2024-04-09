<<<<<<< HEAD
from yaml_generator import generate
import streamlit as st
from github_push import push

# initial_prompt = """ You are a CI specialist. You are only allowed to respond by giving relevant YAML
#     Pipeline code. You cannot respond with anything else. Only generate most basic YAML pipeline code according to user requirements. Add information according to user and not on your own. Add details as the user provides. The user will give you input after :
# User Requirements: """
initial_prompt = "Hi"
def ui(access_token):

    col1, middle_gap, col2 = st.columns([1.5, .5 , 3], gap="large")
    
    if 'yaml_content' not in st.session_state:
        st.session_state.yaml_content = ""

    with col1:
        st.title("Input")
        user_input = st.text_area(label="Input",height=250 ,key="InputBox", placeholder="Ask CrowCI...", label_visibility="hidden")
        col11, col12 = st.columns(2, gap="small")
        with col12:
            submit = st.button(label="Submit")


    with col2:
        col21, col22 = st.columns(2, gap="small")
        yaml_content = ""
        with col21:
            st.title(":blue[YAML]")
        repository_link = st.text_input(label="Repository Name", placeholder = "Link to repository...", label_visibility = "collapsed")
        with col22:
            st.subheader("")
            push_to_github = st.button(label="Push to Github")  
        if submit:
            st.session_state.yaml_content = st.write_stream(generate(initial_prompt, user_input))

        if push_to_github:
            if len(st.session_state.yaml_content) and len(repository_link):
                push(access_token, yaml_content = st.session_state.yaml_content, repository_link = repository_link)
            elif len(st.session_state.yaml_content) == 0:
                st.warning("YAML file empty! Generate response by clicking on submit.")
            else:
                st.warning("Invalid Repository!")
=======
import streamlit as st
import ollama
import re

st.set_page_config(layout="wide")
# Create a title for the app
st.title("Project Crow")


col1, col2 = st.columns(2, gap="large")

with col1:
  user_input = st.text_area("Prompt")
<<<<<<<< HEAD:temp-ui.py
========
  repo_link = st.text_input("Paste your GitHub link here")
>>>>>>>> 4a227b77b32b8d25209390969a9453c59fc143d2:ui.py
  submit = st.button(label="Submit")
  


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
  response = ollama.generate(model="codellama", prompt=final_prompt, stream=True)
  yaml_content = ""
  for line in response["response"]:
    yaml_content += line#.decode("utf-8")
  return yaml_content
with col2:
    if submit:
        # Generate the YAML file based on the prompt and other input
        yaml_file = generate_yaml(prompt_input, user_input)

        # Display the generated YAML code in a code block for clarity
        
        pattern = r'```(.*?)```'
        matches = re.findall(pattern, yaml_file, re.DOTALL)


        content = matches[0].strip()
        # Print the extracted content
        st.code(content, language="yaml")
>>>>>>> 4a227b77b32b8d25209390969a9453c59fc143d2
