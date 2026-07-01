import streamlit as st

st.title("Portfolio Analytics")

st.dataframe(

    [

        {

            "Security": "AAPL",

            "Weight": 7.2

        },

        {

            "Security": "MSFT",

            "Weight": 6.5

        }

    ]

)