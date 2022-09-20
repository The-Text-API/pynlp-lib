
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
    ''''''
    self.__validate_text(text)
    return[f"WORD: {word.text}, UPOS: {word.upos}, XPOS: {word.xpos}" for word in self.document.iter_words()]




# text_for_testing = "PyNLP is the universal open source NLP library for Python. It is maintained by The Text API team."
# print(Stanza_English_default(text_for_testing).pos_tagging())
