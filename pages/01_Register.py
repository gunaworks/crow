import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Register",
)
st.sidebar.header("Register")

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
registration_status = False
try:
    new_email, new_username, new_name = authenticator.register_user('main',preauthorization=False, fields={'Form name': 'Register User'})
    if new_email: 
        st.success("Successfully Registered!")
except Exception as e:
    st.error(e)

with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)