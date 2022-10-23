import stanza

class Stanza_English_default():
  """Implements an abstracted version of the Stanza NLP library in English.

    Attributes
    ----------
    text: str
        The string object we want to analyze with Stanza NLP

    stanza_pipeline: str
        The name of the Stanza language model we want to use

    Methods
    ----------
    token_segmentation(text = None)
        split by tokens

    sentence_segmentation(text = None)
        no tokenization, text data is split by sentences only
    """
  def __init__(self, text: str = None, stanza_pipeline: str = 'en'):
    '''Initializes an English Stanza NLP language model, creates a document data object if text is passed'''
    self.nlp = stanza.Pipeline(stanza_pipeline)
    if text:
      self.document = self.nlp(text)

  def __validate_text(self, text):
        if text:
            self.document = self.nlp(text)
            return
        elif not self.document:
            raise Exception("No text found. Please provide a string.")


  def token_segmentation(self, text = None):
    '''segments by tokens. returns list of strings'''
    self.__validate_text(text)
    return[token.text for token in self.document.iter_tokens()]


  def sentence_segmentation(self, text = None):
    '''segments by sentences only. returns list of strings'''
    self.__validate_text(text)
    return[sentence.text for sentence in self.document.sentences]

  def pos_tagging(self, text = None, fine=False):
    '''returns list of words and their part of speech tags
    user can choose:
    fine grained / fine = True / returns treebank-specific POS tags
    course grained / fine = False / returns universal POS tags
    '''
    self.__validate_text(text)
    if not fine:
      return [f"WORD: {word.text}, UPOS: {word.upos}"for word in self.document.iter_words()]
    else:
      return[f"WORD: {word.text}, XPOS: {word.xpos}" for word in self.document.iter_words()]

  def text_lemmatization(self, text = None):
    '''returns list of root words for text data'''
    self.__validate_text(text)
    return [
        f'WORD: {word.text}, LEMMA: {word.lemma} ' for sent in self.document.sentences
        for word in sent.words
    ]

  def dependency_parsing(self, text = None):
    '''The “id” property will return its index in the sentence.
    Please note that this index is 1-based for the actual words in the sentence.
    The “thread id” property returns the id of the root (head) word in the sentence the current word is connected to.
    The “thread” property will returns the root word the current word is connected to.
    The “deprel” property (short for dependency relations) returns the relationship of the current word to the root word. '''
    self.__validate_text(text)
    return[f'ID: {word.id}, WORD: {word.text}, THREAD ID: {word.head}, THREAD: {sent.words[word.head-1].text if word.head > 0 else "root"}, DEPREL: {word.deprel} '
           for sent in self.document.sentences for word in sent.words]


  def ner_labeling(self, text = None, entities_only=True):
    '''returns list of labeled entities from text document
    user can choose:
    -- only entities displayed / entities_only = True / returns a list of only the recognized and labeled enitites
    -- every token/word displayed / entities_only = False / returns a list of every token in text document.
    Entities are corrently labeled with BIOES NER tags
    If the token is not an entity, a 0 is returned'''
    self.__validate_text(text)
    if entities_only:
      return[f'TOKEN: {ent.text} TYPE: {ent.type}' for sent in self.document.sentences for ent in sent.ents]
    else:
      return[f'TOKEN: {token.text} NER: {token.ner}' for sent in self.document.sentences for token in sent.tokens]


  def sentiment_analysis(self, text = None):
    '''returns 0 for negetive sentiment, 1 for neutral sentiment, and 2 for positive sentiment'''
    self.__validate_text(text)
    for sentence in self.document.sentences:
      return("Sentiment Analysis Value: %d" % (sentence.sentiment))
