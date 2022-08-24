from pynlpl.web import text
from dotenv import load_dotenv
import os

load_dotenv()
text_API = text.TheTextAPI(os.getenv("textapi_key"))

test_text = """The Text API is a comprehensive text processing and sentiment analysis API created by Yujian Tang. PyNLP-Lib or PyNLPL is an open source NLP library for Python. PyNLP-L aims to coalesce many different NLP backend tools and offer a high level API to use them. This test example shows how we can use the online text processing capabilities of PyNLP-L."""

def summarize_test():
    res = text_API.summarize(text=test_text)
    assert "most positive sentences" in res

def most_common_phrases_test():
    res = text_API.most_common_phrases(text=test_text)
    assert "most common phrases" in res

def least_common_phrases_test():
    res = text_API.least_common_phrases(text=test_text)
    assert "least common phrases" in res

def ner_test():
    res = text_API.ner(text=test_text)
    assert "ner" in res

def most_positive_sentences_test():
    res = text_API.most_positive_sentences(text=test_text)
    assert "most positive sentences" in res

def most_negative_sentences_test():
    res = text_API.most_negative_sentences(text=test_text)
    assert "most negative sentences" in res

def summarize_test():
    res = text_API.summarize(text=test_text)
    assert "summary" in res

def kw_test():
    res = text_API.sentences_with_keywords(kws =["PyNLP"], text=test_text)
    assert "\"PyNLP\":" in res

def similarity_by_sentences_test():
    res = text_API.similarity_by_sentences(texts=[test_text, test_text])
    assert any(x in res for x in ["doc1 cleaned", "doc2 cleaned", "repeat sentences"])

def test():
    summarize_test()
    kw_test()
    most_positive_sentences_test()
    most_negative_sentences_test()
    similarity_by_sentences_test()
    most_common_phrases_test()
    least_common_phrases_test()
    ner_test()

test()