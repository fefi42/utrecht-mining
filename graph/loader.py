import os
import weaviate
import pdftotext
import uuid

def generate_uuid(namespace, identifier):
    """ Generate an uuid
    :param namespace: allows to make identifiers unique if they come from different source systems.
                      E.g. google maps, osm, ...
    :param identifier: that is used to generate the uuid
    :return: properly formed uuid in form of string
    """
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, namespace+identifier))

class WeaviateLoader:

    def __init__(self):
        url = os.getenv("WEAVIATE_URL")
        if url == "":
            print("env WEAVIATE_URL not set!")
            exit(1)

        self.client = weaviate.Client(url)

        if not self.client.contains_schema():
            self.client.create_schema("schema.json")

        self.things_batch = weaviate.batch.ThingsBatchRequest()
        self.reference_batch = weaviate.batch.ReferenceBatchRequest()

    def add_pdf(self, pdf):
        """

        :param pdf: that should be added to weaviate
        :type pdf: dict
        :return:
        """
        document = {
            "naam": pdf["name"],
            "url": pdf["url"]
        }

        document_id = generate_uuid(pdf["url"], pdf["name"])
        self.things_batch.add_thing(document, "Document", document_id)

        with open(pdf["file"], 'rb') as pdf_file:
            # Parse the pdf
            # package PyPDF2 does not work correctly use pdftotext instead
            pdf_document_content = pdftotext.PDF(pdf_file)
            for i in range(len(pdf_document_content)):
                pdf_page_content = pdf_document_content[i]
                pdf_page_content = str(pdf_page_content).replace("\n", " ")

                page = {
                    "nummer": i,
                    "tekst": pdf_page_content
                }
                page_id = generate_uuid(document_id, str(i))
                self.things_batch.add_thing(page, "Pagina", page_id)
                self.reference_batch.add_reference("Pagina", page_id, "vanDocument", document_id)
                self.reference_batch.add_reference("Document", document_id, "heeftPaginas", page_id)

        self.client.create_things_in_batch(self.things_batch)
        self.client.add_references_in_batch(self.reference_batch)
        self.things_batch = weaviate.batch.ThingsBatchRequest()
        self.reference_batch = weaviate.batch.ReferenceBatchRequest()