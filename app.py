# 统一的FastAPI应用管理
from fastapi import FastAPI

# 创建主应用
app = FastAPI(
    title="向量搜索系统",
    description="用于向量搜索",
    version="1.0.0"
)

# 导入各个模块的路由
from vector_query import router as vector_router

# 注册路由
app.include_router(vector_router, prefix="/v", tags=["向量搜索"])

# 如果有其他API模块，可以继续添加
# from user_api import router as user_router
# app.include_router(user_router, prefix="/api/user", tags=["用户管理"])
