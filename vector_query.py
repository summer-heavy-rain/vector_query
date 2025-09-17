#发送question文本,返回document的id和distance

from fastapi import FastAPI
import chromadb

# 创建路由
from fastapi import APIRouter
router = APIRouter()

# 连接ChromaDB
client = chromadb.PersistentClient(path="E:/chroma_demo/chroma_db")
collection = client.get_collection(name="meditation_collection")

@router.get("/")
async def root():
    # API根路径
    return {
        "message": "向量搜索API", 
        "usage": "GET /search?question=你的问题"
    }

@router.get("/search")
async def search(question: str):
    # 搜索接口
    # 参数：question - 搜索问题
    # 返回：document的id和distance
    try:
        # 执行搜索 - 直接返回最相似的结果
        results = collection.query(
            query_texts=[question],
            n_results=1  # 只返回1个最相似的结果
        )
        
        # 处理结果
        if results['ids'] and results['ids'][0]:
            return {
                "question": question,
                "id": results['ids'][0][0],
                "distance": results['distances'][0][0]
            }
        else:
            return {
                "question": question,
                "id": None,
                "distance": None
            }
        
    except Exception as e:
        return {"error": str(e)}

