from flask import request, jsonify
from datetime import datetime
from app import app, db
from app.models import Reader, Book, BorrowRecord

# Reader API Endpoints

@app.route('/api/readers', methods=['GET'])
def get_all_readers():
    readers = Reader.query.all()
    return jsonify([reader.to_dict() for reader in readers]), 200

@app.route('/api/readers/<int:id>', methods=['GET'])
def get_reader_by_id(id):
    reader = Reader.query.get(id)
    if not reader:
        return jsonify({"error": "Không tìm thấy độc giả"}), 404
    return jsonify(reader.to_dict()), 200

@app.route('/api/readers', methods=['POST'])
def create_reader():
    data = request.json
    new_reader = Reader(
        name=data['name'],
        email=data['email'],
        phone=data.get('phone')
    )
    db.session.add(new_reader)
    db.session.commit()
    return jsonify(new_reader.to_dict()), 201

@app.route('/api/readers/<int:id>', methods=['PUT'])
def update_reader(id):
    reader = Reader.query.get(id)
    if not reader:
        return jsonify({"error": "Không tìm thấy độc giả"}), 404
    
    data = request.json
    reader.name = data.get('name', reader.name)
    reader.email = data.get('email', reader.email)
    reader.phone = data.get('phone', reader.phone)
    
    db.session.commit()
    return jsonify(reader.to_dict()), 200

@app.route('/api/readers/<int:id>', methods=['DELETE'])
def delete_reader(id):
    reader = Reader.query.get(id)
    if not reader:
        return jsonify({"error": "Không tìm thấy độc giả"}), 404
    
    db.session.delete(reader)
    db.session.commit()
    return jsonify({"message": "Đã xóa độc giả thành công"}), 200

# Book API Endpoints

@app.route('/api/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

@app.route('/api/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Không tìm thấy sách"}), 404
    return jsonify(book.to_dict()), 200

@app.route('/api/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(
        isbn=data.get('isbn'),
        title=data['title'],
        author=data.get('author'),
        total_copies=data.get('total_copies', 0),
        available_copies=data.get('available_copies', 0)
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201

@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Không tìm thấy sách"}), 404
    
    data = request.json
    book.isbn = data.get('isbn', book.isbn)
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.total_copies = data.get('total_copies', book.total_copies)
    book.available_copies = data.get('available_copies', book.available_copies)
    
    db.session.commit()
    return jsonify(book.to_dict()), 200

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Không tìm thấy sách"}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Đã xóa sách thành công"}), 200

# BorrowRecord API Endpoints

@app.route('/api/borrow-records', methods=['GET'])
def get_all_records():
    records = BorrowRecord.query.all()
    return jsonify([record.to_dict() for record in records]), 200

@app.route('/api/borrow-records/<int:id>', methods=['GET'])
def get_record_by_id(id):
    record = BorrowRecord.query.get(id)
    if not record:
        return jsonify({"error": "Không tìm thấy phiếu mượn"}), 404
    return jsonify(record.to_dict()), 200

@app.route('/api/borrow-records', methods=['POST'])
def create_record():
    data = request.json
    book = Book.query.get(data['book_id'])
    reader = Reader.query.get(data['reader_id'])

    if not book or not reader:
        return jsonify({"error": "Sách hoặc độc giả không tồn tại"}), 404

    if book.available_copies <= 0:
        return jsonify({"error": "Sách này hiện đã hết bản có sẵn"}), 400

    due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()

    new_record = BorrowRecord(
        reader_id=reader.id,
        book_id=book.id,
        due_date=due_date,
        status='borrowed'
    )
    
    book.available_copies -= 1

    db.session.add(new_record)
    db.session.commit()
    return jsonify(new_record.to_dict()), 201

@app.route('/api/borrow-records/<int:id>', methods=['PUT'])
def update_record(id):
    record = BorrowRecord.query.get(id)
    if not record:
        return jsonify({"error": "Không tìm thấy phiếu mượn"}), 404

    data = request.json
    new_status = data.get('status')

    if new_status == 'returned' and record.status != 'returned':
        book = Book.query.get(record.book_id)
        if book:
            book.available_copies += 1
        
        record.status = 'returned'
        record.return_date = datetime.utcnow().date()
    
    if 'due_date' in data:
        record.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
    
    if new_status and new_status != 'returned':
        record.status = new_status

    db.session.commit()
    return jsonify(record.to_dict()), 200

@app.route('/api/borrow-records/<int:id>', methods=['DELETE'])
def delete_record(id):
    record = BorrowRecord.query.get(id)
    if not record:
        return jsonify({"error": "Không tìm thấy phiếu mượn"}), 404
    
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Đã xóa phiếu mượn thành công"}), 200