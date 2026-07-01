import streamlit as st

st.title("Enterprise AI Copilot")

question = st.text_area(

    "Ask anything about your portfolio"

)

if st.button("Submit"):

    st.success(

        "AI response will appear here."

    )