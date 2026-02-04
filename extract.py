import fitz  # PyMuPDF

doc = fitz.open("resume.pdf")

text = ""
for page in doc:
    text += page.get_text()

print(text[:500])
