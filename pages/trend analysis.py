import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from textblob import TextBlob
import os


#streamlit layout settings
st.set_page_config(page_title="Trend Analysis", page_icon="💹", layout="wide")


#page description on the sidebar
#st.sidebar.header("here goes the title")
#st.sidebar.text("here goes the description")


st.title(f"Trend Analysis")
st.write("""Trend Analysis of Ratings and Reviews!""")


#reading from csv file and converting it to dataframe
dir = os.path.dirname(__file__)
path = os.path.join(dir, '../reviews.csv')
data = pd.read_csv(path)
df = pd.DataFrame(data)


df ['datetime'] = pd.to_datetime(df['date'])
df['date'] = df['datetime'].dt.date



df['sentiment'] = df['review'].apply(lambda x: TextBlob(x).sentiment.polarity) #sentiment per review
df['review_length'] = df['review'].apply(len) #review length
daily_rev_count = df.groupby('date')['review'].count() #average review count 
daily_avg_rating = df.groupby('date')['rating'].mean().round(2) #average rating




#visualization of average ratings, user sentiment and review length over time
st.title("User Sentiment")
grouped = df.groupby('date').agg({
    'rating': 'mean',
    'review_length': 'mean',
    'sentiment': 'mean'
}).reset_index()

grouped['sentiment'] = grouped['sentiment'].round(2)

fig4 = px.scatter(grouped, 
                 x='date', 
                 y='rating', 
                 size='review_length', 
                 color='sentiment',
                 color_continuous_scale='Viridis', 
                 size_max=50,
                 title="Average Ratings and User Sentiment Over Time")

st.plotly_chart(fig4, use_container_width=True)



#user sentiment as per user review
avg_sentiment_ot = df.groupby('date')['sentiment'].mean().reset_index()
avg_sentiment_ot = avg_sentiment_ot.sort_values(by='date', ascending=False)
fig2 = px.line(avg_sentiment_ot.round(2), x='date', y='sentiment', title='User sentiment over time')
st.plotly_chart(fig2, use_container_width=True)
st.table(avg_sentiment_ot.head(5))


#correlation between sentiment and number of reviews per day:
group_by_day = df.groupby('date').agg(avg_sentiment=('sentiment', 'mean'),num_reviews=('review', 'size')).reset_index()
corr_sentiment_rev = round(group_by_day['avg_sentiment'].corr(group_by_day['num_reviews']), 2)
st.write(f'Correlation between average daily sentiment and number of reviews per day: {corr_sentiment_rev}')


#correlation between sentiment and rating
corr_sentiment_rating = df['sentiment'].corr(df['rating'])
st.write(f"Correlation between sentiment and rating: {corr_sentiment_rating:.2f}")




#distribution of ratings
st.title("Ratings")
#st.write(f"Total no. of ratings: {df['rating'].count()}" )
fig_ratings = px.histogram(df, x='rating', title="Distribution of ratings")
st.plotly_chart(fig_ratings)

#rating over time
daily_avg_rating = df.groupby('date')['rating'].count().reset_index()
daily_avg_rating = daily_avg_rating.sort_values(by='date', ascending=False)
rating_ot = px.line(daily_avg_rating, x='date', y='rating', title='Rating Over Time')
st.plotly_chart(rating_ot, use_container_width=True)
st.table(daily_avg_rating.head(5))



#distribution of review length
st.title("Reviews")
#st.write(f"Total no. of reviews: {df['review'].count()}" )
fig_length = px.histogram(df, x='review_length', title="Distribution of Review Lengths")
st.plotly_chart(fig_length)

#review count over time
daily_rev_count = df.groupby('date')['review'].count().reset_index()
daily_rev_count = daily_rev_count.sort_values(by='date', ascending=False)
review_ot = px.line(daily_rev_count, x='date', y='review', title='Reviews Over Time')
st.plotly_chart(review_ot, use_container_width=True)
st.table(daily_rev_count.head(5))

#avg review length over time
avg_rev_len = df.groupby('date')['review_length'].mean().reset_index()
avg_rev_len = avg_rev_len.sort_values(by='date', ascending=False)
review_len_ot = px.line(avg_rev_len, x='date', y='review_length', title='Review Length Over Time')
st.plotly_chart(review_len_ot, use_container_width = True)
st.table(avg_rev_len.head(5))



#sentiment and review length correlation
correlation_sentiment_length = round(df['sentiment'].corr(df['review'].str.len()), 2)
st.write(f'Correlation between sentiment and review length: {correlation_sentiment_length}')


#review length and rating correlation
correlation_review_length_rating = df['review_length'].corr(df['rating'])
st.write(f"Correlation between review length and rating: {correlation_review_length_rating:.2f}")


# #review count and review length correlation
# daily_avg_rev_len = df.groupby('date')['review_length']
# corr_rev_count_len = daily_rev_count.corr(daily_avg_rev_len)
# st.write(f"Correlation between daily review count and average review length: {corr_rev_count_len:.2f}")


# #review count and rating correlation
# daily_avg_rating = df.groupby('date')['rating'].mean()
# correlation = daily_rev_count['review'].count().corr(daily_avg_rating['rating'])
# st.write(f"Correlation between daily review count and average rating: {correlation_review_count_rating:.2f}")

# Review count and review length correlation
daily_avg_rev_len = df.groupby('date')['review_length'].mean()
daily_rev_count = df.groupby('date').size()
corr_rev_count_len = daily_rev_count.corr(daily_avg_rev_len)
st.write(f"Correlation between daily review count and average review length: {corr_rev_count_len:.2f}")

# Review count and rating correlation
daily_avg_rating = df.groupby('date')['rating'].mean()
corr_rev_count_rating = daily_rev_count.corr(daily_avg_rating)
st.write(f"Correlation between daily review count and average rating: {corr_rev_count_rating:.2f}")








