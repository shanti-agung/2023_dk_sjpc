# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SjpcscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        ## remove space and unwanted characters in rpt table names
        rpt_raw = adapter.get('rpt_name')
        value = rpt_raw.strip("View name:").strip("\t")
        adapter['rpt_name'] = value

        return item
