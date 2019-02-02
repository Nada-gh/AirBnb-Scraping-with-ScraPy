import scrapy
from scrapy.loader import ItemLoader
from demo_project.items import AirBnbItem
class AirBnbSpider(scrapy.Spider):

    # Identity
    name = 'AirBnb'
    allowed_domains = ["www.airbnb.ca"]

    # Requests
    #def start_requests(self):
     #   url = 'https://www.airbnb.ca/s/New-York/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=pYV_znhH'

      #  yield scrapy.Request(url=url, callback= self.parse)

    start_urls= [

        'https://www.airbnb.ca/s/New-York/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=pYV_znhH'
      
    ]

    # Response
    def parse(self, response):
        for div in response.xpath("//div[@class='_1wcpzyga']"):
            loader = ItemLoader(item=AirBnbItem(), selector= div, response= response)
            loader.add_xpath('Room_type', ".//span[@style='color: rgb(118, 118, 118);']/text()[1]")
            loader.add_xpath('num_of_beds', ".//span[@style='color: rgb(118, 118, 118);']/text()[2]")
            loader.add_xpath('Price', ".//span[@class='_12kw8n71']/span[position()=2]")
            loader.add_xpath('Cancel_policy', ".//div[@class='_1cm6f7d']/span[position()=2]")
            loader.add_xpath('Review_stars', ".//span[@class='_q27mtmr']/span/@aria-label")
            loader.add_xpath('num_of_reviewers', ".//span[@class='_1gvnvab']/child::span")
            yield loader.load_item()

        next_page = response.xpath("//li[@class='_b8vexar']/a")

        if next_page is not None:
         
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

          
       



        

        


