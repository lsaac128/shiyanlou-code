# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class RepositoriesSpider(scrapy.Spider):
    name = 'repositories'
    allowed_domains = ['https://www.girhub.com']

    @property
    def start_urls(self):
        url_list = ['https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwODoyNzoxMSswODowMM4FkpTa&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMi0wM1QxMToyODoxNCswODowMM4BzS4l&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wNFQwMDoxNzo1MyswODowMM4BpCnu&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0wOS0xNlQxMDowNjowMyswODowMM4Bb3Ud&tab=repositories'
                ]
        return url_list

    def parse(self, response):
        for course in response.css('div.d-inline-block'):
            item = ShiyanlouItem({
                'name': course.css('h3 a::text').extract_first().strip(),
                'update_time': course.css('div.text-gray relative-time::attr(datetime)').extract_first()
                })
            yield item
