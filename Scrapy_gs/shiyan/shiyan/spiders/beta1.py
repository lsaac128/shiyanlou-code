# -*- coding: utf-8 -*-
import scrapy
from shiyan.items import ShiyanItem

class Beta1Spider(scrapy.Spider):
    name = 'beta1'

    start_urls = ['https://www.shiyanlou.com/courses/63']

    def parse(self, response):
        item = {'title': response.css('h1.course-title::text').extract_first(
                         ).strip(),
                'name': response.css('p.teacher-info span::text'
                        ).extract_first()
        }

        for url in response.css('div.course-item-box a::attr(href)'):
            yield response.follow(url, callback=self.parse)

        yield item
