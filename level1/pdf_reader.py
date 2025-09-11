from pypdf import PdfReader

pdf_path = r"C:\Users\Admin\OneDrive\Desktop\agentic_ai\level1\sample.pdf"

reader = PdfReader(pdf_path)

for i, page in enumerate(reader.pages, start=1): #extracting text from each page
    text = page.extract_text()
    print(f"--- Page {i} ---")
    print(text)
    print()
