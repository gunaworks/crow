import streamlit as st
from oauth import OAuthHandler
from home import home_page

oauth_handler = OAuthHandler()

# Main function
def main():
    token = oauth_handler.get_token()
    if token:
        access_token = token['access_token']
        home_page(access_token)
    else:
        oauth_handler.authorize()

if __name__ == "__main__":
    main()