from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from thevergeSpider.items import VergeReview

class VergeSpider(CrawlSpider):
    name = "thevergeSpider01"
    allowed_domains = ["theverge.com"]
    start_urls = ["https://www.theverge.com/reviews"]
    rules = [
        Rule(LinkExtractor(allow=r'https://www\.theverge\.com/(\d+)/[^/]+$'),
             callback="parse_item",
             follow=True)
    ]

    def parse_item(self, response):
        verge_review = VergeReview()
        verge_review["url"] = response.url
        verge_review["title"] = response.xpath('//h1/text()').extract_first()
        verge_review["author_name"] = response.xpath('//a[contains(@href, "/authors")]/text()').get()
        link_author_profile = response.xpath('//a[contains(@href, "/authors/")]/@href').get()
        if link_author_profile:
            verge_review["link_author_profile"] = response.urljoin(link_author_profile)
        else:
            verge_review["link_author_profile"] = "Something is wrong"
        yield verge_review




