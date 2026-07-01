import streamlit as st

st.title("Application Settings")

st.selectbox(

    "LLM",

    [

        "Azure OpenAI",

        "OpenAI"

    ]

)

st.checkbox(

    "Enable RAG",

    value=True

)

st.checkbox(

    "Enable MCP",

    value=True

)