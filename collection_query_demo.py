import chromadb
import os
import json


# 连接到已存在的Chroma数据库
client = chromadb.PersistentClient(path="/www/wwwroot/vector_query/chroma_db")

# 获取已存在的集合
collection = client.get_collection(name="meditation_collection")

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["我感到很难过"], 
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
print(json.dumps(results, ensure_ascii=False, indent=4))


