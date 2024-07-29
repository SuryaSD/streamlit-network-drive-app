import streamlit as st
import pandas as pd
import os
import getpass
#st.write(getpass.getuser())

# Get the username from environment variable
username = os.getenv('USERNAME')

# Display the username in Streamlit
st.write(f"Hello, {username}!")
