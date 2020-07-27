#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from jinja2.environment import Environment
from jinja2.exceptions import TemplateSyntaxError
from jinja2.loaders import FileSystemLoader
from luckydonaldUtils.files.basics import mkdir_p
from luckydonaldUtils.logger import logging

from output.api1 import routes, classes

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if


class RelEnvironment(Environment):
    """
    Override join_path() to enable relative template paths.

    http://stackoverflow.com/a/8530761/3423324
    """
    def join_path(self, template, parent):
        return os.path.join(os.path.dirname(parent), template)
    # end def join_path
# end class RelEnvironment


def get_template(file_name):
    env = RelEnvironment(loader=FileSystemLoader("templates"))
    try:
        return env.get_template(file_name)
    except TemplateSyntaxError as e:
        logger.warn("{file}:{line} {msg}".format(msg=e.message, file=e.filename if e.filename else file_name, line=e.lineno))
        raise e
    # end with
# end def get_template

init_template = get_template("init.template")
classes_template = get_template("classes.template")
functions_template = get_template("functions.template")

mkdir_p('../derpi/syncrounous/')
mkdir_p('../derpi/asyncrounous/')

with open('../derpi/syncrounous/__init__.py', 'w') as f:
    f.write(init_template.render(is_asyncio=False))
# end with
with open('../derpi/asyncrounous/__init__.py', 'w') as f:
    f.write(init_template.render(is_asyncio=True))
# end with

with open('../derpi/syncrounous/client.py', 'w') as f:
    f.write(functions_template.render(routes=routes, is_asyncio=False))
# end with
with open('../derpi/asyncrounous/client.py', 'w') as f:
    f.write(functions_template.render(routes=routes, is_asyncio=True))
# end with

with open('../derpi/syncrounous/models.py', 'w') as f:
    f.write(classes_template.render(classes=classes, is_asyncio=False))
# end with
with open('../derpi/asyncrounous/models.py', 'w') as f:
    f.write(classes_template.render(classes=classes, is_asyncio=True))
# end with





