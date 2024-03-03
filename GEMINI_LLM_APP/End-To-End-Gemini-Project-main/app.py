# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
from google.cloud import aiplatform
from google.oauth2 import service_account

# Set the path to your JSON key file
json_credentials_path = "c:/Users/Hp/Downloads/gen-lang-client-0210070657-1ffb1a716066.json"

# Create a credentials object
credentials = service_account.Credentials.from_service_account_file(
    json_credentials_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Create a client options object with the credentials
client_options = aiplatform.ClientOptions(credentials=credentials)

# Set the name of the model you want to use
model_name = "Gemini LLM Application"

# Create a model object with the client options and model name
model = aiplatform.gapic.Model(client_options=client_options, model_name=model_name)

# Now you can use the model object to call the GenerativeService.GenerateContent method
response = model.generate_content(question)