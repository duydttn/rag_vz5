import os
import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import docx
from chromadb.config import Settings
from config import *
    
def read_file(file_path):
    text = ""
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        raise ValueError("Chỉ hỗ trợ file .pdf, .docx, hoặc .txt")
    return text

def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
        
    return chunks

def main():
    file_path = FILE_PATH
    full_text = read_file(file_path)
    print(f"Đã đọc dữ liệu từ file: {file_path}")
    
    chunks = chunk_text(full_text, chunk_size=CHUNK_SIZE, overlap=OVERLAP)
    print(f"Đã chia thành {len(chunks)} mảnh (chunks).")

    embedding_model = SentenceTransformer(MODEL_NAME)

    print("--- Đang tạo vector embedding cho từng mảnh ---")
    embeddings = embedding_model.encode(chunks).tolist()

    print("--- Đang lưu vào ChromaDB ---")
    client = chromadb.PersistentClient(path=DB_PATH)
    
    # Reset collection để đảm bảo dữ liệu mới nhất
    try:
        client.delete_collection(name=COLLECTION_NAME)
    except:
        pass

    collection = client.create_collection(name=COLLECTION_NAME)
    
    ids = [f"id_{i}" for i in range(len(chunks))]
    metadatas = [{"source": file_path, "chunk_index": i} for i in range(len(chunks))]
    
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )
    print(f"Đã lưu {len(chunks)} mảnh vào collection '{COLLECTION_NAME}'.")

    # --- PHẦN 2: CHẾ ĐỘ TRUY VẤN TƯƠNG TÁC (Mới) ---
    print("\n" + "="*40)
    print("HỆ THỐNG ĐÃ SẴN SÀNG! (Gõ 'exit' để thoát)")
    print("="*40)

    while True:
        query_text = input("\nNhập câu hỏi của bạn: ").strip()
        
        if query_text.lower() in ['exit', 'quit', 'thoat']:
            print("--- Đã thoát chương trình ---")
            break
        
        if not query_text:
            continue

        print(f"-> Đang tìm kiếm...")
        
        query_embedding = embedding_model.encode([query_text]).tolist()
        
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=N_RESULTS, 
            include=["documents", "metadatas", "distances"]
        )
        
        print("-" * 30)
        for i, doc in enumerate(results['documents'][0]):
            meta = results['metadatas'][0][i]
            dist = results['distances'][0][i]
            
            print(f"Kết quả #{i+1} (Distance: {dist:.4f}):")
            print(f"Nội dung: {doc}")
            print("-" * 30)

if __name__ == "__main__":
    main()