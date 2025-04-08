# Lớp 1 so khớp câu hỏi (Ultra Pro Max)

Dự án này xây dựng hệ thống tìm kiếm và hỏi đáp dựa trên dữ liệu các câu hỏi thường gặp của sinh viên Trường Đại học Công Thương TP.HCM.

## Hướng dẫn chạy

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```
### 2. Cài đặt và chạy Qdrant Vector Database

Để cài đặt và khởi chạy **Qdrant Vector Database**, thực hiện các bước sau:

Nếu bạn chưa cài đặt Docker, tải và cài đặt tại:  
👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

Mở terminal và chạy lệnh sau:
```bash
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
```
Sau khi chạy, Qdrant sẽ hoạt động tại địa chỉ: http://localhost:6333

### 3. Cấu hình
Tạo file .env và điền các thông tin sau:
```bash
EMBEDDING_MODEL_NAME=dangvantuan/vietnamese-embedding
OPENAI_API_KEY=your_api_key
OPENAI_MODEL_NAME=gpt-4o-mini
QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION_NAME=question_collection
QDRANT_TOP_K=5
```

### 4. Chạy ứng dụng
```bash
python src/main.py
```