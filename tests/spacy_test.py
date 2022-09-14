from pynlpl.local.text.spacy import Spacy
# TODO: more accurate tests/better unit testing 

test_text = "PyNLP is the universal open source NLP library for Python. It is maintained by The Text API team."
model = Spacy()

# test for empty error
try:
    model.get_lemmas()
except Exception as e:
    # print(e)
    assert "No text" in str(e)

# test for update doc
model._update_doc(test_text)
assert hasattr(model, "doc")

# test for lemmas
lemmas = model.get_lemmas()
assert isinstance(lemmas, list) 

# test for pos
pos = model.get_parts_of_speech()
assert isinstance(lemmas, list) 

# test for ner
ner = model.extract_ner()
assert isinstance(lemmas, list) 

# test model change
model.change_model("en_core_web_sm")
assert model.nlp.meta['name'] == "core_web_sm"