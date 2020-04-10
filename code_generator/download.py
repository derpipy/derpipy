#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from luckydonaldUtils.logger import logging
import requests

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

page = requests.get('https://derpibooru.org/pages/api')
with open('./output/api.html', 'w') as f:
    f.write(page.text)
# end with
