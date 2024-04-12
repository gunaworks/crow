import streamlit as st
from oauth import OAuthHandler
import extra_streamlit_components as stx

# Initialize OAuth handler and CookieManager
oauth_handler = OAuthHandler()
cookie_manager = stx.CookieManager()

# Main function
def main():
    # Retrieve token from cookie manager
    token = cookie_manager.get("token")

    # Check if 'token' is not in session state, if not initialize it
    if 'token' not in st.session_state:
        st.session_state.token = None

    # If token exists in session state, display user information
    if st.session_state.token:
        st.title("Prompt to YAML")
        st.json(st.session_state.token)
        user_info = oauth_handler.get_user_info(st.session_state.token)
        if user_info:
            st.title("User Information")
            st.write(user_info['name'])
    
    # If no token exists in session state, attempt to retrieve it
    else:
        token = oauth_handler.get_token()
        if token:
            # Set token in session state and cookie
            st.session_state.token = token
            cookie_manager.set("token", token)
        else:
            # If token retrieval fails, initiate OAuth authorization flow
            oauth_handler.authorize()

if __name__ == "__main__":
    main()
