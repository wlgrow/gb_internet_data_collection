import scrapy
import re
from scrapy.http import HtmlResponse
from parser_jobs.items import ParserJobsItem


class HhRuSpider(scrapy.Spider):
    name = "hh_ru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://kazan.hh.ru/search/vacancy?text=data+scientist&area="]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        jobs = response.xpath("//div[@class='vacancy-serp-item__layout']").getall()
        for _ in jobs:
            salary_min = 0
            salary_max = 0
            job_name = response.xpath("//a[@class='serp-item__title']/text()").get()
            job_url = response.xpath("//a[@class='serp-item__title']/@href").get()

            try:
                job_salary_string = response.xpath("//span[@data-qa='vacancy-serp__vacancy-compensation']/text()").get()

                s = re.match('[\d – ]+', job_salary_string)
                if s:
                    min_max = s.group().strip().replace(' ', '').replace(' ', '').replace(' ', '')
                    salary_min = int(min_max.split('–')[0])
                    salary_max = int(min_max.split('–')[1])
                else:
                    g = re.findall('[\d  ]+', job_salary_string)
                    if g:
                        if 'до' in job_salary_string:
                            salary_max = int(g[0].replace(' ', '').replace(' ', '').replace(' ', ''))
                        elif 'от' in job_salary_string:
                            salary_min = int(g[0].replace(' ', '').replace(' ', '').replace(' ', ''))
            except AttributeError:
                pass

            yield ParserJobsItem(
                name=job_name,
                url=job_url,
                min_salary=salary_min,
                max_salary=salary_max
            )
