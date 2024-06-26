by Aditya Kedia | Jun 2023

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
## Screenshots

![My Remote Image](https://file.notion.so/f/f/88bf9889-7860-4f8c-99cf-ee8a0e9f1c53/06d855cc-ae25-479f-9dbb-980b40a06d2b/Untitled.png?id=85450ad2-6597-47fe-841f-752d5e6fb0ed&table=block&spaceId=88bf9889-7860-4f8c-99cf-ee8a0e9f1c53&expirationTimestamp=1710302400000&signature=_bINv_MmYSw10sgDcsjqNkUAK41j4k3bqvMkVcIOUCw&downloadName=Untitled.png)

![My Remote Image](https://file.notion.so/f/f/88bf9889-7860-4f8c-99cf-ee8a0e9f1c53/50e8f002-da81-4117-a43b-8e1ae0ea25e7/Untitled.png?id=68a74c7f-0954-4fe1-b31a-f78429685c8e&table=block&spaceId=88bf9889-7860-4f8c-99cf-ee8a0e9f1c53&expirationTimestamp=1710302400000&signature=sZ35_aAYzMqAqR1OohhfQYMh_J4VSuwac3ru9qseMAM&downloadName=Untitled.png)

![image](https://file.notion.so/f/f/88bf9889-7860-4f8c-99cf-ee8a0e9f1c53/8dca3af5-7bae-4b40-a07f-c2836cd230a0/Untitled.png?id=5dc0ebc7-4217-4870-9f08-d30c13c289a2&table=block&spaceId=88bf9889-7860-4f8c-99cf-ee8a0e9f1c53&expirationTimestamp=1710302400000&signature=uGyqRTFmimzi94vlaMrzMi1lJLcRq4KpvJ9_qlRQLTM&downloadName=Untitled.png)


____
## Acknowledgements
This project utilizes the following open-source libraries and tools:

### App Store Scraper
A [Python library ](https://github.com/cowboy-bebug/app-store-scraper)for scraping Apple app store reviews.

### Streamlit 
A web framework for building interactive dashboards and applications in Python.
