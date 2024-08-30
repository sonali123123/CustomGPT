# Install Python packages from requirements.txt
pip install -r requirements.txt

# Download spaCy models for multiple languages
for lang in en fr es de it uk ru zh ja; do
    python -m spacy download $lang
done