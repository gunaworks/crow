import streamlit as st
from ui import ui
from oauth import OAuthHandler
import extra_streamlit_components as stx

# Initialize OAuth handler and CookieManager
oauth_handler = OAuthHandler()
cookie_manager = stx.CookieManager()

# Function to set logout
def set_logout():
    st.session_state.logout = True
    cookie_manager.delete("token")

# Main function
def main():
    # Retrieve token from OAuth handler
    token = oauth_handler.get_token()

    # Retrieve token from cookie manager
    token_val = cookie_manager.get("token")

    # Check if 'logout' is not in session state, if not initialize it
    if 'logout' not in st.session_state:
        st.session_state.logout = False

    # If token exists, store it in cookie
    if token:
        cookie_manager.set("token", token)

    # If token exists and logout is False, authenticate user and display UI
    if token and not st.session_state.logout:
        user_info = oauth_handler.get_user_info(token)
        access_token = token['access_token']
        if user_info:
            ui(access_token)
            st.button("Logout", on_click=set_logout)

    # If token exists in cookie and logout is False, display UI using token from cookie
    elif token_val and not st.session_state.logout:
        try:
            access_token = token_val['access_token']
            ui(access_token)
            st.button("Logout", on_click=set_logout)
        except Exception as e:
            oauth_handler.authorize()

    # If no token exists, initiate OAuth authorization flow
    else:
        oauth_handler.authorize()

if __name__ == "__main__":
    main()
