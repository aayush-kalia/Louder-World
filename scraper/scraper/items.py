import scrapy

class ScraperItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
