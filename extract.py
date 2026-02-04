
import re
import fitz

# Open PDF
doc = fitz.open("policy.pdf")

# Extract full text
text = ""
for page in doc:
    text += page.get_text()

# REGEX EXTRACTION 

policy_no = re.search(
    r"(?<!Prev\s)Policy No\s*:\s*([0-9/]+)",
    text
)


policy_period = re.search(
    r"FROM\s+[0-9: ]+ON\s+([0-9/]+)\s+TO\s+MIDNIGHT\s+OF\s+([0-9/]+)",
    text
)
gross_premium = re.search(r"\n\s*([0-9,]+)\s*\n\s*[0-9,]+\s*\n\s*\.5\s*\n\s*[0-9,]+", text)
gst = re.search(r"\n\s*[0-9,]+\s*\n\s*([0-9,]+)\s*\n\s*\.5", text)
total_premium = re.search(r"\n\s*[0-9,]+\s*\n\s*[0-9,]+\s*\n\s*\.5\s*\n\s*([0-9,]+)", text)

#STRUCTURED OUTPUT

data = {
    "policy_number": policy_no.group(1) if policy_no else None,
    "policy_period": {
        "from": policy_period.group(1),
        "to": policy_period.group(2)
    } if policy_period else None,
    "gross_premium": gross_premium.group(1).replace(",", "") if gross_premium else None,
    "gst": gst.group(1).replace(",", "") if gst else None,
    "total_premium": total_premium.group(1).replace(",", "") if total_premium else None
}

print(data)
