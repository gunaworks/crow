# crowci

A streamlit app for generating CI/CD pipelines for your workflow. It can be deployed to [Streamlit Cloud](https://streamlit.io/cloud).

## Instructions to run the application locally.
1. Clone this repository.
2. Create a .env file inside the cloned directory and add the following variables.
### AUTHORIZATION_URL=https://github.com/login/oauth/authorize
### TOKEN_URL=https://github.com/login/oauth/access_token
### CLIENT_ID="Your GitHub OAuth App's Client ID"
### CLIENT_SECRET="You GitHub OAuth App's Client Secret"
### REDIRECT_URI=http://localhost:8501/component/streamlit_oauth.authorize_button/index.html
### OPENAI_API_KEY="Your openai api key"
3. Install the requirements using pip install -r requirements.txt.
4. Run the app using streamlit run main.py.
