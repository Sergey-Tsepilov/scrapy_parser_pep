import scrapy


class PepParseItem(scrapy.Item):
    """Представляет данные одного PEP: номер, название и статус."""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
