import scrapy, re
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://alpinabook.ru/catalog/']

    def parse(self, response):
        # Parse each quote div 

        BOOK_SELECTOR = '.b-catalog-items__item'
        NAME_SELECTOR = 'span[itemprop="name"]::text'
        AUTHOR_SELECTOR = 'span[itemprop="author"]::text'
        OLD_PRICE_SELECTOR = '.book-item-price_old::text'
        NEW_PRICE_SELECTOR = '.js-book-item__price::text'
        COVER_SELECTOR = '.book-item-offer__name::text'       
        LABEL_SELECTOR = '.js-book-item-labels__item::text'        
        NEXT_PAGE_SELECTOR = '.b-paginator a::attr("href")'      

        for book in response.css(BOOK_SELECTOR):
            item = BookItem()

            name = book.css(NAME_SELECTOR).get()
            # removing white spaces both in the beginning and in the end of a string
            name = re.sub("^\s+|\s+$", "", name, flags=re.UNICODE)

            label = book.css(LABEL_SELECTOR).get()

            new_price = book.css(NEW_PRICE_SELECTOR).get()
            # removing all non-numeric characters in a string
            if new_price is not None:  
                new_price = re.sub("[^0-9]", "", new_price)

            old_price = book.css(OLD_PRICE_SELECTOR).get()
            # removing all non-numeric characters in a string
            if old_price is not None:  
                old_price = re.sub("[^0-9]", "", old_price)

            cover = book.css(COVER_SELECTOR).get()
            author = book.css(AUTHOR_SELECTOR).getall()
            
            print(new_price)
            item['name'] = name
            item['author'] = author
            item['new_price'] = new_price
            item['old_price'] = old_price
            item['cover'] = cover
            item['label'] = label

            yield item

        # Find the "Next ->" button and follow the link
        next_page = response.css(NEXT_PAGE_SELECTOR).get()

        if next_page:
            yield scrapy.Request(   
                response.urljoin(next_page),
                callback=self.parse
            )

    