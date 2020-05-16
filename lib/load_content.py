import requests
import os
from lib.find_info import parse_pdf_links_from_html


class ContentLoader:

    def __init__(self):
        self.session = requests.session()
        self.html_headers = {
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'HTML',
            'accept-language': 'en-US;q=0.6,en;q=0.4',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
        }
        self.pdf_headers = {
            'method': 'GET',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US;q=0.6,en;q=0.4',
            'cache-control': 'no-cache',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
            'host': 'online.ibabs.eu',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': 1,
            'connection': 'keep-alive'
        }

        current_dir = os.path.dirname(__file__)
        self.downloads_folder = os.path.join(current_dir, "../downloads")

    def load_website(self, url):
        """

        :param url:
        :return: the HTML as a string
        """
        response = self.session.get(url, headers=self.html_headers, timeout=(3, 30))
        return str(response.content)

    def download_pdf(self, url, file_name):
        """ Download pdf into download folder

        :param url: of the pdf that should be loaded
        :param file_name: the name of the file, spaces will be replaced by underscores
        :return: Path to the file (including folder)
        """
        file_name = file_name.replace(" ", "_")

        response = self.session.get(url, headers=self.html_headers, timeout=(3, 30))
        download_file = os.path.join(self.downloads_folder, file_name)
        output_file = open(download_file, 'wb')
        output_file.write(response.content)
        output_file.close()
        return download_file

    def download_all_content_from_website(self, url):
        """

        :param url:
        :return: list of downloaded documents as key 'file' also containing 'name' and 'url'
        :rtype: list of dict
        """
        website = self.load_website(url)
        links = parse_pdf_links_from_html(website)
        # Download all the pdfs and save them in the file
        n = len(links)
        print(f"Found {n} links on the website, starting to download them.")
        for i in range(n):
            print(f"loading {i}/{n}")
            links[i]["file"] = self.download_pdf(links[i]["url"], links[i]["name"])

        return links


if __name__ == "__main__":
    # PDF
    #ContentLoader().load_website("https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&id=e4a91b7f-aaf8-437d-81f4-c3bfe6300d71")

    # HTML
    loader = ContentLoader()
    # html = loader.load_website(
    #     "https://ris2.ibabs.eu/Agenda/Details/Utrecht/f46d8b14-f1a6-40dc-8622-91b548758893")
    #
    #

    loader.download_pdf("https://online.ibabs.eu/ibabsapi/publicdownload.aspx?site=Utrecht&id=ffbcd3ff-ea2c-43b6-87d7-a50fd0df7ef5", "test agenda.pdf")

