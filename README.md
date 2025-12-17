# Hướng Dẫn Test Hệ Thống Mini-RAG

Dưới đây là danh sách các câu hỏi mẫu (Prompts) để kiểm tra khả năng tìm kiếm ngữ nghĩa của hệ thống.

## Nhóm 1: Câu hỏi định nghĩa (Kiểm tra hiểu biết chung)
*Dùng để kiểm tra xem hệ thống có tìm đúng đoạn định nghĩa trong Phần 1 và 2 không.*

1. **"RAG là viết tắt của từ gì và nó hoạt động như thế nào?"**
   *(Kỳ vọng: Tìm thấy đoạn định nghĩa RAG và 3 bước quy trình)*
2. **"Sự khác biệt giữa Machine Learning và Deep Learning?"**
   *(Kỳ vọng: Tìm thấy đoạn so sánh ở Phần 1)*
3. **"ChromaDB dùng để làm gì?"**
   *(Kỳ vọng: Tìm thấy đoạn giải thích về vector database)*

## Nhóm 2: Câu hỏi thông tin cụ thể (Fact retrieval)
*Dùng để kiểm tra khả năng trích xuất thông tin chính xác từ Phần 3.*

4. **"Ai là giảng viên của khóa học này?"**
   *(Kỳ vọng: Tìm thấy tên Tiến sĩ Nguyễn Văn A)*
5. **"Lớp học diễn ra vào lúc nào và ở đâu?"**
   *(Kỳ vọng: Tìm thấy thông tin Thứ 3, 5 và Phòng Lab 305)*
6. **"Học phí khóa học là bao nhiêu?"**
   *(Kỳ vọng: Tìm thấy con số 5.500.000 VNĐ)*
7. **"Tôi cần chuẩn bị máy tính cấu hình thế nào để học?"**
   *(Kỳ vọng: Tìm thấy đoạn yêu cầu RAM 8GB)*

## Nhóm 3: Câu hỏi "bẫy" ngữ nghĩa (Semantic Search Test)
*Dùng từ ngữ khác với văn bản gốc để xem AI có hiểu ý không.*

8. **"Nếu tôi bận và hủy đăng ký sát ngày học thì có được trả lại tiền không?"**
   *(Trong văn bản dùng từ "Hoàn tiền", câu hỏi dùng "trả lại tiền". AI cần tìm ra chính sách hoàn tiền)*
9. **"Khóa học này có dạy về Chatbot không?"**
   *(Trong văn bản không có câu "khóa này dạy chatbot", nhưng có mục "Buổi 5: Thực hành xây dựng Chatbot". AI thông minh sẽ tìm ra đoạn này)*
10. **"Làm sao để liên hệ với người hỗ trợ?"**
    *(Văn bản dùng từ "Trợ giảng", câu hỏi dùng "người hỗ trợ". AI cần tìm ra email của Thạc sĩ Lê Thị B)*
