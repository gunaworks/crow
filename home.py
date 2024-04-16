from yaml_generator import generate
import streamlit as st
from github_push import push

def ui(access_token):
    st.set_page_config(layout="wide")

    left_padding, col1, mid_gap, col2, right_padding = st.columns([1, 1.7 ,.01, 2.5, .5], gap="large")
    
    if 'yaml_content' not in st.session_state:
        st.session_state.yaml_content = ""

    with col1:
        col11, col12 = st.columns([.8,2])
        with col12:
            st.title("Input")
        with st.form(key="Input", clear_on_submit=False, border=True):
            user_input = st.text_area(label="Input",height=250 ,key="InputBox", placeholder="Ask CrowCI...", label_visibility="hidden")
            form_front_gap, form_submit_col =  st.columns([3,1])
            with form_submit_col:
                submit = st.form_submit_button("Submit")


    with col2:
        st.markdown("<h1 style='text-align: center; color: #CFF089;'>YAML</h1>", unsafe_allow_html=True)
        repository_link = st.text_input(label="Repository Name", key = "RepositoryLink", 
                                        placeholder = "Link to repository...", 
                                        label_visibility = "collapsed")
    
        with st.form(key="Output", clear_on_submit=False, border=True):
            st.write("YAML Pipeline will be generated here...")
    
            if submit:
                st.session_state.yaml_content = generate(user_input=user_input)
                st.write(st.session_state.yaml_content)
    
            push_to_github = st.form_submit_button(label="Push to Github")  

        if push_to_github:
            if len(st.session_state.yaml_content) and len(repository_link):
                push(access_token, yaml_content = st.session_state.yaml_content, repository_link = repository_link)
            elif len(st.session_state.yaml_content) == 0:
                st.warning("YAML file empty! Generate response by clicking on submit.")
            else:
                st.warning("Invalid Repository!")