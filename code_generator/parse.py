import json
import bs4
import re
from luckydonaldUtils.logger import logging
from typing import List, Dict
from bs4 import NavigableString
from models import *
logging.add_colored_handler(level=logging.DEBUG)
logger = logging.getLogger(__name__)

FILE = 'api0'
with open(f'./output/{FILE}.html', 'r') as f:
    html = f.read()
# end with

parsed = bs4.BeautifulSoup(html)
main = parsed.select_one('.walloftext')


RE_URL_PRAMS_STR = r':(?P<param>\w+)'  # https://regex101.com/r/78JlNQ/1/
RE_URL_PRAMS = re.compile(RE_URL_PRAMS_STR)
RE_URL_PRAMS_REPLACEMENT = r"{\g<param>}"


def parse_description(description: List[bs4.PageElement]):
    string = ''
    for tag in description:
        if isinstance(tag, NavigableString):
            string += str(tag)
        elif tag.name == 'a' and tag.attrs.get('href', None):
            if tag.attrs.get('href', '').startswith('#'):
                string = f'`{class_names[tag.attrs["href"]]}`'
            else:
                string += f'[{tag.text}](https://derpibooru.org{tag.attrs["href"]})'
            # end if
        else:
            string += tag.text.join({'em': ['**'] * 2, 'code': ['`'] * 2, 'br': ['\n', ''], None: [''] * 2}[tag.name])
        # end if
    # end for
    string.replace('\r\n', '\n')
    return string
# end def


class_names = {}

class_names['https://github.com/derpibooru/cli_intensities'] = 'Intensities'
for element in main.find_all('h2'):
    if element.text and 'id' in element.attrs and element.attrs['id'] and element.attrs['id'].endswith('-response') and element.text.endswith(' Responses'):
        name = element.text[:-10]  # ' Responses' has length 10.
        class_names['#' + element.attrs['id']] = name
    # end if
# end for


classes = []

if FILE == 'api':
    classes.append(Class('Intensities', [
        Parameter("ne", 'Float', 'Northeast intensity. Whatever that means…'),
        Parameter("nw", 'Float', 'Northwest intensity. Whatever that means…'),
        Parameter("se", 'Float', 'Southeast intensity. Whatever that means…'),
        Parameter("sw", 'Float', 'Southwest intensity. Whatever that means…'),
    ]))
    classes.append(Class('Representations', [
        Parameter(key, 'String', f'A mapping of the {key!r} representation names to their respective URLs.')
        for key in ["full", "large", "medium", "small", "tall", "thumb", "thumb_small", "thumb_tiny"]
    ]))
else:
    classes.append(Class('SearchResult', [
        Parameter('hits', 'List[T]', 'List of results'),
        Parameter('total', 'Integer', 'Total amount of results, e.g. for pagination.'),
    ]))
# end if

for element in main.find_all('h2'):
    if element.text and 'id' in element.attrs and element.attrs['id'] and element.attrs['id'].endswith('-response') and element.text.endswith(' Responses'):
        name = element.text[:-10]  # ' Responses' has length 10.

        c = Class(name, [])
        id = element.attrs['id']

        table = element.find_next('table')
        column_headers = []
        for column in table.find_all('th'):
            column_headers.append(column.text)
        # end if
        logger.debug(f'column_headers: {column_headers!r}')
        assert column_headers == ['Field', 'Type', 'Description']
        rows = table.find_all('tr')[1:]  # skip the <thead>
        for row in rows:
            columns = row.find_all('td')
            param = columns[0].code.text
            logger.debug(f'{name}.{param}: {columns[1].text!r}, {columns[2].text!r}')

            if name == 'Image' and param == 'representations':  # because there is no real link to a object.
                type = 'Representations'
            else:
                type = (
                    (
                        [
                            (class_names[t.attrs["href"]])
                            for t in columns[2].contents if not isinstance(t, NavigableString) and t.name == 'a' and t.attrs.get('href', '')
                        ][0]
                    ) if columns[1].text == 'Object' else (
                        columns[1].text
                    )
                )
            # end if
            description = parse_description(columns[2].contents)
            optional = 'optional' in description.lower()

            p = Parameter(
                name=param,
                type=type,
                description=description,
                optional=optional,
            )
            c.params.append(p)
        # end for
        classes.append(c)
    # end if
