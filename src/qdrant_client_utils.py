from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from config import QDRANT_HOST, QDRANT_PORT, QDRANT_COLLECTION_NAME

def init_qdrant_client():
    return QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def recreate_collection(client, vector_size=768):
    client.recreate_collection(
        collection_name=QDRANT_COLLECTION_NAME,
        vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
    )

def insert_data(client, df):
    points = []
    for _, row in df.iterrows():
        points.append(PointStruct(
            id=int(row["STT"]),
            vector=row["embedding"],
            payload={
                "question": row["Câu hỏi"],
                "tokenized": row["Câu hỏi tokenized"],
            }
        ))
    client.upsert(collection_name=QDRANT_COLLECTION_NAME, points=points)
    return len(points)

def search(client, vector, top_k):
    return client.search(
        collection_name=QDRANT_COLLECTION_NAME,
        query_vector=vector,
        limit=top_k,
        with_payload=True
    )
