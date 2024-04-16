import streamlit as st
from oauth import OAuthHandler
from home import ui
# Import other necessary modules or functions

# Initialize OAuth handler
oauth_handler = OAuthHandler()

# Main function
def main():
    token = oauth_handler.get_token()
    if token:
        # oauth_handler.set_token(token)
        # Call other functions or components here
        user_info = oauth_handler.get_user_info(token)
        access_token = token['access_token']
        if user_info:
            ui(access_token)
    else:
        oauth_handler.authorize()

if __name__ == "__main__":
    main()

# import streamlit as st
# # from oauth import OAuthHandler
# from experiments import OAuthHandler
# from home import ui
# import os
# import extra_streamlit_components as stx
# import datetime
# import time

# # Import other necessary modules or functions
# oauth_handler = OAuthHandler() 
# @st.cache_resource(experimental_allow_widgets=True)
# def get_manager():
#     return stx.CookieManager()

# cookie_manager = get_manager()

# # # Initialize OAuth handler
# # def set_logout():
# #     st.session_state.logout = True
# #     cookie_manager.delete("token")
# # Main function
# def main():
#     token = oauth_handler.get_token()
#     # token_val = cookie_manager.get("token")
#     # if 'logout' not in st.session_state:
#     #     st.session_state.logout = False
#     if token:
#         # cookie_manager.set("token", token)
#         #and st.session_state.logout == False:
#         # oauth_handler.set_token(token)
#         # Call other functions or components here
#         user_info = oauth_handler.get_user_info(token)
#         access_token = token['access_token']
#         if user_info:
#             ui(access_token)
#             # st.button("Logout")
#     else:
#         # token_val = cookie_manager.get("token")
#         # if token_val:
#         #     access_token = token_val['access_token']
#         #     ui(access_token)
#         # else:
#         oauth_handler.authorize()
#         token_val = oauth_handler.get_token()
#         cookie_manager.set("token", token_val)

# main()  

# import streamlit as st
# from home import ui
# import experiments
# import extra_streamlit_components as stx
# import datetime
# import time

# cookie_manager = stx.CookieManager()
# # Main function
# def main():
#     token = experiments.get_token()
#     token_val = cookie_manager.get("token")
#     st.write(token_val)
#     if token:
#         # experiments.set_token(token)
#         # Call other functions or components here
#         user_info = experiments.get_user_info(token)
#         access_token = token['access_token']
#         if user_info:
#             st.write(access_token)
#     elif token_val:
#         ui(token_val)
#     else:
#         experiments.authorize()
#         token_val = "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"
#         cookie_manager.set("token", token_val)


# if __name__ == "__main__":
#     main()