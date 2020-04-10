#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

from jinja2.environment import Environment
from jinja2.exceptions import TemplateSyntaxError
from jinja2.loaders import FileSystemLoader
from luckydonaldUtils.files.basics import mkdir_p
from luckydonaldUtils.logger import logging

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

from output.api import routes, classes

init_template = get_template("init.template")
classes_template = get_template("classes.template")
functions_template = get_template("functions.template")

mkdir_p('../derpipy/sync/')

with open('../derpipy/sync/__init__.py', 'w') as f:
    f.write(init_template.render(is_asyncio=False))
# end with

with open('../derpipy/sync/client.py', 'w') as f:
    f.write(functions_template.render(routes=routes, is_asyncio=False))
# end with

with open('../derpipy/sync/models.py', 'w') as f:
    f.write(classes_template.render(classes=classes, is_asyncio=False))
# end with





