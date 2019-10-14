import scrapy

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou-Spider'

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
            yield {
            'name': course.css('h3 a::text').extract_first().strip(),
            'update_time': course.css('div.d-inline-block relative-time::attr(datetime)').extract_first()
            }
