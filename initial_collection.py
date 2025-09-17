import chromadb
import os
import glob
import hashlib

client = chromadb.PersistentClient(path="E:/chroma_demo/chroma_db")
collection = client.create_collection(name="meditation_collection")

# 读取meditationDocuments目录下的所有txt文件
documents_dir = "E:/chroma_demo/meditationDocuments"
txt_files = glob.glob(os.path.join(documents_dir, "*.txt"))

documents = []
metadatas = []
ids = []

for file_path in txt_files:
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 从文件名提取主题名作为ID
    filename = os.path.basename(file_path)
    
    # 使用内容哈希作为ID
    # 不使用uuid，用hash去检测重复
    doc_id = hashlib.md5(content.encode('utf-8')).hexdigest()
    
    # 构建对应的音频文件路径
    audio_file = os.path.join("E:/chroma_demo/meditationAudios", filename)
    
    # 添加到列表中
    documents.append(content)
    metadatas.append({
        "filename": filename,
        "tags": "",
        "audio_key": audio_file
    })
    ids.append(doc_id)

# 添加到集合中
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)
