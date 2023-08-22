import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px
from gensim import corpora
from gensim.models.ldamodel import LdaModel
import streamlit.components.v1 as components
import pyLDAvis.gensim
import os
import spacy
import textwrap
import random


#streamlit layout settings
st.set_page_config(page_title="Clustering", page_icon="📍", layout="wide")


#page description on the sidebar
#st.sidebar.header("here goes the title")
#st.sidebar.text("here goes the description")


st.title(f"Clustering and Topic Modeling")
st.write("""Topic modeling and clustering to identify top topics and review clusters""")


#reading from csv file and converting it to dataframe
dir = os.path.dirname(__file__)
path = os.path.join(dir, '../reviews.csv')
data = pd.read_csv(path)
df = pd.DataFrame(data)


df ['datetime'] = pd.to_datetime(df['date'])
df['date'] = df['datetime'].dt.date


nlp = spacy.load("en_core_web_sm")

# Custom stopwords
custom_stopwords = [
    "app",
    "apple",
    "note",
    "account",
    "close",
    "open",
    "use",
    "user",
    "etc",
    "e.g.",
    "instance"
]


#cleaning, filtering and converting reviews text into tokens
def tokens(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc 
                    if not token.is_stop 
                    and not token.is_punct
                    and not token.is_digit
                    and len(token.lemma_) > 2 
                    and token.lemma_ not in custom_stopwords]

df = df[df['review'].str.len() > 100]

df['review_tokens'] = df['review'].apply(tokens)

df['review_tokens_str'] = df['review_tokens'].apply(' '.join)




#LDA Topic Modeling
st.title('Topic modeling')
st.write('Top topics and associated words\n')
st.write("\n")
dictionary = corpora.Dictionary(df['review_tokens'])
corpus = [dictionary.doc2bow(text) for text in df['review_tokens']]


lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=5, random_state=42)
lda_display = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)

#display topics and associated words
for idx, topic in lda_model.print_topics(-1):
    word_list = topic.split(" + ")
    words = "; ".join([word.split("*")[1].strip('"') for word in word_list])
    st.write(f"{idx}: {words}\n")


#display visualization on streamlit
html_path = "temp_lda_vis.html"
pyLDAvis.save_html(lda_display, html_path)

with open(html_path, 'r') as f:
    html_content = f.read()

components.html(html_content, width=1200, height = 800)


#sample reviews for each topic
st.subheader("Reviews from each Topic")
topic_sample = 3

for idx, topic in lda_model.print_topics(-1):
    st.write(f"Topic {idx}:")
    
    sample_reviews = random.sample(df['review'].tolist(), topic_sample)
    for review in sample_reviews:
        sample_review = '\n'.join(textwrap.wrap(review, width=80)) 
        st.text(sample_review)
        st.write("---") 






#clustering
st.title("k-means clustering")
st.write('Groups reviews that are considered similar together into a cluster')
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['review_tokens_str'])

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())

n_clusters=5
kmeans = KMeans(n_clusters)
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X)


#visualization
df_pca = pd.DataFrame(X_pca, columns=["Component 1", "Component 2"])
df_pca['Cluster'] = [str(label) for label in kmeans.labels_]

fig = px.scatter(df_pca, x="Component 1", y="Component 2", 
                 color='Cluster', 
                 title="Review Clusters", 
                 color_discrete_sequence=px.colors.qualitative.Set1,
                 hover_data=['Cluster'])

st.plotly_chart(fig, use_container_width = True)


#reviews within each cluster
st.subheader("Reviews from each cluster")

for cluster_num in range(n_clusters):
    st.write(f"Cluster {cluster_num} reviews:")
    subset = df['review'][kmeans.labels_ == cluster_num]
    sample_size = min(len(subset), 5)
    sample_reviews = subset.sample(sample_size)
    for review in sample_reviews:
        
        wrapped_review = '\n'.join(textwrap.wrap(review, width=80)) 
        st.text(wrapped_review)
        st.write("---") 



