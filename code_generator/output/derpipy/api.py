#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'luckydonald'

from luckydonaldUtils.logger import logging
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

from typing import Union, List
from .models import *

# import either requests or httpx
# as internet
try:
    import requests as internet
except ImportError:
    try:
        import httpx as internet
    except ImportError:
        raise ImportError('Neither "requests" nor "httpx" could be found. Make sure either of them is installed.')
    # end try
# end try


class SyncBot(object):
    """
    Synchronous client for Derpibooru.org
    """
    _base_url = 'https://derpibooru.org'

    @staticmethod
    def _check_response(response: internet.Response) -> None:
        """
        Makes sure a server response looks valid,
        or raise the appropriate errors if not.

        :param response: A requests/httpx response.
        :type  response: requests.Response|httpx.Response
        """
        assert response.status_code == 200  # TODO
        assert response.headers['content-type'] == 'application/json; charset=utf-8'
    # end def

    
    def comment(
        self, 
        comment_id: int,
    ) -> Comment:
        """
        Fetches a **comment response** for the comment ID referenced by the `comment_id` URL parameter.

        
        :param comment_id: the variable comment_id part of the url.
        :type  comment_id: int
        """
        pass
    # end def comment
    
    def image(
        self, 
        image_id: int,
        filter_id: int,
        key: Union[str, None] = None,
    ) -> Image:
        """
        Fetches an **image response** for the image ID referenced by the `image_id` URL parameter.

        
        :param image_id: the variable image_id part of the url.
        :type  image_id: int
        :param filter_id: Assuming the user can access the filter ID given by the parameter, overrides the current filter for this request. This is primarily useful for unauthenticated API access.
        :type  filter_id: int
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def image
    
    def featured_images(
        self, 
    ) -> Image:
        """
        Fetches an **image response** for the for the current featured image.

        
        """
        pass
    # end def featured_images
    
    def tag(
        self, 
        tag_id: int,
    ) -> Tag:
        """
        Fetches a **tag response** for the **tag slug** given by the `tag_id` URL parameter. The tag's ID is **not** used.

        
        :param tag_id: the variable tag_id part of the url.
        :type  tag_id: int
        """
        pass
    # end def tag
    
    def post(
        self, 
        post_id: int,
    ) -> Post:
        """
        Fetches a **post response** for the post ID given by the `post_id` URL parameter.

        
        :param post_id: the variable post_id part of the url.
        :type  post_id: int
        """
        pass
    # end def post
    
    def user(
        self, 
        user_id: int,
    ) -> User:
        """
        Fetches a **profile response** for the user ID given by the `user_id` URL parameter.

        
        :param user_id: the variable user_id part of the url.
        :type  user_id: int
        """
        pass
    # end def user
    
    def filter(
        self, 
        filter_id: int,
        key: Union[str, None] = None,
    ) -> Filter:
        """
        Fetches a **filter response** for the filter ID given by the `filter_id` URL parameter.

        
        :param filter_id: the variable filter_id part of the url.
        :type  filter_id: int
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def filter
    
    def system_filters(
        self, 
        page: int,
    ) -> List[Filter]:
        """
        Fetches a list of **filter responses** that are flagged as being **system** filters (and thus usable by anyone).

        
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        """
        pass
    # end def system_filters
    
    def user_filters(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Filter]:
        """
        Fetches a list of **filter responses** that belong to the user given by **key**. If no **key** is given or it is invalid, will return a **403 Forbidden** error.

        
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def user_filters
    
    def oembed(
        self, 
        url: str,
    ) -> Oembed:
        """
        Fetches an **oEmbed response** for the given app link or CDN URL.

        
        :param url: Link a deviantART page, a Tumblr post, or the image directly.
        :type  url: str
        """
        pass
    # end def oembed
    
    def search_comments(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Comment]:
        """
        Executes the search given by the `q` query parameter, and returns **comment responses** sorted by descending creation time.

        
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def search_comments
    
    def search_galleries(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Gallery]:
        """
        Executes the search given by the `q` query parameter, and returns **gallery responses** sorted by descending creation time.

        
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def search_galleries
    
    def search_posts(
        self, 
        page: int,
        key: Union[str, None] = None,
    ) -> List[Post]:
        """
        Executes the search given by the `q` query parameter, and returns **post responses** sorted by descending creation time.

        
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def search_posts
    
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

        
        :param filter_id: Assuming the user can access the filter ID given by the parameter, overrides the current filter for this request. This is primarily useful for unauthenticated API access.
        :type  filter_id: int
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        :param per_page: Controls the number of results per page, up to a limit of 50, if the response is paginated. The default is 25.
        :type  per_page: int
        :param q: The current search query, if the request is a search request.
        :type  q: str
        :param sd: The current sort direction, if the request is a search request.
        :type  sd: str
        :param sf: The current sort field, if the request is a search request.
        :type  sf: str
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def search_images
    
    def search_tags(
        self, 
        page: int,
    ) -> List[Tag]:
        """
        Executes the search given by the `q` query parameter, and returns **tag responses** sorted by descending image count.

        
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        """
        pass
    # end def search_tags
    
    def search_reverse(
        self, 
        url: str,
        distance: float,
        key: Union[str, None] = None,
    ) -> List[Image]:
        """
        Returns **image responses** based on the results of reverse-searching the image given by the `url` query parameter.

        
        :param url: Link a deviantART page, a Tumblr post, or the image directly.
        :type  url: str
        :param distance: Match distance (suggested values: between 0.2 and 0.5).
        :type  distance: float
        :param key: An optional authentication token. If omitted, no user will be authenticated.

                    You can find your authentication token in your [account settings](https://derpibooru.org/registration/edit).
        :type  key: str|None
        """
        pass
    # end def search_reverse
    
    def forums(
        self, 
    ) -> Forum:
        """
        Fetches a list of **forum responses**.

        
        """
        pass
    # end def forums
    
    def forum(
        self, 
        short_name: str,
    ) -> Forum:
        """
        Fetches a **forum response** for the abbreviated name given by the `short_name` URL parameter.

        
        :param short_name: the variable short_name part of the url.
        :type  short_name: str
        """
        pass
    # end def forum
    
    def forum_topics(
        self, 
        short_name: str,
        page: int,
    ) -> Topic:
        """
        Fetches a list of **topic responses** for the abbreviated forum name given by the `short_name` URL parameter.

        
        :param short_name: the variable short_name part of the url.
        :type  short_name: str
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        """
        pass
    # end def forum_topics
    
    def forum_topic(
        self, 
        short_name: str,
        topic_slug: str,
    ) -> Topic:
        """
        Fetches a **topic response** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.

        
        :param short_name: the variable short_name part of the url.
        :type  short_name: str
        :param topic_slug: the variable topic_slug part of the url.
        :type  topic_slug: str
        """
        pass
    # end def forum_topic
    
    def forum_posts(
        self, 
        short_name: str,
        topic_slug: str,
        page: int,
    ) -> Post:
        """
        Fetches a list of **post responses** for the abbreviated forum name given by the `short_name` and topic given by `topic_slug` URL parameters.

        
        :param short_name: the variable short_name part of the url.
        :type  short_name: str
        :param topic_slug: the variable topic_slug part of the url.
        :type  topic_slug: str
        :param page: Controls the current page of the response, if the response is paginated. Empty values default to the first page.
        :type  page: int
        """
        pass
    # end def forum_posts
    
    def forum_post(
        self, 
        short_name: str,
        topic_slug: str,
        post_id: int,
    ) -> Post:
        """
        Fetches a **post response** for the abbreviated forum name given by the `short_name`, topic given by `topic_slug` and post given by `post_id` URL parameters.

        
        :param short_name: the variable short_name part of the url.
        :type  short_name: str
        :param topic_slug: the variable topic_slug part of the url.
        :type  topic_slug: str
        :param post_id: the variable post_id part of the url.
        :type  post_id: int
        """
        pass
    # end def forum_post
    
# end class