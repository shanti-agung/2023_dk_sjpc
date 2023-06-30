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
        value = rpt_raw.replace("View name:", "").strip(" :\t")
        value = (value.encode('ascii', 'ignore')).decode("utf-8")
        adapter['rpt_name'] = value

        ## impute the missing view name
        view_name = adapter.get('rpt_name')
        if view_name == "":
            adapter['rpt_name'] = "rpt.bluebook_provider_profile" 

        return item
