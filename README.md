# Get started
Install dependencies
```
python -m pip install -r requirements.txt
```

Go to the `scrape` folder and start the crawler
```
cd mongodb_crawler
scrapy crawl quotes -s MONGO_URI="<CONN_STRING>" -s MONGO_DATABASE="scrapy"
```

Open your `scrapy` database with Compass, there should be 110 documents in the `scrapy_items` collection.
