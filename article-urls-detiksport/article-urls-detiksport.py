import scrapy

class ArticleLinkSpider(scrapy.Spider):
    name = 'article'
    start_urls = [
        'https://sport.detik.com/?tag_from=wp_firstnav_detiksport',
    ]

    def parse(self, response):
        for article in response.css('article'):
            yield {
                'url': article.css('a::attr("href")').get(),
            }