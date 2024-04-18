# crowci

A streamlit app for generating CI/CD pipelines for your workflow. It can be deployed to [Streamlit Cloud](https://streamlit.io/cloud).

## Instructions to run the application locally.
### Clone this repository.
### Create a .env file inside the cloned directory and add the following variables.
    AUTHORIZATION_URL=https://github.com/login/oauth/authorize
    TOKEN_URL=https://github.com/login/oauth/access_token
    CLIENT_ID="Your GitHub OAuth App's Client ID"
    CLIENT_SECRET="You GitHub OAuth App's Client Secret"
    REDIRECT_URI=http://localhost:8501/component/streamlit_oauth.authorize_button/index.html
    OPENAI_API_KEY="Your openai api key"
### Install the requirements.
    pip install -r requirements.txt
### Run the app.
    streamlit run main.py

## User Guide

### Descriptive input for an accurate pipeline.
#### Provide a descriptive input with as much specifications as possible so that the model generates an accurate pipeline. Example:
    Name: deploy-multi-env.yml (Push to main branch)

    Jobs:

    deploy:

    Runs on: ubuntu-latest
    Uses docker image: python:3.9
    Steps:
    Checkout code from main branch
    Install dependencies: pip install boto3
    deploy_staging (if ${{ github.event.branch }} == 'staging')

    Needs: deploy (This job waits for the deploy job to finish)
    Steps:
    Use AWS credentials stored in ${{ secrets.AWS_STAGING_KEY }} and ${{ secrets.AWS_STAGING_SECRET }} (stored securely)
    Configure environment variables for staging deployment using boto3
    deploy_production (if ${{ github.event.branch }} == 'master')

    Needs: deploy (This job waits for the deploy job to finish)
    Steps:
    Use AWS credentials stored in ${{ secrets.AWS_PRODUCTION_KEY }} and ${{ secrets.AWS_PRODUCTION_SECRET }} (stored securely)
    Configure environment variables for production deployment using boto3

#### Enter the repository link in the correct format (eg. https://github.com/your-github-username/your-repository-name).
![Generated Output](https://github.com/gunaworks/crowci/blob/ccj/images/generated_output.png)
#### Clicking on Push to GitHub button pushes the generated yaml file to the .github/workflows directory of your repository.