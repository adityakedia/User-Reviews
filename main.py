#main page for streamlit dashboard using multi page app setup

from scraper import scrape, get_cutoff
import streamlit as st

#page layout
st.title("iOS App Store Reviews Analysis")
st.write("Please enter the App details below to start fetching reviews:")



app_name = st.text_input("Enter App Name:")
app_id = st.text_input("Enter App ID:")
country = st.selectbox('Choose a country:', ['us', 'in', 'uk', 'au', 'my', 'sg', 'ng', 'jp', 'bd', 'pk', 'mx', 'ph', 'vn', 'et', 'eg', 'de', 'ir', 'tr', 'cd', 'fr'])
range = st.selectbox('Choose a date range:', ["last 7 days",  "last 15 days", "last 30 days", "last 90 days"])
count = st.selectbox('Choose number of reviws to fetch:', ["25", "50", "100", "200", "500"])


if st.button("Fetch Reviews"):
    
    st.write(f"Fetching {app_name} reviews for {range}. It may take few minutes")
    
    cutoff = get_cutoff (range)
    reviews = scrape(app_name, country, int(app_id), cutoff, int(count))  

    #once done, display the following
    st.write(f"Fetched {reviews} reviews")
    st.markdown("# pages/fetched reviews")