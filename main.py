from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from main.spiders.main_spider import MainSpider

settings = get_project_settings()
settings['ITEM_PIPELINES'] = {'main.pipelines.JsonWriterPipeline': 1}

process = CrawlerProcess(settings)
process.crawl(MainSpider)
process.start()
