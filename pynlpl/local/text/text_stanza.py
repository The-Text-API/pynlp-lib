# TODO: implement Stanza





# TODO: implement Stanza
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
    tok_and_ssplit(text = None)
        default Stanza tokenization with sentence segmentation

    sentence_segmentation(text = None)
        no tokenization, text data is split by sentances only
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

  def tok_and_ssplit(self, text = None):
    self.__validate_text(text)
    for i, sentence in enumerate(self.document.sentences):
      print(f'-- tokens for sentence# {i+1} --')
      print(*[f'id: {token.id}\ttext: {token.text}' for token in sentence.tokens], sep='\n')


  def sentence_segmentation(self, text = None):
    '''segments by sentences only. returns list of strings'''
    self.__validate_text(text)
    return[sentence.text for sentence in self.document.sentences]


# text_for_testing = "Hey kitty girl. It's your world!"
# print(Stanza_English_default(text_for_testing).sentence_segmentation())
