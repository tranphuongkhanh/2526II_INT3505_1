from locust import HttpUser, task, between
import random

class BookStoreTester(HttpUser):
    # Thời gian nghỉ ngẫu nhiên giữa các lần gửi request của mỗi user (từ 1 đến 3 giây)
    wait_time = between(1, 3)

    @task(3) 
    def view_all_books(self):
        # Trọng số 3: Tương đương 60% lưu lượng sẽ là xem toàn bộ sách
        # Thuộc tính name="" giúp Locust gộp các url động lại thành 1 nhóm trong báo cáo
        self.client.get("/books", name="GET /books")

    @task(1)
    def view_single_book(self):
        book_id = random.randint(1, 3)
        with self.client.get(f"/books/{book_id}", name="GET /books/[id]", catch_response=True) as response:
            if response.status_code == 404:
                response.failure("Không tìm thấy sách")
            elif response.status_code == 200:
                response.success()

    @task(1)
    def create_new_book(self):
        # Trọng số 1: Tương đương 20% lưu lượng là tạo sách mới
        payload = {
            "title": f"Sách Test Hiệu Năng {random.randint(1000, 9999)}",
            "author": "Bot Tự Động",
            "status": "available"
        }
        self.client.post("/books", json=payload, name="POST /books")