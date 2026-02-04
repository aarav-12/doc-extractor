Insurance Document Parser

This project extracts key financial information from an insurance policy document and presents it in a structured format. The focus is on keeping the solution simple, reliable, and easy to understand.

What it does

The parser reads an insurance policy schedule and extracts the most important financial fields:

Policy Number

Policy Period (start and end date)

Gross Premium

GST

Total Premium

The output is printed as structured JSON.

How it works

The PDF is converted to text using PyMuPDF.

The policy schedule section is identified, as it contains customer-specific data.

Regex-based patterns are used to extract financial fields from the text.

Edge cases (such as current vs previous policy number) are handled using contextual checks.

This approach is lightweight, fast, and easy to debug.

Project structure
doc-extractor/
├── extract.py
├── policy.pdf
├── approach.md
└── README.md

Setup & Run

Install dependency:

pip install pymupdf


Run the parser:

python extract.py

Sample output
{
  "policy_number": "253200/31/2024/238",
  "policy_period": {
    "from": "25/05/2023",
    "to": "24/05/2024"
  },
  "gross_premium": "9079",
  "gst": "1634",
  "total_premium": "10713"
}
