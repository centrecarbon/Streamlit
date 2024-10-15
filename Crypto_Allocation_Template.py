import streamlit as st
import pandas as pd

# Set the title for the app
st.title("Crypto Profit Diversification Calculator")

# Description
st.write("Enter the total amount to see how funds are allocated across different networks based on predefined percentages.")

# Load the Excel file
file_path = 'Crypto_Allocation_Template.xlsx'  # Path to your Excel file
df = pd.read_excel(file_path)

# Create an input form for the total amount
total_amount = st.number_input("Enter total amount", min_value=0.0)

# Calculate the allocation based on the input amount
if total_amount > 0:
    df['Amount Allocated'] = df['Percentage (%)'] / 100 * total_amount
    st.write("Calculated Allocations:")
    st.dataframe(df[['Network', 'Percentage (%)', 'Amount Allocated']])

# Option to download the updated Excel file
if st.button('Download Updated Excel File'):
    # Save the updated Excel file with allocated amounts
    df.to_excel('Updated_Crypto_Allocation.xlsx', index=False)
    with open('Updated_Crypto_Allocation.xlsx', 'rb') as file:
        st.download_button('Download', file, file_name='Updated_Crypto_Allocation.xlsx')
