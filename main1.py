import streamlit as st
# from oauth import OAuthHandler
from ui import ui
import os
from oauth import OAuthHandler
import extra_streamlit_components as stx
import datetime
# Import other necessary modules or functions
oauth_handler = OAuthHandler() 
@st.cache_resource(experimental_allow_widgets=True)
def get_manager():
    return stx.CookieManager()

cookie_manager = get_manager()
# Initialize OAuth handler
def set_logout():
    st.session_state.logout = True
    cookie_manager.delete("token")
# Main function
def main():
    token = oauth_handler.get_token()
    token_val = cookie_manager.get("token")
    if 'logout' not in st.session_state:
        st.session_state.logout = False
    if token:
        cookie_manager.set("token", token)
    if token and st.session_state.logout == False:
        # oauth_handler.set_token(token)
        # Call other functions or components here
        user_info = oauth_handler.get_user_info(token)
        access_token = token['access_token']
        if user_info:
            ui(access_token)
            st.button("Logout", on_click=set_logout)
    elif token_val and st.session_state.logout == False:
        try:
            access_token = token_val['access_token']
            ui(access_token)
            st.button("Logout", on_click=set_logout)
        except Exception as e:
            oauth_handler.authorize()
    else:
        oauth_handler.authorize()
if __name__ == "_main_":
    main()