# đo thời gian truy xuất trang 9000 của 1 triệu bản ghi với 3 phương pháp phân trang khác nhau
import time
from app import app, db
from app.models import Book

def measure_time(func, method_name):
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(f"⏱Phương pháp {method_name.ljust(20)}: {(end - start) * 1000:.2f} ms")

def benchmark_pagination():
    page = 100000
    per_page = 10
    offset = (page - 1) * per_page
    cursor_id = offset
    
    with app.app_context():
        print(f"ĐANG TRUY XUẤT TRANG {page} (Bỏ qua {offset} bản ghi)...\n")

        # 1. Page-based
        def run_page_based():
            return Book.query.paginate(page=page, per_page=per_page, error_out=False)

        # 2. Offset-based
        def run_offset_based():
            return Book.query.offset(offset).limit(per_page).all()

        # 3. Cursor-based
        def run_cursor_based():
            return Book.query.filter(Book.id > cursor_id).order_by(Book.id.asc()).limit(per_page).all()

        measure_time(run_page_based, "1. Page-based")
        measure_time(run_offset_based, "2. Offset-based")
        measure_time(run_cursor_based, "3. Cursor-based")

if __name__ == '__main__':
    benchmark_pagination()