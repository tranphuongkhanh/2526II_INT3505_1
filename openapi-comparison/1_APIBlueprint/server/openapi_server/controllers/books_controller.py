import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.lyth_ng_tin_sch_theo_id200_response import LYThNgTinSChTheoID200Response  # noqa: E501
from openapi_server.models.th_msch_mi400_response import ThMSChMI400Response  # noqa: E501
from openapi_server.models.th_msch_mi_request import ThMSChMIRequest  # noqa: E501
from openapi_server.models.xasch_theo_id204_response import XASChTheoID204Response  # noqa: E501
from openapi_server import util


def cp_nht_thng_tin_sch_theo_id(id, body=None):  # noqa: E501
    """Cập nhật thông tin sách theo ID

     # noqa: E501

    :param id: ID của sách
    :type id: 
    :param body: 
    :type body: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    body = body
    if connexion.request.is_json:
        body = ThMSChMIRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ly_danh_sch_tt_c_sch():  # noqa: E501
    """Lấy danh sách tất cả sách

     # noqa: E501


    :rtype: Union[List[object], Tuple[List[object], int], Tuple[List[object], int, Dict[str, str]]
    """
    return 'do some magic!'


def ly_thng_tin_sch_theo_id(id):  # noqa: E501
    """Lấy thông tin sách theo ID

     # noqa: E501

    :param id: ID của sách
    :type id: 

    :rtype: Union[LYThNgTinSChTheoID200Response, Tuple[LYThNgTinSChTheoID200Response, int], Tuple[LYThNgTinSChTheoID200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def thm_sch_mi(body=None):  # noqa: E501
    """Thêm sách mới

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    body = body
    if connexion.request.is_json:
        body = ThMSChMIRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def xa_sch_theo_id(id):  # noqa: E501
    """Xóa sách theo ID

     # noqa: E501

    :param id: ID của sách
    :type id: 

    :rtype: Union[XASChTheoID204Response, Tuple[XASChTheoID204Response, int], Tuple[XASChTheoID204Response, int, Dict[str, str]]
    """
    return 'do some magic!'
