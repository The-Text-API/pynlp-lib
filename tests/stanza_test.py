
import pytest

from pynlpl.local.text.stanza_text import Stanza_English_default

lang_model = Stanza_English_default()


text_for_testing = "PyNLP is the universal open source NLP library for Python. It is maintained by The Text API team."

def test_stanza_sentence_segementation():
  assert lang_model.sentence_segmentation(text_for_testing) == ["PyNLP is the universal open source NLP library for Python.", "It is maintained by The Text API team."]

def test_token_segmentation():
  assert lang_model.token_segmentation(text_for_testing) == ['PyNLP', 'is', 'the', 'universal', 'open', 'source', 'NLP', 'library', 'for', 'Python', '.', 'It', 'is', 'maintained', 'by', 'The', 'Text', 'API', 'team', '.']

def test_pos_tagging():
  assert lang_model.pos_tagging(text_for_testing) == ['WORD: PyNLP, UPOS: PROPN, XPOS: NNP', 'WORD: is, UPOS: AUX, XPOS: VBZ', 'WORD: the, UPOS: DET, XPOS: DT', 'WORD: universal, UPOS: ADJ, XPOS: JJ', 'WORD: open, UPOS: ADJ, XPOS: JJ', 'WORD: source, UPOS: NOUN, XPOS: NN', 'WORD: NLP, UPOS: NOUN, XPOS: NN', 'WORD: library, UPOS: NOUN, XPOS: NN', 'WORD: for, UPOS: ADP, XPOS: IN', 'WORD: Python, UPOS: PROPN, XPOS: NNP', 'WORD: ., UPOS: PUNCT, XPOS: .', 'WORD: It, UPOS: PRON, XPOS: PRP', 'WORD: is, UPOS: AUX, XPOS: VBZ', 'WORD: maintained, UPOS: VERB, XPOS: VBN', 'WORD: by, UPOS: ADP, XPOS: IN', 'WORD: The, UPOS: DET, XPOS: DT', 'WORD: Text, UPOS: PROPN, XPOS: NNP', 'WORD: API, UPOS: PROPN, XPOS: NNP', 'WORD: team, UPOS: NOUN, XPOS: NN', 'WORD: ., UPOS: PUNCT, XPOS: .']
