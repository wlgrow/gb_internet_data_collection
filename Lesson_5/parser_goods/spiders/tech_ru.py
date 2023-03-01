import scrapy
from scrapy.http import HtmlResponse
from parser_goods.items import ParserGoodsItem

class TechRuSpider(scrapy.Spider):
    name = "technopoint_ru"
    allowed_domains = ["technopoint.instavktok.ru"]
    start_urls = ["https://technopoint.instavktok.ru/"]

    def parse(self, response: HtmlResponse):
        goods_links = response.xpath("//a[@class='c-product-thumb__name c-link c-link_style_hover']/@href").getall()
        for link in goods_links:
            yield response.follow(link, callback=self.parse_good)

        print('\n########\n%s\n########\n' %response.url)

    def parse_good(self, response: HtmlResponse):
        good_name = response.xpath("//h1[@class='c-header c-header_h1']/text()").getall()[0]
        good_url = response.url
        good_price = response.xpath("//span[@class='c-product-add-to-cart__price']/text()").getall()[0]
        good_brand = response.xpath("//span[span[@class='c-value__label-text'] = 'Бренд:']/span[@class='c-value__value-text c-link-decorator']/text()").getall()[0]

        yield ParserGoodsItem(
            name=good_name,
            url=good_url,
            price=int(good_price.replace(" ", "")),
            brand=good_brand
        )

