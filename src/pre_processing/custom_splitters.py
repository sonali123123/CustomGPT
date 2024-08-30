from __future__ import annotations

from typing import List, Any

from langchain_text_splitters.base import TextSplitter
import spacy
from spacy.language import Language
from spacy_language_detection import language_detector


class SpacyTextSplitter(TextSplitter):
    """
    A text splitter that uses spaCy to split text into chunks.

    """

    def __init__(
        self,
        language: str = "en",
        separator: str = "\n\n",
        max_len: int = 1_000_000,
        **kwargs: Any,
    ) -> None:
        """
        Initialize the SpacyTextSplitter.
        Parameters
        ----------
        language : str, optional
        The language to use for splitting, by default "en"
        seaparator : str, optional
        The separator to use for splitting, by default "\n\n"
        max_
        len : int, optional
        The maximum length of each chunk, by default 1_000_000
        **kwargs : Any
        Additional keyword arguments to pass to the TextSplitter constructor.
        """
        super().__init(**kwargs)
        self.language = language
        self._separator = separator
        self.max_len = max_len
        #Load the appropriate model for the given language
        self._tokenizer = self._load_spacy_model(language)

    def load_spacy_model(self, language: str) -> Any:
        """
        Load the spaCy model for the given language.
        Parameters
        ----------
        language : str
        The language to load the model for.
        Returns
        -------
        Language
        The loaded spaCy model.
        """
       #Map the detected language to its full SpaCy model name
        language_model_map = {
           "en": "en_core_web_sm",
           "fr": "fr_core_news_sm",
           "de": "de_core_news_sm",
           "es": "es_core_news_sm",
           "it": "it_core_news_sm",
           "pt": "pt_core_news_sm",
           "nl": "nl_core_news_sm",
           "sv": "sv_core_news_sm",
           "da": "da_core_news_sm",
           "no": "no_core_news_sm",
           "fi": "fi_core_news_sm",
           "el": "el_core_news_sm",
           "hu": "hu_core_news_sm",
           "cs": "cs_core_news_sm",
           "sk": "sk_core_news_sm",
           "sl": "sl_core_news_sm",
           "ro": "ro_core_news_sm",
           "pl": "pl_core_news_sm",
           "hi:": "hi_core_web_sm",
           "te": "te_core_web_sm",
           "ta": "ta_core_web_sm",
           "mr": "mr_core_web_sm",
           "bn": "bn_core_web_sm",
           "gu": "gu_core_web_sm",
           "kn": "kn_core_web_sm",
           "ml": "ml_core_web_sm",
           "sa": "sa_core_web_sm",
           'xx': 'xx_ent_wiki_sm'

       }
    
        #Use the full model name if the langusge code is provided
        if language in language_model_map:
            pipeline = language_model_map[language]
            #Load the appropriate model for detected language
            tokenizer = spacy.load(pipeline,exclude=["ner","tagger"])
            tokenizer.max_length = self.max_length
        else:
            #fall to english if the language is not supported
            tokenizer = spacy.load("en_core_web_sm", exclude=["ner","tagger"])
            tokenizer.max_length  = self.max_length
        return tokenizer
    def split_text(self, text: str) -> List[str]:
        splits = (s.text for s in self._tokenizer(text).sents)
        return self._merge_splits(splits, self._separator)