import re
import fitz


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        page_text = page.get_text()
        full_text += page_text + "\n"

    return full_text


def find_policy_number(text):
    lines = text.split("\n")

    for line in lines:
        if "Policy No" in line and "Prev" not in line:
            match = re.search(r"([0-9/]+)", line)
            if match:
                return match.group(1)

    return None


def find_policy_period(text):
    match = re.search(
        r"FROM\s+[0-9: ]+ON\s+([0-9/]+)\s+TO\s+MIDNIGHT\s+OF\s+([0-9/]+)",
        text
    )

    if match:
        return {
            "from": match.group(1),
            "to": match.group(2)
        }

    return None


def find_premium_values(text):
    numbers = re.findall(r"\b[0-9,]{3,}\b", text)

    cleaned = []
    for num in numbers:
        cleaned.append(num.replace(",", ""))

    # From observation of the document structure
    if len(cleaned) >= 3:
        gross = cleaned[0]
        gst = cleaned[1]
        total = cleaned[2]
        return gross, gst, total

    return None, None, None


def main():
    text = extract_text_from_pdf("policy.pdf")

    policy_number = find_policy_number(text)
    policy_period = find_policy_period(text)

    gross_premium, gst, total_premium = find_premium_values(text)

    data = {
        "policy_number": policy_number,
        "policy_period": policy_period,
        "gross_premium": gross_premium,
        "gst": gst,
        "total_premium": total_premium
    }

    print(data)


if __name__ == "__main__":
    main()
