import scrapy

class BookItem(scrapy.Item):
    author = scrapy.Field()
    name = scrapy.Field()
    new_price = scrapy.Field()
    cover = scrapy.Field()
    old_price = scrapy.Field()
    label = scrapy.Field()