# end def


query_parameters: Dict[str, Parameter] = {}

element = main.select_one('h2#parameters')
table = element.find_next('table')
column_headers = []
for column in table.find_all('th'):
    column_headers.append(column.text)
# end if
logger.debug(f'column_headers: {column_headers!r}')
assert column_headers == ['Name', 'Description']
rows = table.find_all('tr')[1:]  # skip the <thead>'s <tr> (containing only <td>s anyway)

for row in rows:
    columns = row.find_all('td')
    param = columns[0].code.text
    description = parse_description(columns[1].contents)
    logger.debug(f'{param}: {columns[1].text!r}')
    optional = 'optional' in description.lower()
    query_parameters[param] = Parameter(param, None, description, optional=optional)
# end for

query_parameters['filter_id'].type = 'Integer'
query_parameters['filter_id'].optional = True
query_parameters['key'].type = 'String'
query_parameters['key'].optional = True
query_parameters['page'].type = 'Integer'
query_parameters['page'].optional = True
query_parameters['per_page'].type = 'Integer'
query_parameters['per_page'].optional = True
query_parameters['q'].type = 'String'
query_parameters['q'].optional = False
query_parameters['q'].api_name = 'q'
query_parameters['q'].name = 'query'
query_parameters['sd'].type = 'String'
query_parameters['sd'].optional = True
query_parameters['sd'].api_name = 'sd'
query_parameters['sd'].name = 'sort_direction'
query_parameters['sf'].type = 'String'
query_parameters['sf'].optional = True
query_parameters['sf'].api_name = 'sf'
query_parameters['sf'].name = 'sort_field'
query_parameters['url'] = Parameter('url', 'String', 'Link a deviantART page, a Tumblr post, or the image directly.')
query_parameters['distance'] = Parameter('distance', 'Float', 'Match distance (suggested values: between 0.2 and 0.5).', optional=True)

logger.debug(f'query_parameters: {query_parameters!r}')

assert all([p.type is not None for p in query_parameters.values()])



route_names = {}
route_names['/api/v1/json/comments/:comment_id'] = 'comment'
route_names['/api/v1/json/images/:image_id'] = 'image'
route_names['/api/v1/json/images/featured'] = 'featured_image'
route_names['/api/v1/json/tags/:tag_id'] = 'tag'
route_names['/api/v1/json/posts/:post_id'] = 'post'
route_names['/api/v1/json/profiles/:user_id'] = 'user'
route_names['/api/v1/json/filters/:filter_id'] = 'filter'
route_names['/api/v1/json/filters/system'] = 'system_filters'
route_names['/api/v1/json/filters/user'] = 'user_filters'
route_names['/api/v1/json/oembed'] = 'oembed'
route_names['/api/v1/json/search/comments'] = 'search_comments'
route_names['/api/v1/json/search/galleries'] = 'search_galleries'
route_names['/api/v1/json/search/posts'] = 'search_posts'
route_names['/api/v1/json/search/images'] = 'search_images'
route_names['/api/v1/json/search/tags'] = 'search_tags'
route_names['/api/v1/json/search/reverse'] = 'search_reverse'
route_names['/api/v1/json/forums'] = 'forums'
route_names['/api/v1/json/forums/:short_name'] = 'forum'
route_names['/api/v1/json/forums/:short_name/topics'] = 'forum_topics'
route_names['/api/v1/json/forums/:short_name/topics/:topic_slug'] = 'forum_topic'
route_names['/api/v1/json/forums/:short_name/topics/:topic_slug/posts'] = 'forum_posts'
route_names['/api/v1/json/forums/:short_name/topics/:topic_slug/posts/:post_id'] = 'forum_post'


routes = []

element = main.select_one('h2#routes')
table = element.find_next('table')
column_headers = []
for column in table.find_all('th'):
    column_headers.append(column.text)
