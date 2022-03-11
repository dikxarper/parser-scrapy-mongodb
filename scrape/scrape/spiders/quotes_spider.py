import scrapy
from ..items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
          item = QuoteItem()

          item['author'] = quote.css('small.author::text').get()
          item['text'] = quote.css('span.text::text').re(r'“(.+)”')[0]
          item['tags'] = quote.css('div.tags a.tag::text').getall()

          yield item

        for a in response.css('ul.pager a'):
          yield response.follow(a, callback=self.parse)