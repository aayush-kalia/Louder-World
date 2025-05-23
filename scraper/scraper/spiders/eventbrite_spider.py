import scrapy
from scraper.items import ScraperItem  

class EventbriteSpider(scrapy.Spider):
    name = "eventbrite"
    allowed_domains = ["eventbrite.com.au"]
    start_urls = [
        "https://www.eventbrite.com.au/d/australia--sydney/events/"
    ]

    def parse(self, response):
        events = response.css('div.eds-event-card-content__content')

        for event in events:
            item = ScraperItem()
            item['title'] = event.css('div.eds-event-card__formatted-name--is-clamped::text').get()
            item['date'] = event.css('div.eds-event-card-content__sub-title::text').get()
            item['location'] = event.css('div.card-text--truncated__one::text').get()
            item['url'] = event.css('a::attr(href)').get()
            item['description'] = None  # Optional: scrape description from the event page later
            yield item

