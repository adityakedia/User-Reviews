#display raw data as fetched from app store

import streamlit as st
import pandas as pd
import os

#streamlit layout settings
st.set_page_config(page_title="Fetched Reviews", page_icon="🌍", layout="wide")


#page description on the sidebar
#st.sidebar.header("here goes the title")
#st.sidebar.text("here goes the description")


st.title(f"Fetched Reviews")
st.write("""Reviews fetched from Apple app store!""")


#reading from csv file and converting it to dataframe
dir = os.path.dirname(__file__)
path = os.path.join(dir, '../reviews.csv')
data = pd.read_csv(path)
df = pd.DataFrame(data)


#displaying data table on streamlit
def data_table():
   st.dataframe(data, height=400,  use_container_width = True)


if __name__ == "__main__":
    data_table()