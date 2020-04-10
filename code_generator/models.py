#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Union, List

from luckydonaldUtils.logger import logging

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

__all__ = ['Route', 'Class', 'Parameter', 'ResponseType', 'UrlPath']


class Route(object):
    def __init__(self, name: str, method: str, path: 'UrlPath', allowed_query_parameters: List[str], description: str, response_format: 'ResponseType', example_url: str):
        self.name = name
        self.method = method
        self.path = path
        self.allowed_query_parameters = allowed_query_parameters
        self.description = description
        self.response_format = response_format
        self.example_url = example_url
    # end if

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, method={self.method!r}, path={self.path!r}, allowed_query_parameters={self.allowed_query_parameters!r}, description={self.description!r}, response_format={self.response_format!r}, example_url={self.example_url!r})"
    # end def

    __repr__ = __str__
# end class


class Class(object):
    def __init__(self, name, params):
        self.name = name
        self.params = params
    # end def

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, params={self.params!r})"
    # end def

    __repr__ = __str__
# end class


class Parameter(object):
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description
    # end def

    def get_type(self):
        return {
            'Integer': 'int',
            'String': 'str',
            'RFC3339 datetime': 'datetime',
            'Float': 'float',
            'Array': 'list',
            'Object': 'dict',
        }
    # end def

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, type={self.type!r}, description={self.description!r})"
    # end def

    __repr__ = __str__
# end class


class ResponseType(object):
    def __init__(self, schema: str, key: Union[str, None], is_list: bool, class_name: str):
        """
        :param schema: String representation of it. E.g. `{"images":[Image]}`
        :param key: The response is an dict with that key, e.g. `{"key": Object}`.
                    If set to `None` there is no wrapping dict, e.g. `Object`.
        :param is_list: If it is a list `[Image]` or just the plain `Image` object
        :param class_name: The name of the object, e.g. `"Image"`
        """
        self.schema = schema  # {"images":[Image]}
        self.key = key   # `{"key": Object}` or `Object` if None.
        self.is_list = is_list  # [Image] or Image
        self.class_name = class_name  # Image
    # end def

    def __str__(self):
        return f"{self.__class__.__name__}(schema={self.schema!r}, is_list={self.is_list!r}, key={self.key!r}, class_name={self.class_name!r}, python_typing_representation={self.python_typing_representation!r})"
    # end def

    def __repr__(self):  # without the property
        return f"{self.__class__.__name__}(schema={self.schema!r}, is_list={self.is_list!r}, key={self.key!r}, class_name={self.class_name!r})"
    # end def

    @property
    def python_typing_representation(self, wrap_if_key=True):
        string = self.class_name
        if self.is_list:
            string = f'List[{string}]'
        # end if
        if wrap_if_key and self.key:
            string = f'Dict[str, {string}]'
        # end if
        return string
# end class


class UrlPath(object):
    def __init__(self, original: str, template: str, params: List[Parameter]):
        self.original = original
        self.template = template
        self.params = params
    # end def

    def __str__(self):
        return f"{self.__class__.__name__}(original={self.original!r}, template={self.template!r}, params={self.params!r})"
    # end def

    __repr__ = __str__
# end class
