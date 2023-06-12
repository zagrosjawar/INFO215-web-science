# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#############
import scrapy
'''
task 1
Create a class 'VergeReview' by extending scrapy.Item class.
Include attributes to store following information:
 URL, Title (first h1 text), authorname (who made the review), link to author profile
'''

class VergeReview(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()  # title (first h1 text)
    author_name = scrapy.Field()  # who made the review
    link_author_profile = scrapy.Field()

