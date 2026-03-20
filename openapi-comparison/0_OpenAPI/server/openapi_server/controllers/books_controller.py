import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.book_input import BookInput  # noqa: E501
from openapi_server.models.books_book_id_delete204_response import BooksBookIdDelete204Response  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util


def books_book_id_delete(book_id):  # noqa: E501
    """Xóa sách theo ID

     # noqa: E501

    :param book_id: 
    :type book_id: int

    :rtype: Union[BooksBookIdDelete204Response, Tuple[BooksBookIdDelete204Response, int], Tuple[BooksBookIdDelete204Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def books_book_id_get(book_id):  # noqa: E501
    """Lấy thông tin sách theo ID

     # noqa: E501

    :param book_id: 
    :type book_id: int

    :rtype: Union[Book, Tuple[Book, int], Tuple[Book, int, Dict[str, str]]
    """
    return 'do some magic!'


def books_book_id_put(book_id, body):  # noqa: E501
    """Cập nhật thông tin sách theo ID

     # noqa: E501

    :param book_id: 
    :type book_id: int
    :param book_input: 
    :type book_input: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    book_input = body
    if connexion.request.is_json:
        book_input = BookInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def books_get():  # noqa: E501
    """Lấy danh sách tất cả sách

     # noqa: E501


    :rtype: Union[List[Book], Tuple[List[Book], int], Tuple[List[Book], int, Dict[str, str]]
    """
    return 'do some magic!'


def books_post(body):  # noqa: E501
    """Thêm sách mới

     # noqa: E501

    :param book_input: 
    :type book_input: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    book_input = body
    if connexion.request.is_json:
        book_input = BookInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
