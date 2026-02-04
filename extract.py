# import re
# import fitz  # PyMuPDF

# # 1. Open the PDF and extract text FIRST
# doc = fitz.open("resume.pdf")

# text = ""
# for page in doc:
#     text += page.get_text()

# # 2. Now search inside the text
# email_match = re.search(
#     r"[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
#     text
# )
# phone_match = re.search(r"\+\d{1,3}[- ]?\d{10}", text)

# if phone_match:
#     phone = phone_match.group()
# else:
#     phone = None

# print("Phone:", phone)


# if email_match:
#     email = email_match.group()
# else:
#     email = None

# print("Email:", email)

# # Optional: sanity check
# print(text[:300])


import fitz

doc = fitz.open("policy.pdf")

text = ""
for page in doc:
    text += page.get_text()

# print(len(text))
for i in range(1, 7):  # pages 2 to 7
    page_text = doc[i].get_text().lower()
    if any(keyword in page_text for keyword in [
        "policy no", "policy number", "premium", "sum insured", "gross premium", "total premium"
    ]):
        print("Financial data found on page:", i + 1)
        print(page_text[:1200])
        break


