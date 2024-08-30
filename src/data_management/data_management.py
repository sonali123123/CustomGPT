import os
from srcs.pre_processing.pdf_processing import load_and_split_data
from srcs.model_management.model_management import save_to_file, load_from_file, index_and_load_model
from srcs.utils.utils import clear_directories, color_text

def check_and_load_data(erase_data=False):
    indexed_data_file = os.path.abspath(".saved_models/indexed_data.pkl")
    model_file = os.path.abspath(".saved_models/model.pkl")

    if not os.path.exists(indexed_data_file) or not os.path.exists(model_file):
        if erase_data:
            print(color_text("Data erased successfully !", "green"))
        else :
            print(color_text("Indexed data or model not found.", "red"))
        os.makedirs(".processed_data/", exist_ok=True)
        os.makedirs(".saved_models/", exist_ok=True)
        raw_data_folder_path = os.path.abspath("data/")
        split_documents = load_and_split_data(raw_data_folder_path)
        db, llm = index_and_load_model(split_documents)
        save_to_file(db, indexed_data_file)
        save_to_file(llm, model_file)
    else:
        print(color_text("Indexed data and model found.", "green"))
        clear_data_answer = None
        while clear_data_answer != "yes" and clear_data_answer != "no":
            clear_data = input(color_text("Do you want to clear the existing data and start fresh? (yes/no): ", "magenta"))
            if clear_data.lower() == 'yes':
                clear_directories(".processed_data/")
                clear_directories(".saved_models/")
                check_and_load_data(erase_data=True)
            elif clear_data.lower() == 'no':
                break
            else:
                print(color_text("Please enter 'yes' or 'no'.", "red"))
        print(color_text("Loading indexed data and model from files...", "yellow"))
        db = load_from_file(indexed_data_file)
        llm = load_from_file(model_file)

    return db, llm