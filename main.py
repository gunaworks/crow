import streamlit as st
from oauth import OAuthHandler
from home import ui

oauth_handler = OAuthHandler()

# Main function
def main():
    token = oauth_handler.get_token()
    if token:
        user_info = oauth_handler.get_user_info(token)
        access_token = token['access_token']
        if user_info:
            ui(access_token)
    else:
        oauth_handler.authorize()

if __name__ == "__main__":
    main()