# TODO: implement spaCy
class Spacy():
    def __init__(self, text = None, spacy_model_name = 'en_core_web_sm'):
        import spacy
        if not spacy.util.is_package(spacy_model_name):
            spacy.cli.download(spacy_model_name)
        self.nlp = spacy.load(spacy_model_name)
        if text:
            self.doc = self.nlp(text)

    def get_lemmas(self, text = None):
        if text:
            self.doc = self.nlp(text)
        return [token.lemma_ for token in self.doc]

    # fine = fine grained
    def get_parts_of_speech(self, text = None, fine = False):
        if text:
            self.doc = self.nlp(text)
        if not fine:
            return [token.pos_ for token in self.doc]
        else:
            return [token.tag_ for token in self.doc]
    
# TODO: implement NLTK
# TODO: implement Stanza