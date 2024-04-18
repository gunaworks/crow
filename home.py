"""This is the home page module"""
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from yaml_generator import generate
from github_push import push_to_github

def home_page(access_token):
    """Displays the ui after oauth."""
    st.set_page_config(layout="wide")
    [left_padding, input_column, mid_gap,
     yaml_output_column,right_padding] = st.columns([.8, 1.8 ,.01, 2.5, .3], gap="large")
    if 'yaml_content' not in st.session_state:
        st.session_state.yaml_content = ""
#################################################################################################
    with input_column:
        st.markdown("<h1 style='text-align: center; color: #6699CC;'>Input</h1>",
                    unsafe_allow_html=True)
        with st.form(key="Input", clear_on_submit=False, border=True):
            user_input = st.text_area(label="Input",height=250 ,key="InputBox",
                                      placeholder="Ask CrowCI...", label_visibility="hidden")
            form_left_padding, form_submit_column =  st.columns([3,1])
            with form_submit_column:
                submit = st.form_submit_button("Submit")
#################################################################################################
    with yaml_output_column:
        st.markdown("<h1 style='text-align: center; color:#6699CC;'>YAML</h1>",
                    unsafe_allow_html=True)
        with st.container(height=300, border=True):
            st.markdown("""<h6 style='text-align: center;color: white;'>
                        Pipeline generated below...</h6>""",
                        unsafe_allow_html=True)
            st.write("")
            if submit:
                st.session_state.yaml_content = generate(user_input)
                with stylable_container("codeblock","""code {white-space:
                                        pre-wrap !important;}""",):
                    st.code(st.session_state.yaml_content, language = "yaml")

        repository_link_column, push_to_github_column = st.columns([3.2,1])
        with repository_link_column:
            repository_link = st.text_input(label="Repository Name",
                                            placeholder = "Link to repository...",
                                            label_visibility = "collapsed")
        with push_to_github_column:
            push_to_github_button = st.button(label="Push to Github")
        if push_to_github_button:
            if len(st.session_state.yaml_content) > 0 and len(repository_link) > 0:
                push_to_github(access_token, yaml_content = st.session_state.yaml_content,
                                    repository_link = repository_link)
            elif len(st.session_state.yaml_content) == 0:
                st.warning("YAML file empty! Generate response by clicking on submit.")
            else:
                st.warning("Enter the repository link.")
