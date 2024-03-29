import streamlit as st
from oauth import OAuthHandler

# Import other necessary modules or functions

# Initialize OAuth handler
oauth_handler = OAuthHandler()

# Main function
def main():
    token = oauth_handler.get_token()
    if token:
        # Call other functions or components here
        st.title("Prompt to YAML")
        st.json(token)
        user_info = oauth_handler.get_user_info(token)
        if user_info:
            st.title("User Information")
            st.write(user_info['name'])
    else:
        oauth_handler.authorize()

if __name__ == "__main__":
    main()
