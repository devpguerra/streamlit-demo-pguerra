import streamlit as st
import requests

FASTAPI_URL = "http://fastapi:80/"

def get_data_from_fastapi():
    try:
        # Send a GET request to the FastAPI endpoint
        response = requests.get(FASTAPI_URL)
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return JSON data from FastAPI
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Request failed: {e}"

# Streamlit app layout
st.title("Streamlit App - Fetch Data from FastAPI!")

if st.button("Fetch Data"):
    data = get_data_from_fastapi()
    st.write(data)  # Display the data fetched from FastAPI
