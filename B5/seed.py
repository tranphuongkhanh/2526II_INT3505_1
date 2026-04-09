# tạo 1 triệu bản ghi sách giả
import time
from faker import Faker
from app import app, db
from app.models import Book

fake = Faker()

def generate_one_million_books():
    total_records = 1000000
    batch_size = 10000

    with app.app_context():
        print(f"BẮT ĐẦU TẠO {total_records} BẢN GHI...")
        start_time = time.time()
        
        # Biến đếm tổng để đảm bảo ISBN không bao giờ trùng
        total_counter = 1 

        for i in range(0, total_records, batch_size):
            books_batch = []
            for _ in range(batch_size):
                # Tạo ISBN độc nhất dựa trên biến đếm (vd: 978-0000000001)
                unique_isbn = f"978-{total_counter:010d}"
                
                books_batch.append({
                    'isbn': unique_isbn,
                    'title': fake.sentence(nb_words=4).replace('.', ''),
                    'author': fake.name(),
                    'total_copies': fake.random_int(min=5, max=100),
                    'available_copies': fake.random_int(min=0, max=5)
                })
                total_counter += 1
            
            # Chèn 10.000 bản ghi vào database cùng lúc
            db.session.bulk_insert_mappings(Book, books_batch)
            db.session.commit()
            print(f"Đã chèn {i + batch_size} / {total_records} sách...")

        end_time = time.time()
        print(f"HOÀN THÀNH! Tổng thời gian: {end_time - start_time:.2f} giây.")

if __name__ == '__main__':        
    generate_one_million_books()