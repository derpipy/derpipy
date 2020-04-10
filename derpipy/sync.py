import requests


class Client(object):
    """
    Client for working
    """

    def __init__(self, api_key):
        self.__api_key = api_key

    # end if

    from models import *
    Route(
        name='filter',
        method='GET',
        path=UrlPath(
            original='/api/v1/json/filters/:filter_id',
            template='/api/v1/json/filters/{filter_id}',
            params=[
                Parameter(
                    name='filter_id',
                    type='Integer',
                    description='the variable filter_id part of the url.',
                    optional=False,
                )
            ]
        ),
        allowed_query_parameters=[
            Parameter(
                name='key',
                type='String',
                description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).',
                optional=True,
            )
        ],
        description='Fetches a **filter response** for the filter ID given by the `filter_id` URL parameter.',
        response_format=ResponseType(
            schema='{"filter":Filter}',
            is_list=False,
            key='filter',
            class_name='Filter'
        ),
        example_url='/api/v1/json/filters/56027'
    )

    _base_url = 'https://derpibooru.org'

    # def {{ route.description }}(self, filter_id: int, key: str=None):
    def filter(self, filter_id: int, key: str=None):
        """
        {{ route.description }}

        :param {{ param.name }}: {{ param.description }}
        :param key:
        :return:
        """
        # url = self._base_url + f{{ repr(route.path.template) }}
        url = self._base_url + f'/api/v1/json/filters/{filter_id}'
        # resp = requests.request({{repr(route.method)}}, url)
        resp = requests.request('GET', url)
        assert resp.status_code == 200  # TODO
        assert resp.headers['content-type'] == 'application/json; charset=utf-8'
        resp.json()


