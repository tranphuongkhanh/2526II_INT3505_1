import unittest

from flask import json

from openapi_server.models.book import Book  # noqa: E501
from openapi_server.models.book_input import BookInput  # noqa: E501
from openapi_server.models.books_book_id_delete204_response import BooksBookIdDelete204Response  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBooksController(BaseTestCase):
    """BooksController integration test stubs"""

    def test_books_book_id_delete(self):
        """Test case for books_book_id_delete

        Xóa sách theo ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{book_id}'.format(book_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_book_id_get(self):
        """Test case for books_book_id_get

        Lấy thông tin sách theo ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{book_id}'.format(book_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_book_id_put(self):
        """Test case for books_book_id_put

        Cập nhật thông tin sách theo ID
        """
        book_input = {"author":"author","title":"title","status":"available"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books/{book_id}'.format(book_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(book_input),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_get(self):
        """Test case for books_get

        Lấy danh sách tất cả sách
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_post(self):
        """Test case for books_post

        Thêm sách mới
        """
        book_input = {"author":"author","title":"title","status":"available"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='POST',
            headers=headers,
            data=json.dumps(book_input),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
