# crowci

A streamlit app for generating CI/CD pipelines for your workflow. It can be deployed to [Streamlit Cloud](https://streamlit.io/cloud).

## Instructions to run the application locally.
### Clone this repository.
### Create a .env file inside the cloned directory and add the following variables.
    * AUTHORIZATION_URL=https://github.com/login/oauth/authorize
    * TOKEN_URL=https://github.com/login/oauth/access_token
    * CLIENT_ID="Your GitHub OAuth App's Client ID"
    * CLIENT_SECRET="You GitHub OAuth App's Client Secret"
    * REDIRECT_URI=http://localhost:8501/component/streamlit_oauth.authorize_button/index.html
    * OPENAI_API_KEY="Your openai api key"
### Install the requirements.
    pip install -r requirements.txt
### Run the app.
    streamlit run main.py
