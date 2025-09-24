1. 初始化chroma数据库，创建相应collection
    -1 initial_collection.py 

2. 测试向量库的搜索
    -2 collection_query_demo.py
    -3 query_demo2.py
  
3. 将ChromaDB中的document迁移到MySQL数据库，meditation_plays表的主键id直接使用collection中每个document的唯一标识符🌟，该标识符通过哈希算法生成，确保全局唯一性
    -4 chroma_migration.py
  
4. 启动服务和路由管理
    -5 run_server.py //启动unicorn服务器，运行FastAPI,http:localhost:8000/
    -6 app.py        //注册注册FastapiApp和路由管理

5. 编写api代码
    -7 vector_query.py//向量搜索


附：
http://localhost:8000/docs：Fastapi提供的查看当前所有api的swagger文档