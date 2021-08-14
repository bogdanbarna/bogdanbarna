# -*- coding: utf-8 -*-

import os
import re
import scrapy
from badgeupdate.items import BadgeSrc

BADGE_URL = os.environ["BADGE_URL"]


class BadgeSpider(scrapy.Spider):
    name = "badgespider"
    start_urls = [BADGE_URL]

    def parse(self, response):
        for img in response.xpath("//img").extract():
            if "cr-standard-grid-item-content__image" in img:
                self.logger.info(img)
                badge_src = re.match(r'^.*src="(.*)">$', img).groups()[0]
                # Spider must return request, item, or None
                yield BadgeSrc(badge_src=badge_src)
