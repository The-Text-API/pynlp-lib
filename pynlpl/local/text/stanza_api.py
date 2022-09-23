
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
    import stanza
    stanza.download(lang='en')
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

  def pos_tagging(self, text = None):
    '''returns list of words and their part of speech tags'''
    self.__validate_text(text)
    return[f"WORD: {word.text}, UPOS: {word.upos}, XPOS: {word.xpos} " for word in self.document.iter_words()]

  def text_lemmatization(self, text = None):
    '''returns list of root words for text data'''
    self.__validate_text(text)
    return [
        f'WORD: {word.text}, LEMMA: {word.lemma} ' for sent in self.document.sentences
        for word in sent.words
    ]

  def dependency_parsing(self, text = None):
    '''returns list of ranking if tokens in text data'''
    self.__validate_text(text)
    return[f'ID: {word.id}, WORD: {word.text}, THREAD ID: {word.head}, THREAD: {sent.words[word.head-1].text if word.head > 0 else "root"}, DEPREL: {word.deprel} ' for sent in self.document.sentences for word in sent.words]
