import scrapy
from datetime import date  

class PopularTagsSpider(scrapy.Spider):
    name = 'populartags'
    start_urls = [
        'https://www.detik.com/',
    ]

    def parse(self, response):
        for tag in response.css('div.tagging'):
            yield {
                'popular-tags': tag.css('div.tagging a::text').getall()
            }