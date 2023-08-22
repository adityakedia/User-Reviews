#reference library and documentation: https://github.com/cowboy-bebug/app-store-scraper

#importing modules and dependencies
from app_store_scraper import AppStore
import pandas as pd
import datetime


#default values to fetch reviews
range = "last 7 days"
today = datetime.date.today()
count = 100


#scraping reviews from Apple appstore
def scrape(app_name, country, app_id, cutoff, count):
     
    print (f"Scraping reviews for {app_name}")
    app = AppStore(country=country, app_name=app_name, app_id=app_id)
    app.review(how_many=count, after=cutoff)

    df = pd.DataFrame(app.reviews)
    df.to_csv('reviews.csv')

    return app.reviews_count


def get_cutoff(range):
    
    if range == "last 7 days":
        cutoff = today - datetime.timedelta(days=7)
    elif range == "last 15 days":
        cutoff = today - datetime.timedelta(days=15)
    elif range == "last 30 days":
        cutoff = today - datetime.timedelta(days=30)
    elif range == "last 90 days":
        cutoff = today - datetime.timedelta(days=90)
    else:
        return None, None

    cutoff = datetime.datetime(cutoff.year, cutoff.month, cutoff.day)

    return cutoff


if __name__ == "__main__":
    
    #cutoff = datetime('2023-08-08') 
    cutoff = get_cutoff("last 15 days")
    print(f"Start Date: {cutoff.date()}, End Date: {today}")
    
    reviews = scrape('amazon', 'us', 297606951, cutoff, count)
    print(f'Total reviews fetched: {reviews}')