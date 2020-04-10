


class Comment(object):
    """
    https://derpibooru.org/pages/api#comment-response
    """

    """ The comment's author. """
    author: str

    """ The comment text. """
    body: str

    """ The comment's ID. """
    id: int

    """ The ID of the image the comment belongs to. """
    image_id: int

    user_id: int
    """ :var user_id: The ID of the user the comment belongs to, if any. """

    def __init__(self, author: str, body: str, id: int, image_id: int, user_id: int):
        """
        https://derpibooru.org/pages/api#comment-response

        :param author: The comment's author.
        :param body: The comment text.
        :param id: The comment's ID.
        :param image_id: The ID of the image the comment belongs to.
        :param user_id: The ID of the user the comment belongs to, if any.
        """
    # end def
# end class
