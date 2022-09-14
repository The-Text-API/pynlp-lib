import spacy

# TODO: implement spaCy
class Spacy():
    """Implements an abstracted version of spaCy's API.
    
    Attributes
    ----------
    text: str
        The string object we want to analyze with spaCy
    
    spacy_model_name: str
        The name of the spaCy model we want to use

    Methods
    ----------
    __validate_text(text)
        Ensures that there is text to process or raises an Exception

    _update_doc(text)
        Updates the document object
        Note: is anyone ever going to use this? idk, we'll see   

    change_model(model_name)
        Changes the spaCy model we use

    get_lemmas(text = None)
        Returns a list of lemmas of each word

    get_parts_of_speech(text = None, fine = False)
        Returns a list of tuples of (word, part of speech)

    extract_ner(text = None)
        Returns a list of tuples of (word, entity tag)

    """
    
    def __init__(self, text: str = None, spacy_model_name: str = 'en_core_web_sm'):
        '''Initializes a spaCy model, creates a doc if text is passed'''
        if not spacy.util.is_package(spacy_model_name):
            spacy.cli.download(spacy_model_name)
        self.nlp = spacy.load(spacy_model_name)
        if text:
            self.doc = self.nlp(text)

    def __validate_text(self, text):
        '''Validates that there is text in the pipeline to process'''

        if text:
            self.doc = self.nlp(text)
            return
        elif not hasattr(self, "doc"):
            raise Exception("No text found. Please provide a string.")
    
    def _update_doc(self, text):
        '''Updates the text doc'''

        self.doc = self.nlp(text)

    def change_model(self, spacy_model_name):
        '''Changes the spaCy model we are using'''

        if not spacy.util.is_package(spacy_model_name):
            spacy.cli.download(spacy_model_name)
        self.nlp = spacy.load(spacy_model_name)

    def get_lemmas(self, text = None):
        '''Return a list of lemmas for each word in the text'''

        self.__validate_text(text)
        return [token.lemma_ for token in self.doc]

    # fine = fine grained
    def get_parts_of_speech(self, text = None, fine = False):
        '''Returns a list of tuples of the word and its part of speech,
         allows for fine-grained POS tagging'''

        self.__validate_text(text)
        if not fine:
            return [(token.text, token.pos_) for token in self.doc]
        else:
            return [(token.text, token.tag_) for token in self.doc]
    
    def extract_ner(self, text = None):
        '''Returns a list of tuples of the entity and its category'''

        self.__validate_text(text)
        return [(token.text, token.label_) for token in self.doc.ents]

