# MongoDB & Scrapy Demonstration

This project was created at the Advanced Databases (NoSQL) at Astana IT University.

## Get started

Clone the repository:

```
git clone git@github.com/dikxarper/parser-scrapy-mongodb
cd scrapy
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

Go to the `scrape` folder and start the crawler:

```
cd mongodb_crawler
scrapy crawl books -s MONGO_URI="<CONN_STRING>" -s MONGO_DATABASE="DATABASE_NAME"
```

## Source

MongoDB & Scrapy Demonstration: https://github.com/mongodb-developer/scrapy