# end if
logger.debug(f'column_headers: {column_headers!r}')
assert column_headers == ['Method', 'Path', 'Allowed Query Parameters', 'Description', 'Response Format', 'Example']
rows = table.find_all('tr')[1:]  # skip the <thead>'s <tr> (containing only <td>s anyway)
for row in rows:
    columns = row.find_all('td')
    path = columns[1].code.text
    name = route_names[path]
    path_python = re.sub(RE_URL_PRAMS, RE_URL_PRAMS_REPLACEMENT, path)
    path_params = []
    matches = re.finditer(RE_URL_PRAMS, path)
    for match in matches:
        param = match.groupdict()['param']
        url_p = Parameter(
            name=param,
            type="Integer" if param.endswith('_id') and param != 'tag_id' else "String",
            description=f'the variable {param} part of the url.'
        )
        path_params.append(url_p)
    # end for

    p = UrlPath(
        original=path,
        template=path_python,
        params=path_params,
    )
    logger.debug(p)

    # Using the Response Format (columns[4].code.contents) we'll get:
    #
    # >>>> {"comment":comment-response}  # columns[4].code.contents
    # >--> {'comment': Comment}          # response_format_schema
    # >--> {'comment': {}}               # response_format_mock
    #  '-> class_name = 'Comment'        # class_name
    #  '-> key = 'comment'               # key
    #  '-> is_list = False               # is_list
    #
    # or
    #
    # >>>> {"images":[image-response]}   # columns[4].code.contents
    # >--> {"images":[Image]}            # response_format_schema
    # >--> {"images":[{}]}               # response_format_mock
    #  '-> class_name = 'Image'          # class_name
    #  '-> key = 'images'                # key
    #  '-> is_list = True                # is_list
    response_format_schema = ''
    response_format_mock = ''
    class_name = None
    for tag in columns[4].code.contents:
        if isinstance(tag, NavigableString):
            response_format_schema += str(tag)
            response_format_mock += str(tag)
        elif tag.name == 'a' and tag.attrs.get('href', ''):
            assert class_name is None  # should still be unfilled, there should be only one type
            class_name = class_names[tag.attrs["href"]]
            response_format_schema += class_name
            response_format_mock += '{}'
        else:
            response_format_schema += tag.text
            response_format_mock += tag.text
        # end if
    # end for

    # Use the Mock object to get the type and key:
    logger.debug(f'schema: {response_format_schema!r}')
    logger.debug(f'mock: {response_format_mock!r}')
    type_mock = json.loads(response_format_mock)
    logger.debug(f'type_mock: {type_mock!r}')
    if type_mock != {}:  # e.g. only the Oembed
        assert isinstance(type_mock, dict)
        keys = list(type_mock.keys())
        logger.debug(f'type_mock keys: {keys!r}')
        has_total = False
        if "total" in keys:
            has_total = True
            keys = [k for k in keys if k != 'total']
        # end def
        assert len(keys) == 1
        keys = list(keys)
        key = keys[0]
        del keys
        value = type_mock[key]
        logger.debug(f'type_mock value: {value!r}')
        assert isinstance(value, dict) or isinstance(value, list)
        if isinstance(value, list):
            # is list of entities
            assert value == [{}]
            is_list = True
        else:
            assert value == {}
            is_list = False
        # end if
    else:
        # Ins
        key = None
        is_list = False
        has_total = False
    # end if

    # generate a python type out of it
    t = ResponseType(
        schema=response_format_schema,
        is_list=is_list,
        key=key,
        class_name=class_name,
        has_total=has_total,
    )

    # now apply it all
    r = Route(
        name=name,
        method=columns[0].code.text,
        path=p,
        allowed_query_parameters=[query_parameters[param.strip()] for param in columns[2].text.split(',') if param],
        description=parse_description(columns[3].contents),
        response_format=t,
        example_url=columns[5].a.attrs['href'],
    )
    routes.append(r)
# end def


with open(f'./output/{FILE}.py', 'w') as f:
    f.write('from models import *\n')
    f.write('\n')
    f.write('routes = [\n')
    for route in routes:
        f.write('\t' + repr(route) + ',\n')
    # end for
    f.write(']\n')
    f.write('classes = [\n')
    for clazz in classes:
        f.write('\t' + repr(clazz) + ',\n')
    # end for
    f.write(']\n')
# end for

print('gnerf')
