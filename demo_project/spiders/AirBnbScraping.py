import scrapy
from scrapy.loader import ItemLoader
from demo_project.items import AirBnbItem
class AirBnbSpider(scrapy.Spider):

    # Identity
    name = 'AirBnb'

    # Requests
    def start_requests(self):
        url = 'https://www.airbnb.ca/s/New-York/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=pYV_znhH'

        yield scrapy.Request(url=url, callback= self.parse)

    # Response
    def parse(self, response):
        item = AirBnbItem()
        for div in response.selector.xpath("//div[@class='_1wcpzyga']"):
                item['Title'] = div.xpath(".//div[@class='_ng4pvpo']/text()").extract()
                item['Room_type']= div.xpath(".//span[@style='color: rgb(118, 118, 118);']/text()[1]").extract()
                item['num_of_beds'] = div.xpath(".//span[@style='color: rgb(118, 118, 118);']/text()[2]").extract()
                item['Price'] = div.xpath(".//span[@class='_12kw8n71']/span[position()=2]").extract()
                item['Cancel_policy']= div.xpath(".//div[@class='_1cm6f7d']/span[position()=2]").extract()
                item['Review_stars'] = div.xpath(".//span[@class='_q27mtmr']/span/@aria-label").extract()
                item['num_of_reviewers']= div.xpath(".//span[@class='_1gvnvab']/child::span").extract()
                yield item

          
       



        

        


