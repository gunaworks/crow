import os
from dotenv import load_dotenv
from streamlit_oauth import OAuth2Component
import streamlit as st
import requests

# Load environment variables
load_dotenv()

class OAuthHandler:
    def __init__(self):
        self.client_id = os.environ.get('CLIENT_ID')
        self.client_secret = os.environ.get('CLIENT_SECRET')
        self.authorization_url = os.environ.get('AUTHORIZATION_URL')
        self.token_url = os.environ.get('TOKEN_URL')
        self.redirect_uri = os.environ.get('REDIRECT_URI')
        self.scope = "user repo project admin"
        self.oauth2 = OAuth2Component(self.client_id, self.client_secret, self.authorization_url, self.token_url,  self.redirect_uri, self.scope)
    def authorize(self):
        st.title("")
        st.title("")
        st.markdown("<h1 style='text-align: center; color: #CFF089;'>Welcome to CrowCI</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: white;'>Login with your GitHub account to continue...</h2>", unsafe_allow_html=True)
        
        st.title("")
        col1, col2, col3 = st.columns([2,2,1])
        with col2:
            result = self.oauth2.authorize_button("Login", self.redirect_uri, self.scope)
        if result and 'token' in result:
            st.session_state.token = result.get('token')
            st.rerun()
            return result['token']
    def get_token(self):
        if 'token' not in st.session_state:
            return None
        return st.session_state['token']
    
    def get_user_info(self, access_token):
        token_string = access_token.get('access_token')
        headers = {"Authorization": f"token {token_string}"}
        response = requests.get("https://api.github.com/user", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch user information.")
            st.error(response.status_code)
            st.error(response.content)
            return None
