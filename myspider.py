import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    name_of_object = 'cat'
    start_urls = ['https://en.wikipedia.org/w/index.php?title=Special:WhatLinksHere/' + name_of_object + '&namespace=4&limit=500']
    def parse(self, response):
        for title in response.css('mw-content-text'):
            yield {'title': title.css('a ::text').extract_first()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)

#for link in response.css('')
