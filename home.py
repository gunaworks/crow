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
            submit = st.button(label="Submit", key="submit_key")


    with col2:
        col21, col22= st.columns(2, gap="small")
        yaml_content = ""
        with col21:
            st.title(":blue[YAML]")
        repository_link = st.text_input(label="Repository Name", key = "RepositoryLink", placeholder = "Link to repository...", label_visibility = "collapsed")

        with col22:
            st.subheader("")
            push_to_github = st.button(label="Push to Github", key = "push_to_github_key")  
        if submit:
            st.session_state.yaml_content = st.write_stream(generate(initial_prompt, user_input))

        if push_to_github:
            if len(st.session_state.yaml_content) and len(repository_link):
                push(access_token, yaml_content = st.session_state.yaml_content, repository_link = repository_link)
            elif len(st.session_state.yaml_content) == 0:
                st.warning("YAML file empty! Generate response by clicking on submit.")
            else:
                st.warning("Invalid Repository!")