# Get started
Install dependencies
```
python -m pip install -r requirements.txt
```

Go to the `scrape` folder and start the crawler
```
cd scrape
scrapy crawl quotes -s MONGO_URI="<CONN_STRING>" -s MONGO_DATABASE="scrapy"
```
