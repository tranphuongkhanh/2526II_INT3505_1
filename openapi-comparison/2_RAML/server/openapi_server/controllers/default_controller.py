import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.book_input import BookInput  # noqa: E501
from openapi_server.models.delete_books_id204_response import DELETEBooksId204Response  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util


def d_elete_books_id(id):  # noqa: E501
    """d_elete_books_id

    X├│a s├ích theo ID # noqa: E501

    :param id: ID cß╗ºa s├ích
    :type id: int

    :rtype: Union[DELETEBooksId204Response, Tuple[DELETEBooksId204Response, int], Tuple[DELETEBooksId204Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def g_et_books():  # noqa: E501
    """g_et_books

    Lß║Ñy danh s├ích tß║Ñt cß║ú s├ích # noqa: E501


    :rtype: Union[List[Book], Tuple[List[Book], int], Tuple[List[Book], int, Dict[str, str]]
    """
    return 'do some magic!'


def g_et_books_id(id):  # noqa: E501
    """g_et_books_id

    Lß║Ñy th├┤ng tin s├ích theo ID # noqa: E501

    :param id: ID cß╗ºa s├ích
    :type id: int

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    return 'do some magic!'


def p_ost_books(body):  # noqa: E501
    """p_ost_books

    Th├¬m s├ích mß╗¢i # noqa: E501

    :param book_input: 
    :type book_input: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    book_input = body
    if connexion.request.is_json:
        book_input = BookInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def p_ut_books_id(id, body):  # noqa: E501
    """p_ut_books_id

    Cß║¡p nhß║¡t th├┤ng tin s├ích theo ID # noqa: E501

    :param id: ID cß╗ºa s├ích
    :type id: int
    :param book_input: 
    :type book_input: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    book_input = body
    if connexion.request.is_json:
        book_input = BookInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
