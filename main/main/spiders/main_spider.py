# -*- coding: utf-8 -*-

import scrapy
import datetime
import uuid
import bs4


class MainSpiderSpider(scrapy.Spider):
    name = "main_spider"
    start_urls = ["https://lenta.ru/rss/news"]

    def parse(self, response):
        items = response.xpath("//item")

        for item in items:
            title = item.xpath(".//title//text()").extract_first()
            link = item.xpath(".//link//text()").extract_first()
            publishedDateTime = item.xpath(".//pubDate//text()").extract_first()

            yield scrapy.Request(
                link,
                callback=self.parse_link,
                meta={
                    "item": {
                        "uid": str(uuid.uuid4()),
                        "link": link,
                        "title": title,
                        "importedDateTime": str(datetime.datetime.now()),
                        "publishedDateTime": publishedDateTime 
                    }
                }
            )

    def parse_link(self, response):
        item = response.meta["item"]

        content = []
        paragraphs = response.xpath("//p[.]").extract()
        for paragraph in paragraphs:
            soup = bs4.BeautifulSoup(paragraph)
            content += [p.get_text().strip() for p in soup.find_all("p")]

        item["content"] = " ".join(content)

        return item
