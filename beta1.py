# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class Beta1Spider(scrapy.Spider):
    name = 'beta1'
    allowed_domains = ['shiyanlou.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for course in response.css('div.col-10.col-lg-9.d-inline-block'):
            item = ShiyanlouItem({
                'name': course.css('div.d-inline-block.mb-1 a::text').extract_first().strip(),
                'update_time': course.css('div.f6.text-gray.mt-2 relative-time::attr(datetime)').extract_first()
            })
            yield item

        yield {
                'commits': response.css('span.num.text-emphasized::text').extract()[0].strip(),
                'branches': response.css('span.num.text-emphasized::text').extract()[1].strip(),
                'releases': response.css('span.num.text-emphasized::text').extract()[2].strip()
            }
        for url in response.css('div.col-10.col-lg-9.d-inline-block a::attr(href)'):
            yield response.follow(url, callback=self.parse)
