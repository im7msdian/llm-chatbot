import streamlit as st
import openai

# Retrieve OpenAI API key from the secrets file
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Initialize OpenAI client
openai.api_key = openai_api_key

# Send a request to OpenAI to get a completion
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "What is Streamlit?"}
  ]
)

# Print the response to the Streamlit app
st.write(response.choices[0].message["content"])
