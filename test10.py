import streamlit as st
import pandas as pd
import os
import getpass
# Get the username from environment variable
username = os.getenv('USERNAME')

# Display the username in Streamlit
if username:
    st.write(f"Hello, {username}!")
else:
    st.write("Username environment variable not set.")
