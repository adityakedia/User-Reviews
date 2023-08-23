# App Store Review Analysis
This project was done as an internal project to help the orgnization gather and analyze user reviews from Apple app store. This was to help the organization understand user sentiment and trends and make better strategic decisions. 

This is a Python application that utilizes an app store scraper to collect app reviews for a given app name, ID, and country. It performs various text analyses, including trend analysis, cluster analysis, and sentiment analysis on the collected reviews. The results are then displayed using a Streamlit dashboard.

____
## Installation
### Clone the repository
git clone https://github.com/adityakedia/User-Reviews.git

____
## Install the required dependencies
pip install -r requirements.txt

____
## Run the application
streamlit run main.py

____
## Usage
Access the Streamlit dashboard in your web browser.

Enter the app name, ID, and country for which you want to analyze app reviews.

Click on the "Fetch Reviews" button to initiate the scraping process.

Once the reviews are collected, it will perform various analyses, including
 
- Trend analysis, 
- N-Gram analysis,
- Text classification,
- Cluster analysis, 
- Topic modeling,
- and Sentiment analysis.

Explore the results presented in the Streamlit dashboard, which provides interactive visualizations and insights based on the analyzed reviews.

____
## Acknowledgements
This project utilizes the following open-source libraries and tools:

### App Store Scraper
A [Python library ](https://github.com/cowboy-bebug/app-store-scraper)for scraping Apple app store reviews.

### Streamlit 
A web framework for building interactive dashboards and applications in Python.
