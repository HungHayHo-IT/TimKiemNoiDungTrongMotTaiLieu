from pageindex import PageIndexClient
import os
from dotenv import load_dotenv

load_dotenv()

# Khởi tạo client
pi_client = PageIndexClient(api_key=os.getenv("PAGEINDEX_API_KEY"))

# Index file PDF
print("Đang xử lý file PDF...")
result = pi_client.index("./examples/published-course-curriculum.pdf")
print(f"Kết quả index: {result}")

# Lấy doc_id từ result
doc_id = result.get("doc_id") or result.get("id")
print(f"Doc ID: {doc_id}")

# Lấy cấu trúc cây của tài liệu
structure = pi_client.get_document_structure(doc_id)
print(f"Cấu trúc tài liệu: {structure}")