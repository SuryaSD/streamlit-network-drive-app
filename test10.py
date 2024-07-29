import streamlit as st
import pandas as pd
import os

# Path to the network drive
network_drive_path = r"G:\MERCH\VSL Reporting and Analytics\SAS\MSI_Data_Dump\Checking_Delete.xlsx"

@st.cache_resource
def load_data(filepath):
    # Check if the file exists
    if os.path.exists(filepath):
        # Read the CSV file
        data = pd.read_excel(filepath)
        return data
    else:
        st.error("File not found!")
        return pd.DataFrame()

def main():
    st.title("Network Drive Data Viewer")

    # Load data from the network drive
    data = load_data(network_drive_path)

    if not data.empty:
        # Display the data in a table
        st.write("Data from the network drive:")
        st.dataframe(data)
    else:
        st.write("No data available to display.")
        
user_id = os.getlogin()
st.write(user_id)

if __name__ == "__main__":
    main()
