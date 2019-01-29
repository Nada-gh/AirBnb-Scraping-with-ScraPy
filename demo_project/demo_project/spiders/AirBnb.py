import scrapy
from scrapy.loader import ItemLoader
from demo_project.items import AirBnbItem

class AirBnbSpider(scrapy.Spider):
    #identity
    name = 'AirB'

    #Requests
    def start_requests(self):
        url= 'https://www.airbnb.ca/s/New-York/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=pYV_znhH'

        yield scrapy.Request(url=url, callback=self.parse)
    

    #Response
    def parse(self, response):
        for i in response.selector.xpath("//div[@class='_1wcpzyga']"):
            loader = ItemLoader(item=AirBnbItem(), selector=i, response= response)
            loader.add_xpath('Title',".//div[@class='_ng4pvpo']/text()")
            loader.add_xpath('room_type',".//span[@style='color: rgb(118, 118, 118);']/text()[1]")
            loader.add_xpath('num_of_beds',".//span[@style='color: rgb(118, 118, 118);']/text()[2]")
            loader.add_xpath('price',".//span[@class='_12kw8n71']/child::span/child::span[2]")
            yield loader.load_item()

           
        next_page= response.selector.xpath("//li[@class='_b8vexar']/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
    