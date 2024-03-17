from datetime import datetime
import streamlit as st

import WRPC_DSM_UI_Accounts
import WRPC_REGIONAL_ENERGY_ACCOUNTS

def download_file():
    filename = f"Extracted Data_WRPC_SRPC_{datetime.now().strftime('%d-%m-%Y')}.xlsx"
    with open(filename, "rb") as f:
        file_content = f.read()
    st.download_button(label="Download File", data=file_content, file_name=filename)

if __name__ == '__main__':
    st.markdown('### WRPC SRPC EXTRACT DATA')
    
    years = ['2024','2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010']
    # Create dropdown widgets for selecting the year and title filter
    selected_year = st.selectbox('Select a Year:', years)
    current_month = datetime.now().strftime('%B')
    months = ["January", "February", "March", "April","May", "June", "July", "August","September", "October", "November", "December"] 
    selected_month = st.selectbox("Select a month", options=months, index=0, format_func=lambda x: x.title())
    checkbox_labels = ["WRPC Regional Accounts", "WRPC DSM UI Accounts", "SRPC Option 1", "SRPC Option 2"]
    
    # Create multiple checkboxes
    checkbox_values = [st.checkbox(label) for label in checkbox_labels]

    # Define a dictionary mapping each label to a tuple containing its corresponding function and its arguments
    function_mapping = {
        "WRPC Regional Accounts": (WRPC_REGIONAL_ENERGY_ACCOUNTS.extract_data, selected_year, selected_month),
        "WRPC DSM UI Accounts": (WRPC_DSM_UI_Accounts.fetch_pdfs, selected_year, selected_month),
        # "SRPC Option 1": (process_option_3, arg1, arg2),
        # "SRPC Option 2": (process_option_4, arg1, arg2)
    }

    if st.button('Extract Data'):
        for label, value in zip(checkbox_labels, checkbox_values):
            if value:
                func, *args = function_mapping[label]
                func(*args)  # Call the corresponding function with its arguments based on the selected option
        
        download_file()
