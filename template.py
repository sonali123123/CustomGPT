import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/pre_processing/custom_splitters.py",
    "src/pre_processing/language_detection.py",
    "src/pre_processing/pdf_processing.py",
    "src/pre_processing/text_splitting.py",
    "src/model_management/model_management.py",
    "src/data_management/data_management.py",
    "src/chatbot_interface/chatbot_interface.py",
    "main.py",
    ".gitignore",
    "install.sh"

]


for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")
      
      
    