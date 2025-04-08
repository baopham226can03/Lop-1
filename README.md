# Student FAQ Q&A System

Dự án này xây dựng hệ thống tìm kiếm và hỏi đáp dựa trên dữ liệu các câu hỏi thường gặp của sinh viên Trường Đại học Công Thương TP.HCM.

## Hướng dẫn chạy

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```

### 2. Cấu hình
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

### 3. Chạy ứng dụng
```bash
python src/main.py
```