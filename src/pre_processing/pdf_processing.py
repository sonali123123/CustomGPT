import os

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import MarkdownHeaderTextSplitter
from src.pre_processing.custom_splitters import SpacyTextSplitter
from src.pre_processing.text_splitting import get_appropriated_splitter
from src.pre_processing.language_detection import detect_language_from_pdf
from src.utils.utils import color_text

def load_and_split_data(pdf_folder_path):
    """
    Load and split data from PDFs in the specified folder and log details about how documents are split to a file
    """

    processed_data_folder_path = os.path.abspath(".processed_data/") + "/"
    split_documents = []

    for pdf_name in os.listdir(pdf_folder_path):
        splitter = get_appropriated_splitter(pdf_name)
        loader = PyPDFLoader(os.path.join(processed_data_folder_path, pdf_name))
        pages = loader.load()
        if (type(splitter) == MarkdownHeaderTextSplitter):
            pages_to_split = []
            for page in pages:
                splits = splitter.split_text(page.page_content)
                pages_to_split.extend(splits)
            language = detect_language_from_pdf(os.path.abspath(".processed_data/") + "/" + pdf_name)
            splitter = SpacyTextSplitter(chunk_size=1000, language=language)
            pages = pages_to_split
        document_splits = []  # To store splits for current document
        for page in pages:
            splits = splitter.split_text(page.page_content)
            document_splits.extend(splits)
        
        split_documents.extend(document_splits)
        print(color_text(f"Document {pdf_name} split.", "green"))
    return split_documents