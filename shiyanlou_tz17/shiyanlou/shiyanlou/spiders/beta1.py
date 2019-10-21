# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import ShiyanlouItem

class Beta1Spider(scrapy.Spider):
    name = 'beta1'
    #allowed_domains = ['github.com']
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for course in response.css('li.col-12.d-flex'):
            item = ShiyanlouItem({
                'name': course.css('div.d-inline-block.mb-1 a::text').extract_first().strip(),
                'update_time': course.css('div.f6.text-gray.mt-2 relative-time::attr(datetime)').extract_first()
                })
            course_url = course.css('h3 a::attr(href)').extract_first()
            full_course_url = response.urljoin(course_url)
            request = scrapy.Request(full_course_url, self.parse_author)
            request.meta['item'] = item
            yield request
            if response.css('div.BtnGroup button::text').extract_first() == 'Previous':
                xiayiye = response.css('div.BtnGroup a::attr(href)').extract_first()
                yield response.follow(xiayiye, callback=self.parse)
            elif len(response.css('div.BtnGroup a::attr(href)')) == 2:
                xiayiye = response.css('div.BtnGroup a::attr(href)').extract()[1]
                yield response.follow(xiayiye, callback=self.parse)
            elif response.css('div.BtnGroup button::text').extract_first() == 'Next':
                pass
            
    
    def parse_author(self, response):
        item = response.meta['item']
        item['commits'] = response.css('span.num.text-emphasized::text').extract()[0].strip()
        item['branches'] = response.css('span.num.text-emphasized::text').extract()[1].strip()
        item['releases'] = response.css('span.num.text-emphasized::text').extract()[2].strip()
        yield item
