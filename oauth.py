"""This module is for OAuth using GitHub."""
import os
from dotenv import load_dotenv
from streamlit_oauth import OAuth2Component
import streamlit as st
import requests
load_dotenv()

class OAuthHandler:
    """OAuthHandler class"""
    def __init__(self):
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.authorization_url = os.environ.get('AUTHORIZATION_URL')
        self.token_url = os.environ.get('TOKEN_URL')
        self.redirect_uri = os.environ.get('REDIRECT_URI')
        self.scope = "user repo project workflow"
        self.oauth2 = OAuth2Component(self.client_id, self.client_secret,
                                      self.authorization_url, self.token_url,
                                      self.redirect_uri, self.scope)
####################################################################################
    def authorize(self):
        """authorize method"""
        #Using empty st.title to shift the contents of the page a bit down
        st.title("")
        st.title("")
        st.markdown("""<h1 style='text-align: center; color: #CFF089;'>
                    Welcome to CrowCI</h1>""",
                    unsafe_allow_html=True)
        st.markdown("""<h2 style='text-align: center; color: white;'>
                    Login with your GitHub account to continue...</h2>""",
                    unsafe_allow_html=True)
        st.title("")
        left_padding, center_column, right_padding = st.columns([2,2,1])
        with center_column:
            result = self.oauth2.authorize_button("Login", self.redirect_uri, self.scope)
        if result and 'token' in result:
            st.session_state.token = result.get('token')
            st.rerun()
            return result['token']
        return None
####################################################################################
    def get_token(self):
        """get_token method"""
        if 'token' not in st.session_state:
            return None
        return st.session_state['token']
####################################################################################
    def get_user_info(self, access_token):
        """get_user_info method"""
        token_string = access_token.get('access_token')
        headers = {"Authorization": f"token {token_string}"}
        response = requests.get("https://api.github.com/user", headers=headers)
        if response.status_code == 200:
            return response.json()
        st.error("Failed to fetch user information.")
        st.error(response.status_code)
        st.error(response.content)
        return None
