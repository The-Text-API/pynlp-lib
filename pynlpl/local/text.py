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
    get_lemmas(text = None)

    """
    def __init__(self, text: str = None, spacy_model_name: str = 'en_core_web_sm'):
        '''Initializes a spaCy model, creates a doc if text is passed'''
        import spacy
        if not spacy.util.is_package(spacy_model_name):
            spacy.cli.download(spacy_model_name)
        self.nlp = spacy.load(spacy_model_name)
        if text:
            self.doc = self.nlp(text)

    def __validate_text(self, text):
        if text:
            self.doc = self.nlp(text)
            return
        elif not self.doc:
            raise Exception("No text found. Please provide a string.")

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
    

    
# TODO: implement NLTK
# TODO: implement Stanza