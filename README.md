# MongoDB & Scrapy Demonstration

This project demonstrates how to use Scrapy to scrape data from a website and store it in a MongoDB database. You can follow the accompanying tutorial to [Build a Web Scraper with MongoDB](https://www.mongodb.com/basics/how-to-use-mongodb-to-store-scraped-data).

## Get started

Clone the repository:

```
git clone git@github.com:mongodb-developer/scrapy.git
cd scrapy
```

Install dependencies:
```
python -m pip install -r requirements.txt
```

Go to the `scrape` folder and start the crawler:
```
cd mongodb_crawler
scrapy crawl quotes -s MONGO_URI="<CONN_STRING>" -s MONGO_DATABASE="scrapy"
```

Open your `scrapy` database with Compass, there should be 110 documents in the `scrapy_items` collection.

## Disclaimer

Use at your own risk; not a supported MongoDB product
