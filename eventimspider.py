import scrapy


class EventimspiderSpider(scrapy.Spider):
    name = 'eventimspider'
    
    start_urls = ['https://www.eventim.de/en/events/konzerte-1/jazz-blues-4/']

    def parse(self, response):
        events=response.css('div.listing-item')
        for event in events:
            #here we put the data returned into the format we want to output for our csv or json file
            yield{
                'name' : event.css('div.event-listing-city.theme-text-color::text').get(),
                'discription' : event.css('div.listing-description.theme-text-color.line-clamp.hidden-xs::text').get(),
                'date' : event.css('span.listing-data.theme-text-color span::text').get(),
                #'rate' : response.css('span.rating-icon-wrapper[title]').get().replace('<span class="rating-icon-wrapper" role="img" title="','').replace('" aria-label="4.71 out of 5 stars">\n<i class="icon icon-rating-star-full"></i>\n<i class="icon icon-rating-star-full"></i>\n<i class="icon icon-rating-star-full"></i>\n<i class="icon icon-rating-star-full"></i>\n<i class="icon icon-rating-star-half"></i>\n</span>',''),
            }
        next_page = response.css('[data-qa="nextPage"]::attr(href)').get()

        if next_page is not None:
          next_page_url = 'https://www.eventim.de/' + next_page
          yield response.follow(next_page_url, callback=self.parse)
