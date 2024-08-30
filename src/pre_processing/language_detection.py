from PyPDF2 import PdfFileReader
from langdetect import detect

def detect_language_from_pdf(pdf_path: str) -> str:
    """
    Detect the language of a PDF file.
    Parameters
    ----------
    filepath : str
        The path to the PDF file.
    Returns
    -------
    str
        The language of the PDF file.
    """
    with open(pdf_path, "rb") as file:
        reader = PdfFileReader(file)
        text = ""
        #Read first 1000 characters from the pdf to sample the text
        for page_num in range(min(10,reader.numPages())):
            text += reader.getPage(page_num).extractText()
        #Detect the language of sample text
        language = detect(text)
    return language
