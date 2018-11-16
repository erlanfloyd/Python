import scrapy

class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.zakon.kz/']

    def parse(self, response):
        for href in response.css('.product_pod a::attr(href)').extract():
            url = response.urljoin(href)
            print(url)
