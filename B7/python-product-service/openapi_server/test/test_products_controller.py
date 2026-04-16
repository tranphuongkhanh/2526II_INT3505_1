import unittest

from flask import json

from openapi_server.models.product import Product  # noqa: E501
from openapi_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_create_product(self):
        """Test case for create_product

        Tạo sản phẩm mới
        """
        product = {"price":15000000,"name":"Laptop Acer Aspire Lite 15","description":"Laptop văn phòng","id":"id","stock":50}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/products',
            method='POST',
            headers=headers,
            data=json.dumps(product),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_product(self):
        """Test case for delete_product

        Xóa sản phẩm
        """
        headers = { 
        }
        response = self.client.open(
            '/products/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_products(self):
        """Test case for get_all_products

        Lấy tất cả sản phẩm
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/products',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product_by_id(self):
        """Test case for get_product_by_id

        Lấy sản phẩm theo ID
        """
        headers = { 
        }
        response = self.client.open(
            '/products/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_product(self):
        """Test case for update_product

        Cập nhật sản phẩm
        """
        product = {"price":15000000,"name":"Laptop Acer Aspire Lite 15","description":"Laptop văn phòng","id":"id","stock":50}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/products/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(product),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
