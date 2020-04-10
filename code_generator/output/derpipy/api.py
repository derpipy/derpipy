#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luckydonald'

logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

from typing import Union, List
from .models import *

class SyncBot(object):

    

    # Route(name='comment', method='GET', path=UrlPath(original='/api/v1/json/comments/:comment_id', template='/api/v1/json/comments/{comment_id}', params=[Parameter(name='comment_id', type='Integer', description='the variable comment_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **comment response** for the comment ID referenced by the `comment_id` URL parameter.', response_format=ResponseType(schema='{"comment":Comment}', is_list=False, key='comment', class_name='Comment'), example_url='/api/v1/json/comments/1000')

    def comment(
        self, 
        comment_id: int,
    ) -> Comment:
    """
    Fetches a **comment response** for the comment ID referenced by the `comment_id` URL parameter.
    """
        pass
    # end def comment

    

    # Route(name='image', method='GET', path=UrlPath(original='/api/v1/json/images/:image_id', template='/api/v1/json/images/{image_id}', params=[Parameter(name='image_id', type='Integer', description='the variable image_id part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='filter_id', type='Integer', description='Assuming the user can access the filter ID given by the parameter, overrides the current filter for this request. This is primarily useful for unauthenticated API access.', optional=False)], description='Fetches an **image response** for the image ID referenced by the `image_id` URL parameter.', response_format=ResponseType(schema='{"image":Image}', is_list=False, key='image', class_name='Image'), example_url='/api/v1/json/images/1')

    def image(
        self, 
        image_id: int,
        filter_id: int,
        key: Union[str, None] = None,
    ) -> Image:
    """
    Fetches an **image response** for the image ID referenced by the `image_id` URL parameter.
    """
        pass
    # end def image

    

    # Route(name='featured_images', method='GET', path=UrlPath(original='/api/v1/json/images/featured', template='/api/v1/json/images/featured', params=[]), allowed_query_parameters=[], description='Fetches an **image response** for the for the current featured image.', response_format=ResponseType(schema='{"image":Image}', is_list=False, key='image', class_name='Image'), example_url='/api/v1/json/images/featured')

    def featured_images(
        self, 
    ) -> Image:
    """
    Fetches an **image response** for the for the current featured image.
    """
        pass
    # end def featured_images

    

    # Route(name='tag', method='GET', path=UrlPath(original='/api/v1/json/tags/:tag_id', template='/api/v1/json/tags/{tag_id}', params=[Parameter(name='tag_id', type='Integer', description='the variable tag_id part of the url.', optional=False)]), allowed_query_parameters=[], description="Fetches a **tag response** for the **tag slug** given by the `tag_id` URL parameter. The tag's ID is **not** used.", response_format=ResponseType(schema='{"tag":Tag}', is_list=False, key='tag', class_name='Tag'), example_url='/api/v1/json/tags/artist-colon-atryl')

    def tag(
        self, 
        tag_id: int,
    ) -> Tag:
    """
    Fetches a **tag response** for the **tag slug** given by the `tag_id` URL parameter. The tag's ID is **not** used.
    """
        pass
    # end def tag

    

    # Route(name='post', method='GET', path=UrlPath(original='/api/v1/json/posts/:post_id', template='/api/v1/json/posts/{post_id}', params=[Parameter(name='post_id', type='Integer', description='the variable post_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **post response** for the post ID given by the `post_id` URL parameter.', response_format=ResponseType(schema='{"post":Post}', is_list=False, key='post', class_name='Post'), example_url='/api/v1/json/posts/2730144')

    def post(
        self, 
        post_id: int,
    ) -> Post:
    """
    Fetches a **post response** for the post ID given by the `post_id` URL parameter.
    """
        pass
    # end def post

    

    # Route(name='user', method='GET', path=UrlPath(original='/api/v1/json/profiles/:user_id', template='/api/v1/json/profiles/{user_id}', params=[Parameter(name='user_id', type='Integer', description='the variable user_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **profile response** for the user ID given by the `user_id` URL parameter.', response_format=ResponseType(schema='{"user":User}', is_list=False, key='user', class_name='User'), example_url='/api/v1/json/profiles/216494')

    def user(
        self, 
        user_id: int,
    ) -> User:
    """
    Fetches a **profile response** for the user ID given by the `user_id` URL parameter.
    """
        pass
    # end def user

    

    # Route(name='filter', method='GET', path=UrlPath(original='/api/v1/json/filters/:filter_id', template='/api/v1/json/filters/{filter_id}', params=[Parameter(name='filter_id', type='Integer', description='the variable filter_id part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True)], description='Fetches a **filter response** for the filter ID given by the `filter_id` URL parameter.', response_format=ResponseType(schema='{"filter":Filter}', is_list=False, key='filter', class_name='Filter'), example_url='/api/v1/json/filters/56027')

    def filter(
        self, 
        filter_id: int,
        key: Union[str, None] = None,
    ) -> Filter:
    """
    Fetches a **filter response** for the filter ID given by the `filter_id` URL parameter.
    """
        pass
    # end def filter

    

    # Route(name='system_filters', method='GET', path=UrlPath(original='/api/v1/json/filters/system', template='/api/v1/json/filters/system', params=[]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **filter responses** that are flagged as being **system** filters (and thus usable by anyone).', response_format=ResponseType(schema='{"filters":[Filter]}', is_list=True, key='filters', class_name='Filter'), example_url='/api/v1/json/filters/system')

    def system_filters(
        self, 
        page: int,
    ) -> List[Filter]:
    """
    Fetches a list of **filter responses** that are flagged as being **system** filters (and thus usable by anyone).
    """
        pass
    # end def system_filters

    

    # Route(name='user_filters', method='GET', path=UrlPath(original='/api/v1/json/filters/user', template='/api/v1/json/filters/user', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **filter responses** that belong to the user given by **key**. If no **key** is given or it is invalid, will return a **403 Forbidden** error.', response_format=ResponseType(schema='{"filters":[Filter]}', is_list=True, key='filters', class_name='Filter'), example_url='/api/v1/json/filters/user')

    def user_filters(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Filter]:
    """
    Fetches a list of **filter responses** that belong to the user given by **key**. If no **key** is given or it is invalid, will return a **403 Forbidden** error.
    """
        pass
    # end def user_filters

    

    # Route(name='oembed', method='GET', path=UrlPath(original='/api/v1/json/oembed', template='/api/v1/json/oembed', params=[]), allowed_query_parameters=[Parameter(name='version', type='String', description='Link a deviantART page, a Tumblr post, or the image directly.', optional=False)], description='Fetches an **oEmbed response** for the given app link or CDN URL.', response_format=ResponseType(schema='Oembed', is_list=False, key=None, class_name='Oembed'), example_url='/api/v1/json/oembed?url=https://derpicdn.net/img/2012/1/2/3/full.png')

    def oembed(
        self, 
        version: str,
    ) -> Oembed:
    """
    Fetches an **oEmbed response** for the given app link or CDN URL.
    """
        pass
    # end def oembed

    

    # Route(name='search_comments', method='GET', path=UrlPath(original='/api/v1/json/search/comments', template='/api/v1/json/search/comments', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **comment responses** sorted by descending creation time.', response_format=ResponseType(schema='{"comments":[Comment]}', is_list=True, key='comments', class_name='Comment'), example_url='/api/v1/json/search/comments?q=image_id:1000000')

    def search_comments(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Comment]:
    """
    Executes the search given by the `q` query parameter, and returns **comment responses** sorted by descending creation time.
    """
        pass
    # end def search_comments

    

    # Route(name='search_galleries', method='GET', path=UrlPath(original='/api/v1/json/search/galleries', template='/api/v1/json/search/galleries', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **gallery responses** sorted by descending creation time.', response_format=ResponseType(schema='{"galleries":[Gallery]}', is_list=True, key='galleries', class_name='Gallery'), example_url='/api/v1/json/search/galleries?q=title:mean*')

    def search_galleries(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Gallery]:
    """
    Executes the search given by the `q` query parameter, and returns **gallery responses** sorted by descending creation time.
    """
        pass
    # end def search_galleries

    

    # Route(name='search_posts', method='GET', path=UrlPath(original='/api/v1/json/search/posts', template='/api/v1/json/search/posts', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **post responses** sorted by descending creation time.', response_format=ResponseType(schema='{"posts":[Post]}', is_list=True, key='posts', class_name='Post'), example_url='/api/v1/json/search/posts?q=subject:time wasting thread')

    def search_posts(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Post]:
    """
    Executes the search given by the `q` query parameter, and returns **post responses** sorted by descending creation time.
    """
        pass
    # end def search_posts

    

    # Route(name='search_images', method='GET', path=UrlPath(original='/api/v1/json/search/images', template='/api/v1/json/search/images', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='filter_id', type='Integer', description='Assuming the user can access the filter ID given by the parameter, overrides the current filter for this request. This is primarily useful for unauthenticated API access.', optional=False), Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False), Parameter(name='per_page', type='Integer', description='Controls the number of results per page, up to a limit of 50, if the response is paginated. The default is 25.', optional=False), Parameter(name='q', type='String', description='The current search query, if the request is a search request.', optional=False), Parameter(name='sd', type='String', description='The current sort direction, if the request is a search request.', optional=False), Parameter(name='sf', type='String', description='The current sort field, if the request is a search request.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **image responses**.', response_format=ResponseType(schema='{"images":[Image]}', is_list=True, key='images', class_name='Image'), example_url='/api/v1/json/search/images?q=safe')

    def search_images(
        self, 
        filter_id: int,
        page: int,
        per_page: int,
        q: str,
        sd: str,
        sf: str,
        key: Union[str, None] = None,
    ) -> List[Image]:
    """
    Executes the search given by the `q` query parameter, and returns **image responses**.
    """
        pass
    # end def search_images

    

    # Route(name='search_tags', method='GET', path=UrlPath(original='/api/v1/json/search/tags', template='/api/v1/json/search/tags', params=[]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Executes the search given by the `q` query parameter, and returns **tag responses** sorted by descending image count.', response_format=ResponseType(schema='{"tags":[Tag]}', is_list=True, key='tags', class_name='Tag'), example_url='/api/v1/json/search/tags?q=analyzed_name:wing')

    def search_tags(
        self, 
        page: int,
    ) -> List[Tag]:
    """
    Executes the search given by the `q` query parameter, and returns **tag responses** sorted by descending image count.
    """
        pass
    # end def search_tags

    

    # Route(name='search_reverse', method='POST', path=UrlPath(original='/api/v1/json/search/reverse', template='/api/v1/json/search/reverse', params=[]), allowed_query_parameters=[Parameter(name='key', type='String', description='An optional authentication token. If omitted, no user will be authenticated.\n\nYou can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).', optional=True), Parameter(name='version', type='String', description='Link a deviantART page, a Tumblr post, or the image directly.', optional=False), Parameter(name='version', type='Float', description='Match distance (suggested values: between 0.2 and 0.5).', optional=False)], description='Returns **image responses** based on the results of reverse-searching the image given by the `url` query parameter.', response_format=ResponseType(schema='{"images":[Image]}', is_list=True, key='images', class_name='Image'), example_url='/api/v1/json/search/reverse?url=https://derpicdn.net/img/2019/12/24/2228439/full.jpg')

    def search_reverse(
        self, 
        version: str,
        version: float,
        key: Union[str, None] = None,
    ) -> List[Image]:
    """
    Returns **image responses** based on the results of reverse-searching the image given by the `url` query parameter.
    """
        pass
    # end def search_reverse

    

    # Route(name='forums', method='GET', path=UrlPath(original='/api/v1/json/forums', template='/api/v1/json/forums', params=[]), allowed_query_parameters=[], description='Fetches a list of **forum responses**.', response_format=ResponseType(schema='{"forums":Forum}', is_list=False, key='forums', class_name='Forum'), example_url='/api/v1/json/forums')

    def forums(
        self, 
    ) -> Forum:
    """
    Fetches a list of **forum responses**.
    """
        pass
    # end def forums

    

    # Route(name='forum', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name', template='/api/v1/json/forums/{short_name}', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **forum response** for the abbreviated name given by the `short_name` URL parameter.', response_format=ResponseType(schema='{"forum":Forum}', is_list=False, key='forum', class_name='Forum'), example_url='/api/v1/json/forums/dis')

    def forum(
        self, 
        short_name: str,
    ) -> Forum:
    """
    Fetches a **forum response** for the abbreviated name given by the `short_name` URL parameter.
    """
        pass
    # end def forum

    

    # Route(name='forum_topics', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics', template='/api/v1/json/forums/{short_name}/topics', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **topic responses** for the abbreviated forum name given by the `short_name` URL parameter.', response_format=ResponseType(schema='{"topics":Topic}', is_list=False, key='topics', class_name='Topic'), example_url='/api/v1/json/forums/dis/topics')

    def forum_topics(
        self, 
        short_name: str,
        page: int,
    ) -> Topic:
    """
    Fetches a list of **topic responses** for the abbreviated forum name given by the `short_name` URL parameter.
    """
        pass
    # end def forum_topics

    

    # Route(name='forum_topic', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics/:topic_slug', template='/api/v1/json/forums/{short_name}/topics/{topic_slug}', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False), Parameter(name='topic_slug', type='String', description='the variable topic_slug part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **topic response** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.', response_format=ResponseType(schema='{"topic":Topic}', is_list=False, key='topic', class_name='Topic'), example_url='/api/v1/json/forums/dis/topics/ask-the-mods-anything')

    def forum_topic(
        self, 
        short_name: str,
        topic_slug: str,
    ) -> Topic:
    """
    Fetches a **topic response** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.
    """
        pass
    # end def forum_topic

    

    # Route(name='forum_posts', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics/:topic_slug/posts', template='/api/v1/json/forums/{short_name}/topics/{topic_slug}/posts', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False), Parameter(name='topic_slug', type='String', description='the variable topic_slug part of the url.', optional=False)]), allowed_query_parameters=[Parameter(name='page', type='Integer', description='Controls the current page of the response, if the response is paginated. Empty values default to the first page.', optional=False)], description='Fetches a list of **post responses** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.', response_format=ResponseType(schema='{"posts":Post}', is_list=False, key='posts', class_name='Post'), example_url='/api/v1/json/forums/dis/topics/ask-the-mods-anything/posts')

    def forum_posts(
        self, 
        short_name: str,
        topic_slug: str,
        page: int,
    ) -> Post:
    """
    Fetches a list of **post responses** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.
    """
        pass
    # end def forum_posts

    

    # Route(name='forum_post', method='GET', path=UrlPath(original='/api/v1/json/forums/:short_name/topics/:topic_slug/posts/:post_id', template='/api/v1/json/forums/{short_name}/topics/{topic_slug}/posts/{post_id}', params=[Parameter(name='short_name', type='String', description='the variable short_name part of the url.', optional=False), Parameter(name='topic_slug', type='String', description='the variable topic_slug part of the url.', optional=False), Parameter(name='post_id', type='Integer', description='the variable post_id part of the url.', optional=False)]), allowed_query_parameters=[], description='Fetches a **post response** for the abbreviated forum name given by the `short_name`, topic given by `topic_slug` and post given by `post_id` URL parameters.', response_format=ResponseType(schema='{"post":Post}', is_list=False, key='post', class_name='Post'), example_url='/api/v1/json/forums/dis/topics/ask-the-mods-anything/posts/2761095')

    def forum_post(
        self, 
        short_name: str,
        topic_slug: str,
        post_id: int,
    ) -> Post:
    """
    Fetches a **post response** for the abbreviated forum name given by the `short_name`, topic given by `topic_slug` and post given by `post_id` URL parameters.
    """
        pass
    # end def forum_post
