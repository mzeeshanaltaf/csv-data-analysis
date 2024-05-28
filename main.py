from utility import *

# --- PAGE SETUP ---
# Initialize streamlit app
page_title = "CSV Whisperer "
page_icon = "📜"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Configure the API key
st.sidebar.title("Config️uration Options")
api_key, file_uploader = configure_apikey_sidebar()
st.sidebar.divider()
st.sidebar.subheader('About')
st.sidebar.markdown(''' Any Queries: Contact [Zeeshan Altaf](zeeshan.altaf@gmail.com)''')
st.sidebar.markdown(''' Source code: [GitHub](https://github.com/mzeeshanaltaf/csv-data-analysis)''')

st.title("CSV Whisperer")
st.write(":blue[***Unlock insights from your CSV data.***]")
st.write("Transform the way you interact with your data. Simply upload your CSV file, "
         "and effortlessly process and explore its contents. You can ask any question "
         "related to your CSV data and receive instant, accurate answers")


# Capture the CSV file
st.subheader('Upload CSV File:')
data = st.file_uploader("Upload CSV file", type="csv", disabled=not file_uploader, label_visibility="collapsed")

if data is None:
    prompt_activation = False
else:
    prompt_activation = True

st.subheader('Enter Your Query:')
query = st.text_input("Enter your query", disabled=not prompt_activation, label_visibility="collapsed")
button = st.button("Generate Response", type='primary', disabled=not prompt_activation)

if button:
    with st.spinner('Processing ...'):
        answer = query_agent(data, query, api_key)
        st.write(answer["output"])
