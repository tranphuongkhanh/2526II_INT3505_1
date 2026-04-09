const mongoose = require('mongoose');

const productSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: [true, 'Tên sản phẩm là bắt buộc'],
      trim: true,
      maxlength: [200, 'Tên không được quá 200 ký tự'],
    },
    price: {
      type: Number,
      required: [true, 'Giá là bắt buộc'],
      min: [0, 'Giá không được âm'],
    },
    description: {
      type: String,
      trim: true,
    },
    stock: {
      type: Number,
      default: 0,
      min: [0, 'Số lượng không được âm'],
    },
  },
  {
    timestamps: true, // Tự động thêm createdAt và updatedAt
  }
);

module.exports = mongoose.model('Product', productSchema);
