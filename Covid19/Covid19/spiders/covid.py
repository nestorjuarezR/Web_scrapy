import scrapy
from Covid19.items import Covid19Item

class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['https://www.bbc.com/news/world-51235105']
    start_urls = ['http://https://www.bbc.com/news/world-51235105/']

    def parse(self, response):
        item = Covid19Item()
        deaths_convert = []

        deaths = [x.strip() for x in response.css("table.core-table tbody tr.core__row td.c__c[aria-label=Deaths]::text").getall()]
        [deaths_convert.append(int(x.replace(",","") if x !="" else 0 ))  for x in deaths]
        item['country'] = [x.strip() for x in response.css("table.core-table tbody tr.core__row td.c__r ::text").getall()]
        item['deaths'] =  deaths_convert
        yield item