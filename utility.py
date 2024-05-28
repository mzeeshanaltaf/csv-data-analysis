import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
import streamlit as st


# Function to configure sidebar to verify and get the model  api key
def configure_apikey_sidebar():
    api_key = st.sidebar.text_input(f'Enter the API Key', type='password',
                                    help='Get API Key from: https://platform.openai.com/api-keys')
    if api_key == '':
        st.sidebar.warning('Enter the API key')
        file_uploader = False
    elif api_key.startswith('sk-') and (len(api_key) == 51):
        st.sidebar.success('Proceed to uploading the CSV file!', icon='️👉')
        file_uploader = True
    else:
        st.sidebar.warning('Please enter the correct credentials!', icon='⚠️')
        file_uploader = False

    return api_key, file_uploader


def query_agent(data, query, api_key):

    # Parse the CSV file and create a Pandas DataFrame from its contents.
    df = pd.read_csv(data)

    llm = ChatOpenAI(model='gpt-3.5-turbo-1106', temperature=0, api_key=api_key)

    # Create a Pandas DataFrame agent.
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    # Python REPL: A Python shell used to evaluating and executing Python commands.
    # It takes python code as input and outputs the result. The input python code can be generated from another tool in
    # the LangChain
    return agent.invoke(query)
