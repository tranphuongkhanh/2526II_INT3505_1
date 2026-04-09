/* eslint-disable no-unused-vars */
const Service = require('./Service');
const Product = require('../models/Product');

/**
* Tạo sản phẩm mới
*
* product Product 
* no response value expected for this operation
* */
const createProduct = ({ product }) => new Promise(
  async (resolve, reject) => {
    try {
      const newProduct = new Product(product);
      const savedProduct = await newProduct.save();

      resolve(Service.successResponse(
        savedProduct, 
        201
      ));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Lỗi khi tạo sản phẩm',
        e.status || 500,
      ));
    }
  },
);
/**
* Xóa sản phẩm
*
* id Integer 
* no response value expected for this operation
* */
const deleteProduct = ({ id }) => new Promise(
  async (resolve, reject) => {
    try {
      const deletedProduct = await Product.findByIdAndDelete(id);
      
      if (!deletedProduct) {
        return reject(Service.rejectResponse('Không tìm thấy sản phẩm để xóa', 404));
      }

      resolve(Service.successResponse({
        message: 'Đã xóa sản phẩm thành công',
      }, 200));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Lỗi khi xóa sản phẩm',
        e.status || 500,
      ));
    }
  },
);
/**
* Lấy tất cả sản phẩm
*
* returns List
* */
const getAllProducts = () => new Promise(
  async (resolve, reject) => {
    try {
      const products = await Product.find();
      
      resolve(Service.successResponse(
        products, 
        200
      ));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Lỗi khi lấy danh sách sản phẩm',
        e.status || 500,
      ));
    }
  },
);
/**
* Lấy sản phẩm theo ID
*
* id Integer 
* no response value expected for this operation
* */
const getProductById = ({ id }) => new Promise(
  async (resolve, reject) => {
    try {
      const product = await Product.findById(id);
      
      if (!product) {
        return reject(Service.rejectResponse('Không tìm thấy sản phẩm', 404));
      }
      
      resolve(Service.successResponse(
        product, 
        200
      ));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Lỗi khi truy vấn sản phẩm',
        e.status || 500,
      ));
    }
  },
);
/**
* Cập nhật sản phẩm
*
* id Integer 
* product Product 
* no response value expected for this operation
* */
const updateProduct = ({ id, product }) => new Promise(
  async (resolve, reject) => {
    try {
      // { new: true } đảm bảo Mongoose trả về document SAU KHI đã cập nhật thay vì dữ liệu cũ
      const updatedProduct = await Product.findByIdAndUpdate(id, product, { new: true });
      
      if (!updatedProduct) {
        return reject(Service.rejectResponse('Không tìm thấy sản phẩm để cập nhật', 404));
      }
      
      resolve(Service.successResponse(
        updatedProduct, 
        200
      ));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Lỗi khi cập nhật sản phẩm',
        e.status || 500,
      ));
    }
  },
);

module.exports = {
  createProduct,
  deleteProduct,
  getAllProducts,
  getProductById,
  updateProduct,
};
