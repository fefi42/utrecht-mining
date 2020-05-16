from lib.load_content import ContentLoader
from graph.loader import WeaviateLoader


def add_pdf_to_weaviate(pdfs):
    """

    :param pdfs:
    :type pdfs: list of dict
    :return:
    """
    wl = WeaviateLoader()
    i = 0
    for pdf in pdfs:
        print(f"Loading pdf {i} to weaviate")
        wl.add_pdf(pdf)
        i += 1


# TODO replace urls by a script that finds them automatically
urls = ["https://ris2.ibabs.eu/Agenda/Details/Utrecht/3d443019-361b-4066-b94a-033ca60c2e94"]

if __name__ == "__main__":
    loader = ContentLoader()
    print("Downloading the pdfs")
    pdfs = loader.download_all_content_from_website(urls[0])

    print("Load them to weaviate")
    results = add_pdf_to_weaviate(pdfs)
    print("Finished 👋")