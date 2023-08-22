import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from textblob import TextBlob
import textwrap
import os

#streamlit layout settings
st.set_page_config(page_title="Sentiment", page_icon="😁", layout="wide")


#page description on the sidebar
#st.sidebar.header("here goes the title")
#st.sidebar.text("here goes the description")


st.title(f"Sentiment Analysis")
st.write("""Sentiment Analysis of the Reviews!""")


#reading from csv file and converting it to dataframe
dir = os.path.dirname(__file__)
path = os.path.join(dir, '../reviews.csv')
data = pd.read_csv(path)
df = pd.DataFrame(data)


df ['datetime'] = pd.to_datetime(df['date'])
df['date'] = df['datetime'].dt.date


data['polarity'] = data['review'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
data['subjectivity'] = data['review'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)

data['polarity'] = data['polarity'].round(2)
data['subjectivity'] = data['subjectivity'].round(2)
data['review'] = data['review'].apply(lambda x: '\n'.join(textwrap.wrap(str(x), width=50)))

st.table(data[['polarity', 'subjectivity']].describe())
st.table(data[['review', 'rating', 'polarity', 'subjectivity']].head())




