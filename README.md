# Get started
Install dependencies
```
python -m pip install -f requirements.txt
```

Start the crawler
```
scrapy crawl quotes -s MONGO_URI="<CONN_STRING>" -s MONGO_DATABASE="scrapy"
```