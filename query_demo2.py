import chromadb

# 连接到数据库并获取集合
client = chromadb.PersistentClient(path="E:/chroma_demo/chroma_db")
collection = client.get_collection(name="meditation_collection")

print("=== 基本查询操作 ===")

# 1. 查看集合信息
print(f"集合名称: {collection.name}")
print(f"文档总数: {collection.count()}")

# 2. 获取所有文档ID
all_docs = collection.get()
print(f"所有文档ID: {all_docs['ids']}")

# 3. 获取特定文档
anxiety_doc = collection.get(ids=["anxiety_relief"])
if anxiety_doc['ids']:
    print(f"\n焦虑缓解文档内容: {anxiety_doc['documents'][0][:200]}...")
    print(f"音频文件: {anxiety_doc['metadatas'][0].get('audio_key', 'N/A')}")

# 4. 根据元数据查询
meditation_docs = collection.get(where={"type": "meditation_guide"})
print(f"\n冥想指南文档数量: {len(meditation_docs['ids'])}")

# 5. 简单的文本搜索（如果支持）
try:
    results = collection.query(
        query_texts=["焦虑"],
        n_results=2
    )
    print(f"\n搜索'焦虑'的结果:")
    for i, doc_id in enumerate(results['ids'][0]):
        print(f"  {i+1}. {doc_id} (相似度: {1-results['distances'][0][i]:.3f})")
except Exception as e:
    print(f"\n搜索功能需要嵌入函数: {e}")

print("\n查询完成！")



