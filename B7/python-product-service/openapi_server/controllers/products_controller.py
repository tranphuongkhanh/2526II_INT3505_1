import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.product import Product  # noqa: E501
from openapi_server import util

from bson.objectid import ObjectId
from bson.errors import InvalidId
from database import products_collection

def format_product(mongo_doc):
    """Đổi _id của MongoDB thành id dạng string để khớp với chuẩn OpenAPI"""
    if not mongo_doc:
        return None
    mongo_doc['id'] = str(mongo_doc['_id'])
    del mongo_doc['_id']
    return mongo_doc

def create_product(body):  # noqa: E501
    """Tạo sản phẩm mới

     # noqa: E501

    :param product: 
    :type product: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    product = body
    if connexion.request.is_json:
        product = Product.from_dict(connexion.request.get_json())  # noqa: E501
        product_dict = product.to_dict()
        result = products_collection.insert_one(product_dict)
        product.id = str(result.inserted_id)
        return product, 201
    return 'Dữ liệu đầu vào không hợp lệ', 400


def delete_product(id_):  # noqa: E501
    """Xóa sản phẩm

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        result = products_collection.delete_one({"_id": ObjectId(id_)})
        if result.deleted_count > 0:
            return {'message': 'Đã xóa sản phẩm thành công'}, 200
        return 'Không tìm thấy sản phẩm để xóa', 404
    except InvalidId:
        return 'ID không đúng định dạng', 400


def get_all_products():  # noqa: E501
    """Lấy tất cả sản phẩm

     # noqa: E501


    :rtype: Union[List[Product], Tuple[List[Product], int], Tuple[List[Product], int, Dict[str, str]]
    """
    cursor = products_collection.find()
    products = [format_product(doc) for doc in cursor]    
    return products, 200


def get_product_by_id(id_):  # noqa: E501
    """Lấy sản phẩm theo ID

     # noqa: E501

    :param id: 
    :type id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        doc = products_collection.find_one({"_id": ObjectId(id_)})
        if doc:
            return format_product(doc), 200
        return 'Không tìm thấy sản phẩm', 404
    except InvalidId:
        return 'ID không đúng định dạng', 400


def update_product(id_, body):  # noqa: E501
    """Cập nhật sản phẩm

     # noqa: E501

    :param id: 
    :type id: str
    :param product: 
    :type product: dict | bytes

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    product = body
    if connexion.request.is_json:
        try:
            product = Product.from_dict(connexion.request.get_json())
            update_data = product.to_dict()

            result = products_collection.update_one(
                {"_id": ObjectId(id_)},
                {"$set": update_data}
            )

            if result.matched_count == 0:
                return 'Không tìm thấy sản phẩm để cập nhật', 404

            updated_doc = products_collection.find_one({"_id": ObjectId(id_)})
            return format_product(updated_doc), 200
            
        except InvalidId:
            return 'ID không đúng định dạng', 400
            
    return 'Dữ liệu đầu vào không hợp lệ', 400
