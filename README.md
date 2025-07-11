
# 🧪 Aganitha Paper Fetcher

This project is a Python command-line tool that fetches research papers from PubMed based on a user-specified query. It identifies papers where at least one author is affiliated with a **non-academic (pharma/biotech)** company and saves the results in a CSV file.

---

## ✨ Features

- Fetches research papers using the PubMed API  
- Filters authors with non-academic/company affiliations  
- Saves filtered results as a CSV  
- Command-line input for dynamic keyword search  

---

## 📦 Requirements

- Python 3.x  
- `requests` module  

Install it by running:
```bash
pip install requests


---

🚀 How to Run

python main.py

1. Enter a keyword (e.g., cancer, diabetes)


2. The script will:

Fetch PubMed IDs

Download metadata (XML)

Parse affiliations

Save valid results to filtered_papers.csv





---

📁 Output Files

paper_details.xml: Raw metadata of fetched papers

filtered_papers.csv: Final filtered paper info



---

🧠 Tools & Technologies Used

Python 3

requests – for API calls

xml.etree.ElementTree – for XML parsing

csv – for file output

ChatGPT – for LLM-based development guidance



---



## 📊 Sample Output CSV Fields

| Column Name               | Description                                         |
|--------------------------|-----------------------------------------------------|
| PubmedID                 | Unique paper ID                                     |
| Title                    | Title of the paper                                  |
| Publication Date         | Year of publication                                 |
| Non-academic Author(s)   | Authors with company affiliation                    |
| Company Affiliation(s)   | Names of pharma/biotech companies from affiliation  |


Heuristics for Non-Academic Authors

-Affiliations not containing
keywords like:
university, institute, college, school, department are assumed to be company or industry-affiliated.

 Developer Info

Name: Srinavya
Batch: 2024
Role: Full Stack Developer Intern (Fresher)

*Notes for Reviewers*

-This project is a submission for Aganitha's Take-Home Exercise 2025.
-The code is organized in a single CLI-based script.
-Guidance and LLM help were taken via ChatGPT (OpenAI) for logic design and optimization.


