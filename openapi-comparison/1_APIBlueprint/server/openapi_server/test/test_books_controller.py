import unittest

from flask import json

from openapi_server.models.lyth_ng_tin_sch_theo_id200_response import LYThNgTinSChTheoID200Response  # noqa: E501
from openapi_server.models.th_msch_mi400_response import ThMSChMI400Response  # noqa: E501
from openapi_server.models.th_msch_mi_request import ThMSChMIRequest  # noqa: E501
from openapi_server.models.xasch_theo_id204_response import XASChTheoID204Response  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBooksController(BaseTestCase):
    """BooksController integration test stubs"""

    def test_cp_nht_thng_tin_sch_theo_id(self):
        """Test case for cp_nht_thng_tin_sch_theo_id

        Cập nhật thông tin sách theo ID
        """
        body = openapi_server.ThMSChMIRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books/{id}'.format(id=1),
            method='PUT',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ly_danh_sch_tt_c_sch(self):
        """Test case for ly_danh_sch_tt_c_sch

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

    def test_ly_thng_tin_sch_theo_id(self):
        """Test case for ly_thng_tin_sch_theo_id

        Lấy thông tin sách theo ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{id}'.format(id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_thm_sch_mi(self):
        """Test case for thm_sch_mi

        Thêm sách mới
        """
        body = openapi_server.ThMSChMIRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_xa_sch_theo_id(self):
        """Test case for xa_sch_theo_id

        Xóa sách theo ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{id}'.format(id=1),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
