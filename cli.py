from lib.load_content import ContentLoader
from lib.find_info import find_in_pdf
import json
import validators

def prompt_event_url():
    print("Please provide an url of an event you want to scrape.")
    print("See https://ris2.ibabs.eu/Calendar/Index/Utrecht for events.")
    event_url = input()
    event_url = event_url.strip()
    if not validators.url(event_url):
        print("The URL is not valid!")
        exit(1)
    return event_url


def search_all_pdfs(pdf_list, key_words):
    pdf_result = {}
    for pdf in pdf_list:
        list_of_findings = find_in_pdf(pdf['file'], key_words)
        pdf_result[pdf['file']] = list_of_findings
    return pdf_result

def read_key_words_file():
    key_words = []
    with open('key_words.txt', 'r') as key_words_file:
        for line in key_words_file.readlines():
            key_words.append(line.strip())
    return key_words

if __name__ == "__main__":
    print("Welcome to PSC Utrecht scraper 0.0.1")
    key_words = read_key_words_file()
    event_url = prompt_event_url()
    loader = ContentLoader()
    print("Downloading the pdfs")
    pdfs = loader.download_all_content_from_website(event_url)
    print("Searching pdfs")
    results = search_all_pdfs(pdfs, key_words)
    print("Here is what we found:")
    print(json.dumps(results, indent=4, sort_keys=True))