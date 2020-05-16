import pdftotext


def parse_pdf_links_from_html(html):
    """

    :param html:
    :type html: str
    :return:
    """
    splitted_at_pdf_class = html.split('<li class="pdf">')
    # Remove the first split because it is the html start
    splitted_at_pdf_class = splitted_at_pdf_class[1:]

    links_to_pdfs = []
    for pdf_link_element in splitted_at_pdf_class:
        # Find the start of the href
        link_start = pdf_link_element.find('<a href="') + 9
        # Cut the beginning
        href = pdf_link_element[link_start:]
        # Cut the end
        link = href[:href.find('"')]
        link = link.replace('&amp;', '&')
        # name of the link
        label = href[href.find('>')+1:href.find('</a>')]

        links_to_pdfs.append({
            "name": label,
            "url": link
        })

    return links_to_pdfs


def find_in_pdf(file_path, key_words):
    """

    :param file_path:
    :type file_path: str
    :param key_words:
    :type key_words: list of str
    :return: dict containing the keywords and a list of pages where it appears
    """
    # Initialize return value with empty lists
    found_key_words = {}
    for w in key_words:
        found_key_words[w] = []

    with open(file_path, 'rb') as pdf_file:
        # Parse the pdf
        # package PyPDF2 does not work correctly use pdftotext instead
        pdf_document = pdftotext.PDF(pdf_file)

        # Go over all pdf pages
        for i in range(len(pdf_document)):
            pdf_page = pdf_document[i]
            #print(pdf_page)

            # Check if page contains any of the key words
            key_words_on_this_page = are_in_corpus(key_words, pdf_page)
            for word in key_words_on_this_page:
                if key_words_on_this_page[word]:
                    # Page contains key word
                    found_key_words[word].append(i)

    return found_key_words

def are_in_corpus(key_words, corpus):
    """

    :param key_words: that are searched for
    :type key_words: list of str
    :param corpus: that is searched
    :type corpus: str
    :return: true if the
    """
    corpus = corpus.lower()
    result = {}
    for word in key_words:
        if corpus.find(word.lower()) >= 0:
            result[word] = True
        else:
            result[word] = False
    return result