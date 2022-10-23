
import pytest

from pynlpl.local.text.stanza_api import Stanza_English_default

lang_model = Stanza_English_default()


text_for_testing = "PyNLP is the universal open source NLP library for Python. It is maintained by The Text API team."

def test_stanza_sentence_segementation():
  assert lang_model.sentence_segmentation(text_for_testing) == ["PyNLP is the universal open source NLP library for Python.", "It is maintained by The Text API team."]

def test_token_segmentation():
  assert lang_model.token_segmentation(text_for_testing) == ['PyNLP', 'is', 'the', 'universal', 'open', 'source', 'NLP', 'library', 'for', 'Python', '.', 'It', 'is', 'maintained', 'by', 'The', 'Text', 'API', 'team', '.']

def test_pos_tagging():
  assert lang_model.pos_tagging(text_for_testing, fine=True) == ['WORD: PyNLP, XPOS: NNP', 'WORD: is, XPOS: VBZ', 'WORD: the, XPOS: DT', 'WORD: universal, XPOS: JJ', 'WORD: open, XPOS: JJ', 'WORD: source, XPOS: NN', 'WORD: NLP, XPOS: NN', 'WORD: library, XPOS: NN', 'WORD: for, XPOS: IN', 'WORD: Python, XPOS: NNP', 'WORD: ., XPOS: .', 'WORD: It, XPOS: PRP', 'WORD: is, XPOS: VBZ', 'WORD: maintained, XPOS: VBN', 'WORD: by, XPOS: IN', 'WORD: The, XPOS: DT', 'WORD: Text, XPOS: NNP', 'WORD: API, XPOS: NNP', 'WORD: team, XPOS: NN', 'WORD: ., XPOS: .']
  assert lang_model.pos_tagging(text_for_testing) == ['WORD: PyNLP, UPOS: PROPN', 'WORD: is, UPOS: AUX', 'WORD: the, UPOS: DET', 'WORD: universal, UPOS: ADJ', 'WORD: open, UPOS: ADJ', 'WORD: source, UPOS: NOUN', 'WORD: NLP, UPOS: NOUN', 'WORD: library, UPOS: NOUN', 'WORD: for, UPOS: ADP', 'WORD: Python, UPOS: PROPN', 'WORD: ., UPOS: PUNCT', 'WORD: It, UPOS: PRON', 'WORD: is, UPOS: AUX', 'WORD: maintained, UPOS: VERB', 'WORD: by, UPOS: ADP', 'WORD: The, UPOS: DET', 'WORD: Text, UPOS: PROPN', 'WORD: API, UPOS: PROPN', 'WORD: team, UPOS: NOUN', 'WORD: ., UPOS: PUNCT']

def test_text_lemmatization():
  assert lang_model.text_lemmatization(text_for_testing) == ['WORD: PyNLP, LEMMA: PyNLP ', 'WORD: is, LEMMA: be ', 'WORD: the, LEMMA: the ', 'WORD: universal, LEMMA: universal ', 'WORD: open, LEMMA: open ', 'WORD: source, LEMMA: source ', 'WORD: NLP, LEMMA: nlp ', 'WORD: library, LEMMA: library ', 'WORD: for, LEMMA: for ', 'WORD: Python, LEMMA: python ', 'WORD: ., LEMMA: . ', 'WORD: It, LEMMA: it ', 'WORD: is, LEMMA: be ', 'WORD: maintained, LEMMA: maintain ', 'WORD: by, LEMMA: by ', 'WORD: The, LEMMA: the ', 'WORD: Text, LEMMA: text ', 'WORD: API, LEMMA: api ', 'WORD: team, LEMMA: team ', 'WORD: ., LEMMA: . ']

def test_dependency_parsing():
  assert lang_model.dependency_parsing(text_for_testing) == ['ID: 1, WORD: PyNLP, THREAD ID: 8, THREAD: library, DEPREL: nsubj ', 'ID: 2, WORD: is, THREAD ID: 8, THREAD: library, DEPREL: cop ', 'ID: 3, WORD: the, THREAD ID: 8, THREAD: library, DEPREL: det ', 'ID: 4, WORD: universal, THREAD ID: 8, THREAD: library, DEPREL: amod ', 'ID: 5, WORD: open, THREAD ID: 8, THREAD: library, DEPREL: amod ', 'ID: 6, WORD: source, THREAD ID: 8, THREAD: library, DEPREL: compound ', 'ID: 7, WORD: NLP, THREAD ID: 8, THREAD: library, DEPREL: compound ', 'ID: 8, WORD: library, THREAD ID: 0, THREAD: root, DEPREL: root ', 'ID: 9, WORD: for, THREAD ID: 10, THREAD: Python, DEPREL: case ', 'ID: 10, WORD: Python, THREAD ID: 8, THREAD: library, DEPREL: nmod ', 'ID: 11, WORD: ., THREAD ID: 8, THREAD: library, DEPREL: punct ', 'ID: 1, WORD: It, THREAD ID: 3, THREAD: maintained, DEPREL: nsubj:pass ', 'ID: 2, WORD: is, THREAD ID: 3, THREAD: maintained, DEPREL: aux:pass ', 'ID: 3, WORD: maintained, THREAD ID: 0, THREAD: root, DEPREL: root ', 'ID: 4, WORD: by, THREAD ID: 8, THREAD: team, DEPREL: case ', 'ID: 5, WORD: The, THREAD ID: 8, THREAD: team, DEPREL: det ', 'ID: 6, WORD: Text, THREAD ID: 8, THREAD: team, DEPREL: compound ', 'ID: 7, WORD: API, THREAD ID: 8, THREAD: team, DEPREL: compound ', 'ID: 8, WORD: team, THREAD ID: 3, THREAD: maintained, DEPREL: obl ', 'ID: 9, WORD: ., THREAD ID: 3, THREAD: maintained, DEPREL: punct ']

def test_ner_labeling():
  assert lang_model.ner_labeling(text_for_testing) == ['TOKEN: PyNLP TYPE: ORG', 'TOKEN: NLP TYPE: ORG', 'TOKEN: Python TYPE: ORG', 'TOKEN: The Text API TYPE: ORG']
  assert lang_model.ner_labeling(text_for_testing, entities_only=False) == ['TOKEN: PyNLP NER: S-ORG', 'TOKEN: is NER: O', 'TOKEN: the NER: O', 'TOKEN: universal NER: O', 'TOKEN: open NER: O', 'TOKEN: source NER: O', 'TOKEN: NLP NER: S-ORG', 'TOKEN: library NER: O', 'TOKEN: for NER: O', 'TOKEN: Python NER: S-ORG', 'TOKEN: . NER: O', 'TOKEN: It NER: O', 'TOKEN: is NER: O', 'TOKEN: maintained NER: O', 'TOKEN: by NER: O', 'TOKEN: The NER: B-ORG', 'TOKEN: Text NER: I-ORG', 'TOKEN: API NER: E-ORG', 'TOKEN: team NER: O', 'TOKEN: . NER: O']

def test_sentiment_analysis():
  assert lang_model.sentiment_analysis(text_for_testing) == "Sentiment Analysis Value: 1"
