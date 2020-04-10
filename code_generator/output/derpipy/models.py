#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

__author__ = 'luckydonald'
__all__ = ['DerpiModel', 'Intensities','Representations','Image','Comment','Forum','Topic','Post','Tag','User','Filter','Links','Awards','Gallery','Oembed'

from luckydonaldUtils.logger import logging
logger = logging.getLogger(__name__)
if __name__ == '__main__':
    logging.add_colored_handler(level=logging.DEBUG)
# end if

from datetime import datetime
from typing import Union, List





class DerpiModel(object):
    """ Base class for all models """
    pass
# end class DerpiModel




class Intensities(DerpiModel):
    """
    A parsed Intensities response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param ne: Northeast intensity. Whatever that means…
    :type  ne: float
    
    :param nw: Northwest intensity. Whatever that means…
    :type  nw: float
    
    :param se: Southeast intensity. Whatever that means…
    :type  se: float
    
    :param sw: Southwest intensity. Whatever that means…
    :type  sw: float
    
    """

    
    """ Northeast intensity. Whatever that means… """
    ne: float
    
    """ Northwest intensity. Whatever that means… """
    nw: float
    
    """ Southeast intensity. Whatever that means… """
    se: float
    
    """ Southwest intensity. Whatever that means… """
    sw: float
    

    def __init__(
        self, 
        ne: float,
        nw: float,
        se: float,
        sw: float,
    ):
        """
        A parsed Intensities response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param ne: Northeast intensity. Whatever that means…
        :type  ne: float
        
        :param nw: Northwest intensity. Whatever that means…
        :type  nw: float
        
        :param se: Southeast intensity. Whatever that means…
        :type  se: float
        
        :param sw: Southwest intensity. Whatever that means…
        :type  sw: float
        
        """
        pass
    # end def __init__
# end class



class Representations(DerpiModel):
    """
    A parsed Representations response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param full: A mapping of the 'full' representation names to their respective URLs.
    :type  full: str
    
    :param large: A mapping of the 'large' representation names to their respective URLs.
    :type  large: str
    
    :param medium: A mapping of the 'medium' representation names to their respective URLs.
    :type  medium: str
    
    :param small: A mapping of the 'small' representation names to their respective URLs.
    :type  small: str
    
    :param tall: A mapping of the 'tall' representation names to their respective URLs.
    :type  tall: str
    
    :param thumb: A mapping of the 'thumb' representation names to their respective URLs.
    :type  thumb: str
    
    :param thumb_small: A mapping of the 'thumb_small' representation names to their respective URLs.
    :type  thumb_small: str
    
    :param thumb_tiny: A mapping of the 'thumb_tiny' representation names to their respective URLs.
    :type  thumb_tiny: str
    
    """

    
    """ A mapping of the 'full' representation names to their respective URLs. """
    full: str
    
    """ A mapping of the 'large' representation names to their respective URLs. """
    large: str
    
    """ A mapping of the 'medium' representation names to their respective URLs. """
    medium: str
    
    """ A mapping of the 'small' representation names to their respective URLs. """
    small: str
    
    """ A mapping of the 'tall' representation names to their respective URLs. """
    tall: str
    
    """ A mapping of the 'thumb' representation names to their respective URLs. """
    thumb: str
    
    """ A mapping of the 'thumb_small' representation names to their respective URLs. """
    thumb_small: str
    
    """ A mapping of the 'thumb_tiny' representation names to their respective URLs. """
    thumb_tiny: str
    

    def __init__(
        self, 
        full: str,
        large: str,
        medium: str,
        small: str,
        tall: str,
        thumb: str,
        thumb_small: str,
        thumb_tiny: str,
    ):
        """
        A parsed Representations response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param full: A mapping of the 'full' representation names to their respective URLs.
        :type  full: str
        
        :param large: A mapping of the 'large' representation names to their respective URLs.
        :type  large: str
        
        :param medium: A mapping of the 'medium' representation names to their respective URLs.
        :type  medium: str
        
        :param small: A mapping of the 'small' representation names to their respective URLs.
        :type  small: str
        
        :param tall: A mapping of the 'tall' representation names to their respective URLs.
        :type  tall: str
        
        :param thumb: A mapping of the 'thumb' representation names to their respective URLs.
        :type  thumb: str
        
        :param thumb_small: A mapping of the 'thumb_small' representation names to their respective URLs.
        :type  thumb_small: str
        
        :param thumb_tiny: A mapping of the 'thumb_tiny' representation names to their respective URLs.
        :type  thumb_tiny: str
        
        """
        pass
    # end def __init__
# end class



class Image(DerpiModel):
    """
    A parsed Image response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param aspect_ratio: The image's width divided by its height.
    :type  aspect_ratio: float
    
    :param comment_count: The number of comments made on the image.
    :type  comment_count: int
    
    :param created_at: The creation time, in UTC, of the image.
    :type  created_at: datetime
    
    :param deletion_reason: The hide reason for the image, or null if none provided. This will only have a value on images which are deleted for a rule violation.
    :type  deletion_reason: str
    
    :param description: The image's description.
    :type  description: str
    
    :param downvotes: The number of downvotes the image has.
    :type  downvotes: int
    
    :param duplicate_of: The ID of the target image, or null if none provided. This will only have a value on images which are merged into another image.
    :type  duplicate_of: int
    
    :param faves: The number of faves the image has.
    :type  faves: int
    
    :param first_seen_at: The time, in UTC, this image was first seen (before any duplicate merging).
    :type  first_seen_at: datetime
    
    :param format: The file extension of this image. One of "gif", "jpg", "jpeg", "png", "svg", "webm".
    :type  format: str
    
    :param height: The image's height, in pixels.
    :type  height: int
    
    :param hidden_from_users: Whether this image is hidden. An image is hidden if it is merged or deleted for a rule violation.
    :type  hidden_from_users: bool
    
    :param id: The image's ID.
    :type  id: int
    
    :param intensities: Optional object of internal image intensity data for deduplication purposes. May be null if intensities have not yet been generated.
    :type  intensities: Intensities
    
    :param mime_type: The MIME type of this image. One of "image/gif", "image/jpeg", "image/png", "image/svg+xml", "video/webm".
    :type  mime_type: str
    
    :param name: The filename that this image was uploaded with.
    :type  name: str
    
    :param orig_sha512_hash: The SHA512 hash of this image as it was originally uploaded.
    :type  orig_sha512_hash: str
    
    :param processed: Whether the image has finished optimization.
    :type  processed: bool
    
    :param representations: A mapping of representation names to their respective URLs. Contains the keys "full", "large", "medium", "small", "tall", "thumb", "thumb_small", "thumb_tiny".
    :type  representations: Representations
    
    :param score: The image's number of upvotes minus the image's number of downvotes.
    :type  score: int
    
    :param sha512_hash: The SHA512 hash of this image after it has been processed.
    :type  sha512_hash: str
    
    :param source_url: The current source URL of the image.
    :type  source_url: str
    
    :param spoilered: Whether this image is hit by the current filter.
    :type  spoilered: bool
    
    :param tag_count: The number of tags present on this image.
    :type  tag_count: int
    
    :param tag_ids: A list of tag IDs this image contains.
    :type  tag_ids: list
    
    :param tags: A list of tag names this image contains.
    :type  tags: list
    
    :param thumbnails_generated: Whether this image has finished thumbnail generation. Do not attempt to load images from view_url or representations if this is false.
    :type  thumbnails_generated: bool
    
    :param updated_at: The time, in UTC, the image was last updated.
    :type  updated_at: datetime
    
    :param uploader: The image's uploader.
    :type  uploader: str
    
    :param uploader_id: The ID of the image's uploader.
    :type  uploader_id: int
    
    :param upvotes: The image's number of upvotes.
    :type  upvotes: int
    
    :param view_url: The image's view URL, including tags.
    :type  view_url: str
    
    :param width: The image's width, in pixels.
    :type  width: int
    
    :param wilson_score: The lower bound of the Wilson score interval for the image, based on its upvotes and downvotes, given a z-score corresponding to a confidence of 99.5%.
    :type  wilson_score: float
    
    """

    
    """ The image's width divided by its height. """
    aspect_ratio: float
    
    """ The number of comments made on the image. """
    comment_count: int
    
    """ The creation time, in UTC, of the image. """
    created_at: datetime
    
    """ The hide reason for the image, or null if none provided. This will only have a value on images which are deleted for a rule violation. """
    deletion_reason: str
    
    """ The image's description. """
    description: str
    
    """ The number of downvotes the image has. """
    downvotes: int
    
    """ The ID of the target image, or null if none provided. This will only have a value on images which are merged into another image. """
    duplicate_of: int
    
    """ The number of faves the image has. """
    faves: int
    
    """ The time, in UTC, this image was first seen (before any duplicate merging). """
    first_seen_at: datetime
    
    """ The file extension of this image. One of "gif", "jpg", "jpeg", "png", "svg", "webm". """
    format: str
    
    """ The image's height, in pixels. """
    height: int
    
    """ Whether this image is hidden. An image is hidden if it is merged or deleted for a rule violation. """
    hidden_from_users: bool
    
    """ The image's ID. """
    id: int
    
    """ Optional object of internal image intensity data for deduplication purposes. May be null if intensities have not yet been generated. """
    intensities: Intensities
    
    """ The MIME type of this image. One of "image/gif", "image/jpeg", "image/png", "image/svg+xml", "video/webm". """
    mime_type: str
    
    """ The filename that this image was uploaded with. """
    name: str
    
    """ The SHA512 hash of this image as it was originally uploaded. """
    orig_sha512_hash: str
    
    """ Whether the image has finished optimization. """
    processed: bool
    
    """ A mapping of representation names to their respective URLs. Contains the keys "full", "large", "medium", "small", "tall", "thumb", "thumb_small", "thumb_tiny". """
    representations: Representations
    
    """ The image's number of upvotes minus the image's number of downvotes. """
    score: int
    
    """ The SHA512 hash of this image after it has been processed. """
    sha512_hash: str
    
    """ The current source URL of the image. """
    source_url: str
    
    """ Whether this image is hit by the current filter. """
    spoilered: bool
    
    """ The number of tags present on this image. """
    tag_count: int
    
    """ A list of tag IDs this image contains. """
    tag_ids: list
    
    """ A list of tag names this image contains. """
    tags: list
    
    """ Whether this image has finished thumbnail generation. Do not attempt to load images from view_url or representations if this is false. """
    thumbnails_generated: bool
    
    """ The time, in UTC, the image was last updated. """
    updated_at: datetime
    
    """ The image's uploader. """
    uploader: str
    
    """ The ID of the image's uploader. """
    uploader_id: int
    
    """ The image's number of upvotes. """
    upvotes: int
    
    """ The image's view URL, including tags. """
    view_url: str
    
    """ The image's width, in pixels. """
    width: int
    
    """ The lower bound of the Wilson score interval for the image, based on its upvotes and downvotes, given a z-score corresponding to a confidence of 99.5%. """
    wilson_score: float
    

    def __init__(
        self, 
        aspect_ratio: float,
        comment_count: int,
        created_at: datetime,
        deletion_reason: str,
        description: str,
        downvotes: int,
        duplicate_of: int,
        faves: int,
        first_seen_at: datetime,
        format: str,
        height: int,
        hidden_from_users: bool,
        id: int,
        intensities: Intensities,
        mime_type: str,
        name: str,
        orig_sha512_hash: str,
        processed: bool,
        representations: Representations,
        score: int,
        sha512_hash: str,
        source_url: str,
        spoilered: bool,
        tag_count: int,
        tag_ids: list,
        tags: list,
        thumbnails_generated: bool,
        updated_at: datetime,
        uploader: str,
        uploader_id: int,
        upvotes: int,
        view_url: str,
        width: int,
        wilson_score: float,
    ):
        """
        A parsed Image response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param aspect_ratio: The image's width divided by its height.
        :type  aspect_ratio: float
        
        :param comment_count: The number of comments made on the image.
        :type  comment_count: int
        
        :param created_at: The creation time, in UTC, of the image.
        :type  created_at: datetime
        
        :param deletion_reason: The hide reason for the image, or null if none provided. This will only have a value on images which are deleted for a rule violation.
        :type  deletion_reason: str
        
        :param description: The image's description.
        :type  description: str
        
        :param downvotes: The number of downvotes the image has.
        :type  downvotes: int
        
        :param duplicate_of: The ID of the target image, or null if none provided. This will only have a value on images which are merged into another image.
        :type  duplicate_of: int
        
        :param faves: The number of faves the image has.
        :type  faves: int
        
        :param first_seen_at: The time, in UTC, this image was first seen (before any duplicate merging).
        :type  first_seen_at: datetime
        
        :param format: The file extension of this image. One of "gif", "jpg", "jpeg", "png", "svg", "webm".
        :type  format: str
        
        :param height: The image's height, in pixels.
        :type  height: int
        
        :param hidden_from_users: Whether this image is hidden. An image is hidden if it is merged or deleted for a rule violation.
        :type  hidden_from_users: bool
        
        :param id: The image's ID.
        :type  id: int
        
        :param intensities: Optional object of internal image intensity data for deduplication purposes. May be null if intensities have not yet been generated.
        :type  intensities: Intensities
        
        :param mime_type: The MIME type of this image. One of "image/gif", "image/jpeg", "image/png", "image/svg+xml", "video/webm".
        :type  mime_type: str
        
        :param name: The filename that this image was uploaded with.
        :type  name: str
        
        :param orig_sha512_hash: The SHA512 hash of this image as it was originally uploaded.
        :type  orig_sha512_hash: str
        
        :param processed: Whether the image has finished optimization.
        :type  processed: bool
        
        :param representations: A mapping of representation names to their respective URLs. Contains the keys "full", "large", "medium", "small", "tall", "thumb", "thumb_small", "thumb_tiny".
        :type  representations: Representations
        
        :param score: The image's number of upvotes minus the image's number of downvotes.
        :type  score: int
        
        :param sha512_hash: The SHA512 hash of this image after it has been processed.
        :type  sha512_hash: str
        
        :param source_url: The current source URL of the image.
        :type  source_url: str
        
        :param spoilered: Whether this image is hit by the current filter.
        :type  spoilered: bool
        
        :param tag_count: The number of tags present on this image.
        :type  tag_count: int
        
        :param tag_ids: A list of tag IDs this image contains.
        :type  tag_ids: list
        
        :param tags: A list of tag names this image contains.
        :type  tags: list
        
        :param thumbnails_generated: Whether this image has finished thumbnail generation. Do not attempt to load images from view_url or representations if this is false.
        :type  thumbnails_generated: bool
        
        :param updated_at: The time, in UTC, the image was last updated.
        :type  updated_at: datetime
        
        :param uploader: The image's uploader.
        :type  uploader: str
        
        :param uploader_id: The ID of the image's uploader.
        :type  uploader_id: int
        
        :param upvotes: The image's number of upvotes.
        :type  upvotes: int
        
        :param view_url: The image's view URL, including tags.
        :type  view_url: str
        
        :param width: The image's width, in pixels.
        :type  width: int
        
        :param wilson_score: The lower bound of the Wilson score interval for the image, based on its upvotes and downvotes, given a z-score corresponding to a confidence of 99.5%.
        :type  wilson_score: float
        
        """
        pass
    # end def __init__
# end class



class Comment(DerpiModel):
    """
    A parsed Comment response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param author: The comment's author.
    :type  author: str
    
    :param body: The comment text.
    :type  body: str
    
    :param id: The comment's ID.
    :type  id: int
    
    :param image_id: The ID of the image the comment belongs to.
    :type  image_id: int
    
    :param user_id: The ID of the user the comment belongs to, if any.
    :type  user_id: int
    
    """

    
    """ The comment's author. """
    author: str
    
    """ The comment text. """
    body: str
    
    """ The comment's ID. """
    id: int
    
    """ The ID of the image the comment belongs to. """
    image_id: int
    
    """ The ID of the user the comment belongs to, if any. """
    user_id: int
    

    def __init__(
        self, 
        author: str,
        body: str,
        id: int,
        image_id: int,
        user_id: int,
    ):
        """
        A parsed Comment response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param author: The comment's author.
        :type  author: str
        
        :param body: The comment text.
        :type  body: str
        
        :param id: The comment's ID.
        :type  id: int
        
        :param image_id: The ID of the image the comment belongs to.
        :type  image_id: int
        
        :param user_id: The ID of the user the comment belongs to, if any.
        :type  user_id: int
        
        """
        pass
    # end def __init__
# end class



class Forum(DerpiModel):
    """
    A parsed Forum response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param name: The forum's name.
    :type  name: str
    
    :param short_name: The forum's short name (used to identify it).
    :type  short_name: str
    
    :param description: The forum's description.
    :type  description: str
    
    :param topic_count: The amount of topics in the forum.
    :type  topic_count: int
    
    :param post_count: The amount of posts in the forum.
    :type  post_count: int
    
    """

    
    """ The forum's name. """
    name: str
    
    """ The forum's short name (used to identify it). """
    short_name: str
    
    """ The forum's description. """
    description: str
    
    """ The amount of topics in the forum. """
    topic_count: int
    
    """ The amount of posts in the forum. """
    post_count: int
    

    def __init__(
        self, 
        name: str,
        short_name: str,
        description: str,
        topic_count: int,
        post_count: int,
    ):
        """
        A parsed Forum response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param name: The forum's name.
        :type  name: str
        
        :param short_name: The forum's short name (used to identify it).
        :type  short_name: str
        
        :param description: The forum's description.
        :type  description: str
        
        :param topic_count: The amount of topics in the forum.
        :type  topic_count: int
        
        :param post_count: The amount of posts in the forum.
        :type  post_count: int
        
        """
        pass
    # end def __init__
# end class



class Topic(DerpiModel):
    """
    A parsed Topic response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param slug: The topic's slug (used to identify it).
    :type  slug: str
    
    :param title: The topic's title.
    :type  title: str
    
    :param post_count: The amount of posts in the topic.
    :type  post_count: int
    
    :param view_count: The amount of views the topic has received.
    :type  view_count: int
    
    :param sticky: Whether the topic is sticky.
    :type  sticky: bool
    
    :param last_replied_to_at: The time, in UTC, when the last reply was made.
    :type  last_replied_to_at: datetime
    
    :param locked: Whether the topic is locked.
    :type  locked: bool
    
    :param user_id: The ID of the user who made the topic. Null if posted anonymously.
    :type  user_id: int
    
    :param author: The name of the user who made the topic.
    :type  author: str
    
    """

    
    """ The topic's slug (used to identify it). """
    slug: str
    
    """ The topic's title. """
    title: str
    
    """ The amount of posts in the topic. """
    post_count: int
    
    """ The amount of views the topic has received. """
    view_count: int
    
    """ Whether the topic is sticky. """
    sticky: bool
    
    """ The time, in UTC, when the last reply was made. """
    last_replied_to_at: datetime
    
    """ Whether the topic is locked. """
    locked: bool
    
    """ The ID of the user who made the topic. Null if posted anonymously. """
    user_id: int
    
    """ The name of the user who made the topic. """
    author: str
    

    def __init__(
        self, 
        slug: str,
        title: str,
        post_count: int,
        view_count: int,
        sticky: bool,
        last_replied_to_at: datetime,
        locked: bool,
        user_id: int,
        author: str,
    ):
        """
        A parsed Topic response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param slug: The topic's slug (used to identify it).
        :type  slug: str
        
        :param title: The topic's title.
        :type  title: str
        
        :param post_count: The amount of posts in the topic.
        :type  post_count: int
        
        :param view_count: The amount of views the topic has received.
        :type  view_count: int
        
        :param sticky: Whether the topic is sticky.
        :type  sticky: bool
        
        :param last_replied_to_at: The time, in UTC, when the last reply was made.
        :type  last_replied_to_at: datetime
        
        :param locked: Whether the topic is locked.
        :type  locked: bool
        
        :param user_id: The ID of the user who made the topic. Null if posted anonymously.
        :type  user_id: int
        
        :param author: The name of the user who made the topic.
        :type  author: str
        
        """
        pass
    # end def __init__
# end class



class Post(DerpiModel):
    """
    A parsed Post response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param author: The post's author.
    :type  author: str
    
    :param body: The post text.
    :type  body: str
    
    :param id: The post's ID (used to identify it).
    :type  id: int
    
    :param user_id: The ID of the user the comment belongs to, if any.
    :type  user_id: int
    
    """

    
    """ The post's author. """
    author: str
    
    """ The post text. """
    body: str
    
    """ The post's ID (used to identify it). """
    id: int
    
    """ The ID of the user the comment belongs to, if any. """
    user_id: int
    

    def __init__(
        self, 
        author: str,
        body: str,
        id: int,
        user_id: int,
    ):
        """
        A parsed Post response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param author: The post's author.
        :type  author: str
        
        :param body: The post text.
        :type  body: str
        
        :param id: The post's ID (used to identify it).
        :type  id: int
        
        :param user_id: The ID of the user the comment belongs to, if any.
        :type  user_id: int
        
        """
        pass
    # end def __init__
# end class



class Tag(DerpiModel):
    """
    A parsed Tag response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param aliased_tag: The slug of the tag this tag is aliased to, if any.
    :type  aliased_tag: str
    
    :param aliases: The slugs of the tags aliased to this tag.
    :type  aliases: list
    
    :param category: The category class of this tag. One of "character", "content-fanmade", "content-official", "error", "oc", "origin", "rating", "species", "spoiler".
    :type  category: str
    
    :param description: The long description for the tag.
    :type  description: str
    
    :param dnp_entries: An array of objects containing DNP entries claimed on the tag.
    :type  dnp_entries: list
    
    :param id: The tag's ID.
    :type  id: int
    
    :param images: The image count of the tag.
    :type  images: int
    
    :param implied_by_tags: The slugs of the tags this tag is implied by.
    :type  implied_by_tags: list
    
    :param implied_tags: The slugs of the tags this tag implies.
    :type  implied_tags: list
    
    :param name: The name of the tag.
    :type  name: str
    
    :param name_in_namespace: The name of the tag in its namespace.
    :type  name_in_namespace: str
    
    :param namespace: The namespace of the tag.
    :type  namespace: str
    
    :param short_description: The short description for the tag.
    :type  short_description: str
    
    :param slug: The slug for the tag.
    :type  slug: str
    
    :param spoiler_image: The spoiler image URL for the tag.
    :type  spoiler_image: str
    
    """

    
    """ The slug of the tag this tag is aliased to, if any. """
    aliased_tag: str
    
    """ The slugs of the tags aliased to this tag. """
    aliases: list
    
    """ The category class of this tag. One of "character", "content-fanmade", "content-official", "error", "oc", "origin", "rating", "species", "spoiler". """
    category: str
    
    """ The long description for the tag. """
    description: str
    
    """ An array of objects containing DNP entries claimed on the tag. """
    dnp_entries: list
    
    """ The tag's ID. """
    id: int
    
    """ The image count of the tag. """
    images: int
    
    """ The slugs of the tags this tag is implied by. """
    implied_by_tags: list
    
    """ The slugs of the tags this tag implies. """
    implied_tags: list
    
    """ The name of the tag. """
    name: str
    
    """ The name of the tag in its namespace. """
    name_in_namespace: str
    
    """ The namespace of the tag. """
    namespace: str
    
    """ The short description for the tag. """
    short_description: str
    
    """ The slug for the tag. """
    slug: str
    
    """ The spoiler image URL for the tag. """
    spoiler_image: str
    

    def __init__(
        self, 
        aliased_tag: str,
        aliases: list,
        category: str,
        description: str,
        dnp_entries: list,
        id: int,
        images: int,
        implied_by_tags: list,
        implied_tags: list,
        name: str,
        name_in_namespace: str,
        namespace: str,
        short_description: str,
        slug: str,
        spoiler_image: str,
    ):
        """
        A parsed Tag response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param aliased_tag: The slug of the tag this tag is aliased to, if any.
        :type  aliased_tag: str
        
        :param aliases: The slugs of the tags aliased to this tag.
        :type  aliases: list
        
        :param category: The category class of this tag. One of "character", "content-fanmade", "content-official", "error", "oc", "origin", "rating", "species", "spoiler".
        :type  category: str
        
        :param description: The long description for the tag.
        :type  description: str
        
        :param dnp_entries: An array of objects containing DNP entries claimed on the tag.
        :type  dnp_entries: list
        
        :param id: The tag's ID.
        :type  id: int
        
        :param images: The image count of the tag.
        :type  images: int
        
        :param implied_by_tags: The slugs of the tags this tag is implied by.
        :type  implied_by_tags: list
        
        :param implied_tags: The slugs of the tags this tag implies.
        :type  implied_tags: list
        
        :param name: The name of the tag.
        :type  name: str
        
        :param name_in_namespace: The name of the tag in its namespace.
        :type  name_in_namespace: str
        
        :param namespace: The namespace of the tag.
        :type  namespace: str
        
        :param short_description: The short description for the tag.
        :type  short_description: str
        
        :param slug: The slug for the tag.
        :type  slug: str
        
        :param spoiler_image: The spoiler image URL for the tag.
        :type  spoiler_image: str
        
        """
        pass
    # end def __init__
# end class



class User(DerpiModel):
    """
    A parsed User response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param id: The ID of the user.
    :type  id: int
    
    :param name: The name of the user.
    :type  name: str
    
    :param slug: The slug of the user.
    :type  slug: str
    
    :param role: The role of the user.
    :type  role: str
    
    :param description: The description (bio) of the user.
    :type  description: str
    
    :param avatar_url: The URL of the user's thumbnail. Null if they haven't set one.
    :type  avatar_url: str
    
    :param created_at: The creation time, in UTC, of the user.
    :type  created_at: datetime
    
    :param comments_count: The comment count of the user.
    :type  comments_count: int
    
    :param uploads_count: The upload count of the user.
    :type  uploads_count: int
    
    :param posts_count: The forum posts count of the user.
    :type  posts_count: int
    
    :param topics_count: The forum topics count of the user.
    :type  topics_count: int
    
    :param links: The links the user has registered. See `Links`.
    :type  links: Links
    
    :param awards: The awards/badges of the user. See `Awards`.
    :type  awards: Awards
    
    """

    
    """ The ID of the user. """
    id: int
    
    """ The name of the user. """
    name: str
    
    """ The slug of the user. """
    slug: str
    
    """ The role of the user. """
    role: str
    
    """ The description (bio) of the user. """
    description: str
    
    """ The URL of the user's thumbnail. Null if they haven't set one. """
    avatar_url: str
    
    """ The creation time, in UTC, of the user. """
    created_at: datetime
    
    """ The comment count of the user. """
    comments_count: int
    
    """ The upload count of the user. """
    uploads_count: int
    
    """ The forum posts count of the user. """
    posts_count: int
    
    """ The forum topics count of the user. """
    topics_count: int
    
    """ The links the user has registered. See `Links`. """
    links: Links
    
    """ The awards/badges of the user. See `Awards`. """
    awards: Awards
    

    def __init__(
        self, 
        id: int,
        name: str,
        slug: str,
        role: str,
        description: str,
        avatar_url: str,
        created_at: datetime,
        comments_count: int,
        uploads_count: int,
        posts_count: int,
        topics_count: int,
        links: Links,
        awards: Awards,
    ):
        """
        A parsed User response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param id: The ID of the user.
        :type  id: int
        
        :param name: The name of the user.
        :type  name: str
        
        :param slug: The slug of the user.
        :type  slug: str
        
        :param role: The role of the user.
        :type  role: str
        
        :param description: The description (bio) of the user.
        :type  description: str
        
        :param avatar_url: The URL of the user's thumbnail. Null if they haven't set one.
        :type  avatar_url: str
        
        :param created_at: The creation time, in UTC, of the user.
        :type  created_at: datetime
        
        :param comments_count: The comment count of the user.
        :type  comments_count: int
        
        :param uploads_count: The upload count of the user.
        :type  uploads_count: int
        
        :param posts_count: The forum posts count of the user.
        :type  posts_count: int
        
        :param topics_count: The forum topics count of the user.
        :type  topics_count: int
        
        :param links: The links the user has registered. See `Links`.
        :type  links: Links
        
        :param awards: The awards/badges of the user. See `Awards`.
        :type  awards: Awards
        
        """
        pass
    # end def __init__
# end class



class Filter(DerpiModel):
    """
    A parsed Filter response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param id: The id of the filter.
    :type  id: int
    
    :param name: The name of the filter.
    :type  name: str
    
    :param description: The description of the filter.
    :type  description: str
    
    :param user_id: The id of the user the filter belongs to. Null if it isn't assigned to a user (usually system filters only).
    :type  user_id: int
    
    :param user_count: The amount of users employing this filter.
    :type  user_count: int
    
    :param system: If true, is a system filter. System filters are usable by anyone and don't have a user_id set.
    :type  system: bool
    
    :param public: If true, is a public filter. Public filters are usable by anyone.
    :type  public: bool
    
    :param spoilered_tag_ids: A list of tag IDs (as integers) that this filter will spoil.
    :type  spoilered_tag_ids: list
    
    :param spoilered_complex: The complex spoiled filter.
    :type  spoilered_complex: str
    
    :param hidden_tag_ids: A list of tag IDs (as integers) that this filter will hide.
    :type  hidden_tag_ids: list
    
    :param hidden_complex: The complex hidden filter.
    :type  hidden_complex: str
    
    """

    
    """ The id of the filter. """
    id: int
    
    """ The name of the filter. """
    name: str
    
    """ The description of the filter. """
    description: str
    
    """ The id of the user the filter belongs to. Null if it isn't assigned to a user (usually system filters only). """
    user_id: int
    
    """ The amount of users employing this filter. """
    user_count: int
    
    """ If true, is a system filter. System filters are usable by anyone and don't have a user_id set. """
    system: bool
    
    """ If true, is a public filter. Public filters are usable by anyone. """
    public: bool
    
    """ A list of tag IDs (as integers) that this filter will spoil. """
    spoilered_tag_ids: list
    
    """ The complex spoiled filter. """
    spoilered_complex: str
    
    """ A list of tag IDs (as integers) that this filter will hide. """
    hidden_tag_ids: list
    
    """ The complex hidden filter. """
    hidden_complex: str
    

    def __init__(
        self, 
        id: int,
        name: str,
        description: str,
        user_id: int,
        user_count: int,
        system: bool,
        public: bool,
        spoilered_tag_ids: list,
        spoilered_complex: str,
        hidden_tag_ids: list,
        hidden_complex: str,
    ):
        """
        A parsed Filter response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param id: The id of the filter.
        :type  id: int
        
        :param name: The name of the filter.
        :type  name: str
        
        :param description: The description of the filter.
        :type  description: str
        
        :param user_id: The id of the user the filter belongs to. Null if it isn't assigned to a user (usually system filters only).
        :type  user_id: int
        
        :param user_count: The amount of users employing this filter.
        :type  user_count: int
        
        :param system: If true, is a system filter. System filters are usable by anyone and don't have a user_id set.
        :type  system: bool
        
        :param public: If true, is a public filter. Public filters are usable by anyone.
        :type  public: bool
        
        :param spoilered_tag_ids: A list of tag IDs (as integers) that this filter will spoil.
        :type  spoilered_tag_ids: list
        
        :param spoilered_complex: The complex spoiled filter.
        :type  spoilered_complex: str
        
        :param hidden_tag_ids: A list of tag IDs (as integers) that this filter will hide.
        :type  hidden_tag_ids: list
        
        :param hidden_complex: The complex hidden filter.
        :type  hidden_complex: str
        
        """
        pass
    # end def __init__
# end class



class Links(DerpiModel):
    """
    A parsed Links response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param user_id: The ID of the user who owns this link.
    :type  user_id: int
    
    :param created_at: The creation time, in UTC, of this link.
    :type  created_at: datetime
    
    :param state: The state of this link.
    :type  state: str
    
    :param tag_id: The ID of an associated tag for this link. Null if no tag linked.
    :type  tag_id: int
    
    """

    
    """ The ID of the user who owns this link. """
    user_id: int
    
    """ The creation time, in UTC, of this link. """
    created_at: datetime
    
    """ The state of this link. """
    state: str
    
    """ The ID of an associated tag for this link. Null if no tag linked. """
    tag_id: int
    

    def __init__(
        self, 
        user_id: int,
        created_at: datetime,
        state: str,
        tag_id: int,
    ):
        """
        A parsed Links response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param user_id: The ID of the user who owns this link.
        :type  user_id: int
        
        :param created_at: The creation time, in UTC, of this link.
        :type  created_at: datetime
        
        :param state: The state of this link.
        :type  state: str
        
        :param tag_id: The ID of an associated tag for this link. Null if no tag linked.
        :type  tag_id: int
        
        """
        pass
    # end def __init__
# end class



class Awards(DerpiModel):
    """
    A parsed Awards response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param image_url: The URL of this award.
    :type  image_url: str
    
    :param title: The title of this award.
    :type  title: str
    
    :param id: The ID of the badge this award is derived from.
    :type  id: int
    
    :param label: The label of this award.
    :type  label: str
    
    :param awarded_on: The time, in UTC, when this award was given.
    :type  awarded_on: datetime
    
    """

    
    """ The URL of this award. """
    image_url: str
    
    """ The title of this award. """
    title: str
    
    """ The ID of the badge this award is derived from. """
    id: int
    
    """ The label of this award. """
    label: str
    
    """ The time, in UTC, when this award was given. """
    awarded_on: datetime
    

    def __init__(
        self, 
        image_url: str,
        title: str,
        id: int,
        label: str,
        awarded_on: datetime,
    ):
        """
        A parsed Awards response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param image_url: The URL of this award.
        :type  image_url: str
        
        :param title: The title of this award.
        :type  title: str
        
        :param id: The ID of the badge this award is derived from.
        :type  id: int
        
        :param label: The label of this award.
        :type  label: str
        
        :param awarded_on: The time, in UTC, when this award was given.
        :type  awarded_on: datetime
        
        """
        pass
    # end def __init__
# end class



class Gallery(DerpiModel):
    """
    A parsed Gallery response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param description: The gallery's description.
    :type  description: str
    
    :param id: The gallery's ID.
    :type  id: int
    
    :param spoiler_warning: The gallery's spoiler warning.
    :type  spoiler_warning: str
    
    :param thumbnail_id: The ID of the cover image for the gallery.
    :type  thumbnail_id: int
    
    :param title: The gallery's title.
    :type  title: str
    
    :param user: The name of the gallery's creator.
    :type  user: str
    
    :param user_id: The ID of the gallery's creator.
    :type  user_id: int
    
    """

    
    """ The gallery's description. """
    description: str
    
    """ The gallery's ID. """
    id: int
    
    """ The gallery's spoiler warning. """
    spoiler_warning: str
    
    """ The ID of the cover image for the gallery. """
    thumbnail_id: int
    
    """ The gallery's title. """
    title: str
    
    """ The name of the gallery's creator. """
    user: str
    
    """ The ID of the gallery's creator. """
    user_id: int
    

    def __init__(
        self, 
        description: str,
        id: int,
        spoiler_warning: str,
        thumbnail_id: int,
        title: str,
        user: str,
        user_id: int,
    ):
        """
        A parsed Gallery response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param description: The gallery's description.
        :type  description: str
        
        :param id: The gallery's ID.
        :type  id: int
        
        :param spoiler_warning: The gallery's spoiler warning.
        :type  spoiler_warning: str
        
        :param thumbnail_id: The ID of the cover image for the gallery.
        :type  thumbnail_id: int
        
        :param title: The gallery's title.
        :type  title: str
        
        :param user: The name of the gallery's creator.
        :type  user: str
        
        :param user_id: The ID of the gallery's creator.
        :type  user_id: int
        
        """
        pass
    # end def __init__
# end class



class Oembed(DerpiModel):
    """
    A parsed Oembed response of the Derpibooru API.
    Yes, a better description should be here.

    
    :param author_name: The comma-delimited names of the image authors.
    :type  author_name: str
    
    :param author_url: The source URL of the image.
    :type  author_url: str
    
    :param cache_age: Always 7200.
    :type  cache_age: int
    
    :param derpibooru_comments: The number of comments made on the image.
    :type  derpibooru_comments: int
    
    :param derpibooru_id: The image's ID.
    :type  derpibooru_id: int
    
    :param derpibooru_score: The image's number of upvotes minus the image's number of downvotes.
    :type  derpibooru_score: int
    
    :param derpibooru_tags: The names of the image's tags.
    :type  derpibooru_tags: list
    
    :param provider_name: Always "Derpibooru".
    :type  provider_name: str
    
    :param provider_url: Always "https://derpibooru.org".
    :type  provider_url: str
    
    :param title: The image's ID and associated tags, as would be given on the title of the image page.
    :type  title: str
    
    :param type: Always "photo".
    :type  type: str
    
    :param version: Always "1.0".
    :type  version: str
    
    """

    
    """ The comma-delimited names of the image authors. """
    author_name: str
    
    """ The source URL of the image. """
    author_url: str
    
    """ Always 7200. """
    cache_age: int
    
    """ The number of comments made on the image. """
    derpibooru_comments: int
    
    """ The image's ID. """
    derpibooru_id: int
    
    """ The image's number of upvotes minus the image's number of downvotes. """
    derpibooru_score: int
    
    """ The names of the image's tags. """
    derpibooru_tags: list
    
    """ Always "Derpibooru". """
    provider_name: str
    
    """ Always "https://derpibooru.org". """
    provider_url: str
    
    """ The image's ID and associated tags, as would be given on the title of the image page. """
    title: str
    
    """ Always "photo". """
    type: str
    
    """ Always "1.0". """
    version: str
    

    def __init__(
        self, 
        author_name: str,
        author_url: str,
        cache_age: int,
        derpibooru_comments: int,
        derpibooru_id: int,
        derpibooru_score: int,
        derpibooru_tags: list,
        provider_name: str,
        provider_url: str,
        title: str,
        type: str,
        version: str,
    ):
        """
        A parsed Oembed response of the Derpibooru API.
        Yes, a better description should be here.

        
        :param author_name: The comma-delimited names of the image authors.
        :type  author_name: str
        
        :param author_url: The source URL of the image.
        :type  author_url: str
        
        :param cache_age: Always 7200.
        :type  cache_age: int
        
        :param derpibooru_comments: The number of comments made on the image.
        :type  derpibooru_comments: int
        
        :param derpibooru_id: The image's ID.
        :type  derpibooru_id: int
        
        :param derpibooru_score: The image's number of upvotes minus the image's number of downvotes.
        :type  derpibooru_score: int
        
        :param derpibooru_tags: The names of the image's tags.
        :type  derpibooru_tags: list
        
        :param provider_name: Always "Derpibooru".
        :type  provider_name: str
        
        :param provider_url: Always "https://derpibooru.org".
        :type  provider_url: str
        
        :param title: The image's ID and associated tags, as would be given on the title of the image page.
        :type  title: str
        
        :param type: Always "photo".
        :type  type: str
        
        :param version: Always "1.0".
        :type  version: str
        
        """
        pass
    # end def __init__
# end class

