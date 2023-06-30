import scrapy
from sjpcscraper.items import RptFieldItem


class PenelopespiderSpider(scrapy.Spider):
    name = "penelopespider"
    allowed_domains = ["intercom.help"]
    start_urls = ["https://intercom.help/ssgpenelope/en/articles/5189678-views-and-standard-views"]

    def parse(self, response):
        views = response.css('div.intercom-interblocks-table')[0]
        categories = views.css('table tr a')
        for category in categories:
            category_url = category.css('a').attrib['href']
            yield scrapy.Request(category_url, callback=self.parse_category)

    def parse_category(self, response):
        body = response.css('div.article_body')
        headers = body.xpath('//div[contains(@class,"intercom-interblocks-heading")]/following-sibling::div[1]/p')
        tables = response.css('div.intercom-interblocks-table')
        num_tables = len(tables)

        for i in range(num_tables):
            view_category = response.css('header::text').get()
            rpt_name = headers[i].xpath('text()').get()
            table = tables[i]
            table_rows = table.css('table tr')
            for row in table_rows:
                is_header_row = (row.css('p ::text').get() == 'Field')
                if not is_header_row:
                    field_item = RptFieldItem()
                    field_item['category'] = view_category
                    field_item['rpt_name'] = rpt_name
                    field_item['field_name'] = row.xpath('td[1]/div/p/text()').get()
                    field_item['data_type'] = row.xpath('td[2]/div/p/text()').get()
                    field_item['notes'] = row.xpath('td[3]/div/p/text()').get()
                    yield field_item
                

