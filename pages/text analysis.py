#text analytics for app store reviews

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import plotly.express as px
import spacy
import os



#streamlit layout settings
st.set_page_config(page_title="Text Analysis", page_icon="🆎", layout="wide")


#page description on the sidebar
#st.sidebar.header("here goes the title")
#st.sidebar.text("here goes the description")


st.title(f"Text Analysis")
st.write("""Analysing text from the app store reviews!""")


#reading from csv file and converting it to dataframe
dir = os.path.dirname(__file__)
path = os.path.join(dir, '../reviews.csv')
data = pd.read_csv(path)
df = pd.DataFrame(data)


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

df['review_tokens'] = df['review_tokens'].apply(' '.join)



#categories and associated keywords
categories = {
    "Usability": [
        "intuitive", "easy", "complicated", "complex", "simple", 
        "user-friendly", "difficult", "challenging", "straightforward", 
        "confusing", "convenient", "inconvenient", "practical", "impractical"
    ],
    "Features": [
        "feature", "function", "option", "setting", "tool", 
        "capability", "missing", "lacking", "abundant", "variety", 
        "flexible", "rigid", "versatile"
    ],
    "Performance": [
        "slow", "fast", "lag", "freeze", "crash", "performance", 
        "responsive", "unresponsive", "efficient", "inefficient", 
        "seamless", "buggy", "smooth"
    ],
    "Support": [
        "help", "support", "response", "customer service", "assistance", 
        "quick", "slow", "helpful", "unhelpful", "friendly", "rude", 
        "knowledgeable", "ignorant"
    ],
    "Pricing": [
        "price", "expensive", "cheap", "cost", "value", "overpriced", 
        "underpriced", "worth", "not worth", "affordable", "pricey", 
        "economic", "budget"
    ],
    "Bugs/Issues": [
        "bug", "error", "issue", "crash", "problem", "glitch", 
        "fault", "defect", "malfunction", "break", "failure", "flaw"
    ]
}

#categorizing reviews into predefined categories
st.title("Review Categorization")
def categorize_review(review):
    assigned_categories = []
    for category, keywords in categories.items():
        if any(keyword in review for keyword in keywords):
            assigned_categories.append(category)
    return ', '.join(assigned_categories) if assigned_categories else 'Other'

df['category'] = df['review_tokens'].apply(categorize_review)

category_counts = df['category'].value_counts()

st.bar_chart(category_counts)
st.table(df[['review', 'category']].head(5))



# Bigram Analysis
st.title(f"Bigram Analysis")
st.write("""Displays the count of two adjacent tokens that appears frequently together""")

bi_vector = CountVectorizer(ngram_range=(2, 2))
bi_matrix = bi_vector.fit_transform(df['review_tokens'])
bi_freq = sum(bi_matrix).toarray()[0]
bi_df = pd.DataFrame({'bigram': bi_vector.get_feature_names_out(), 'count': bi_freq})
top_bi = bi_df.sort_values('count', ascending=False).head(20)

fig_bi = px.bar(top_bi, x='bigram', y='count', title="Top 20 Bigrams")
st.plotly_chart(fig_bi, use_container_width = True)
st.table(top_bi.head(5).reset_index(drop=True))


# Trigram Analysis
st.title(f"Trigram Analysis")
st.write("""Displays the count of three adjacent tokens that appears frequently together""")

tri_vector = CountVectorizer(ngram_range=(3, 3))
tri_matrix = tri_vector.fit_transform(df['review_tokens'])
tri_freq = sum(tri_matrix).toarray()[0]
tri_df = pd.DataFrame({'trigram': tri_vector.get_feature_names_out(), 'count': tri_freq})
top_tri = tri_df.sort_values('count', ascending=False).head(20)

fig_tri = px.bar(top_tri, x='trigram', y='count', title="Top 20 Trigrams")
st.plotly_chart(fig_tri, use_container_width = True)
st.table(top_tri.head(5).reset_index(drop=True))