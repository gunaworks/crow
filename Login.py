
#This FILE is not being used right now. Entry point to project is main.py!
import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Login",
)
st.sidebar.header("Login")
#new
hashed_passwords = stauth.Hasher(['abc','def']).generate()

import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
def main():
    name, authentication_status, username = authenticator.login('main')
    if authentication_status:
        try:
            authenticator.logout('Logout') 
        except Exception as err:
            st.error(f'Unexpected exception {err}')
            raise Exception(err)  # but not this, let's crash the app
        st.write(f'Welcome *{name}*')
        st.title('Some content')
    elif authentication_status is False:
        st.error('Username/password is incorrect')
    elif authentication_status is None:
        st.warning('Please enter your username and password')

    if authentication_status and st.button("Change Password"):
        try:
            if authenticator.reset_password(username, 'main'):
                st.success('Password modified successfully')
        except Exception as e:
            st.error(e)
    # if authentication_status and st.button("Update Details"):
    #     try:
    #         if authenticator.update_user_details(username, 'main'):
    #             st.success('Entries updated successfully')
    #     except Exception as e:
    #         st.error(e)
    # if st.button("Forgot Username"):
    #     try:
    #         username_forgot_username, email_forgot_username = authenticator.forgot_username('main')
    #         if username_forgot_username:
    #             st.success('Username sent securely')
    #             # Username to be transferred to the user securely
    #         else:
    #             st.error('Email not found')
    #     except Exception as e:
    #         st.error(e)

    with open('config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    
if __name__ == "__main__":
    main()