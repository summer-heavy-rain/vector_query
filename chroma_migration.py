# 将chroma数据库中的数据迁移到mysql数据库中

import chromadb
import mysql.connector
from datetime import datetime

# 连接到chroma数据库
client = chromadb.PersistentClient(path="E:/chroma_demo/chroma_db")
collection = client.get_collection(name="meditation_collection")

# MySQL数据库配置
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'chromaset',
    'charset': 'utf8mb4'
}

def migrate_chroma_to_mysql():
    """将ChromaDB数据迁移到MySQL"""
    
    # 连接MySQL数据库
    try:
        mysql_conn = mysql.connector.connect(**mysql_config)
        mysql_cursor = mysql_conn.cursor()
        print("✅ MySQL数据库连接成功")
    except mysql.connector.Error as e:
        print(f"❌ MySQL连接失败: {e}")
        return
    
    try:
        # 获取ChromaDB中的所有数据
        results = collection.get()

        # 迁移到meditation_plays表
        for i, (doc_id, document, metadata) in enumerate(zip(
            results['ids'], 
            results['documents'], 
            results['metadatas']
        )):
            filename = metadata.get('filename', f'document_{i}')
            
            # 插入到meditation_plays表，使用ChromaDB的原始ID
            insert_query = """
            INSERT INTO meditation_plays (id, description, create_by)
            VALUES (%s, %s, %s)
            """
            
            values = (
                doc_id,  # 使用ChromaDB的原始ID
                document,  # description字段使用document内容
                1,  # 默认创建人ID
            )
            
            mysql_cursor.execute(insert_query, values)
            play_id = doc_id  # 使用ChromaDB的ID作为play_id
            
            print(f"✅ 迁移记录 {i+1}: {filename}")
        
        # 提交事务
        mysql_conn.commit()
        print(f"🎉 成功迁移 {len(results['documents'])} 条记录到MySQL")
        
    except Exception as e:
        print(f"❌ 迁移过程中出错: {e}")
        mysql_conn.rollback()
    
    finally:
        mysql_cursor.close()
        mysql_conn.close()
        print("🔒 MySQL连接已关闭")

if __name__ == "__main__":
    migrate_chroma_to_mysql()
