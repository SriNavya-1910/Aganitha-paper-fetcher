import requests

print("Welcome to Aganitha Paper Fetcher")

# Step 1: Get input from user
query = input("Enter a research keyword to search for papers: ")
print("You entered:", query)

# Step 2: Function to fetch paper IDs from PubMed
def fetch_papers(query):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data["esearchresult"]["idlist"]

# Step 3: Function to fetch paper details using IDs
def fetch_details(paper_ids):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        with open("paper_details.xml", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("Details saved to paper_details.xml")
    else:
        print("Failed to fetch details. Status code:", response.status_code)

# Step 4: Run everything
paper_ids = fetch_papers(query)
print("Paper IDs found:", paper_ids)

fetch_details(paper_ids)
import xml.etree.ElementTree as ET
import csv

def is_non_academic(affiliation):
    if affiliation:
        academic_keywords = ['university', 'college', 'institute', 'school', 'department']
        for word in academic_keywords:
            if word in affiliation.lower():
                return False
        return True
    return False

def parse_and_save_to_csv():
    tree = ET.parse("paper_details.xml")
    root = tree.getroot()

    with open("filtered_papers.csv", mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)"])

        for article in root.findall(".//PubmedArticle"):
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            date = article.findtext(".//PubDate/Year")

            non_academic_authors = []
            company_affiliations = []

            for author in article.findall(".//Author"):
                affiliation = author.findtext(".//AffiliationInfo/Affiliation")
                if is_non_academic(affiliation):
                    lastname = author.findtext("LastName") or ""
                    firstname = author.findtext("ForeName") or ""
                    full_name = f"{firstname} {lastname}".strip()
                    non_academic_authors.append(full_name)
                    company_affiliations.append(affiliation)

            if non_academic_authors:
                writer.writerow([
                    pmid, title, date,
                    "; ".join(non_academic_authors),
                    "; ".join(company_affiliations)
                ])

    print("Filtered results saved to filtered_papers.csv")

# Call this function
parse_and_save_to_csv()