import pandas as pd
import re
from embedder import embed_dataframe, tokenize_text, embed_text
from qdrant_client_utils import init_qdrant_client, recreate_collection, insert_data, search
from openai_utils import clarify_question, choose_best_match
from config import QDRANT_TOP_K

# Load dữ liệu
df = pd.read_excel("data/BỘ 250 CÂU HỎI CỦA SINH VIÊN VỀ TRƯỜNG ĐẠI HỌC CÔNG THƯƠNG TP.HCM.xlsx", header=1)
df = df.iloc[:, :3].drop(columns=["STT"])
df["STT"] = range(1, len(df) + 1)

# Embedding
df = embed_dataframe(df)

# Qdrant
client = init_qdrant_client()
recreate_collection(client)
count = insert_data(client, df)
print(f"✅ Đã lưu {count} câu hỏi vào Qdrant.")

# Truy vấn người dùng
query_text = input("Nhập câu hỏi: ")
clarified = clarify_question(query_text)
print(f"\n🧠 Câu hỏi sau khi làm rõ: {clarified}")

query_vector = embed_text(tokenize_text(clarified))
results = search(client, query_vector, QDRANT_TOP_K)

retrieved = [(res.id, res.payload["question"]) for res in results]
response_text = choose_best_match(clarified, retrieved)

match = re.fullmatch(r"\d+", response_text)
if match:
    best_stt = int(match.group())
    row = df[df["STT"] == best_stt].iloc[0]
    print(f"\n✅ Câu phù hợp nhất (STT {best_stt}): {row['Câu hỏi']}")
    print(f"💡 Câu trả lời: {row['Câu trả lời ']}")
else:
    print("🤖 Tôi không có thông tin.")
