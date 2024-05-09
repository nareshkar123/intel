import joblib
import streamlit as st
st.title("SPAM HAM CLASSIFICATION")
reload_model = joblib.load('spam-model')

#ask the user to give input for prediction to check if spam or not

ip = st.text_input("Enter message", "Type yr msg", key="placeholder")
op = reload_model.predict([ip])
if st.button('PREDICT'):
    st.title(op[0])

