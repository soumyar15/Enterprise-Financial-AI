import streamlit as st

st.title("Investment Research")

company = st.text_input(

    "Company Name"

)

if st.button("Generate Research"):

    st.success(

        "Research report generated."

    )