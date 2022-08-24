import requests

class TheTextAPI:
    MOST_POSITIVE_SENTENCES = "most_positive_sentences"
    MOST_NEGATIVE_SENTENCES = "most_negative_sentences"
    SUMMARIZE = "summarize"
    NER = "ner"
    MOST_COMMON_PHRASES = "most_common_phrases"
    LEAST_COMMON_PHRASES = "least_common_phrases"
    SIMILARITY_BY_SENTENCES = "similarity_by_sentences"
    SENTENCES_WITH_KEYWORDS = "sentences_with_keywords"
    POLARITY_BY_SENTENCE = "polarity_by_sentence"
    TEXT_POLARITY = "text_polarity"
    TEXT_API_ENDPOINT = "https://app.thetextapi.com/text/"

    # connection is if we want to pass in a connection object
    # useful for multiple requests and pooling
    def __init__(self, apikey: str = None, connection=None, **kwargs) -> str:
        if apikey:
            self.apikey = apikey
            self.headers = {
                "Content-Type": "application/json",
                "apikey": apikey
            }
        if connection:
            self.connection = connection
    
    def use_key(self, apikey: str):
        self.apikey=apikey
        self.headers = {
                "Content-Type": "application/json",
                "apikey": apikey
            }
    
    def load_text(self, text: str):
        self.text = text
    
    def _post_req(self, endpoint: str, **kwargs) -> str:
        body = {
            "text": self.text
        }
        for kw, arg in kwargs.items():
            body[kw] = arg
        res = requests.post(url=endpoint, headers=self.headers, json=body)
        return res.text

    def summarize(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        summarize_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.SUMMARIZE
        return self._post_req(summarize_url, **kwargs)
    
    def ner(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        ner_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.NER
        return self._post_req(ner_url, **kwargs)
    
    def most_common_phrases(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        most_common_phrases_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.MOST_COMMON_PHRASES   
        return self._post_req(most_common_phrases_url, **kwargs)
    
    def least_common_phrases(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        least_common_phrases_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.LEAST_COMMON_PHRASES
        return self._post_req(least_common_phrases_url, **kwargs)
    
    def similarity_by_sentences(self, texts: list, include_current_text: bool = True, **kwargs) -> str:
        # TODO: seems to trigger an error in the API itself, investigate and update
        # if include_current_text and hasattr(self, "text"):
        #     texts.append(self.text)
        similarity_by_sentences_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.SIMILARITY_BY_SENTENCES 
        body = {
            "texts": texts
        }
        for kw, arg in kwargs.items():
            body[kw] = arg
        res = requests.post(url=similarity_by_sentences_url, headers=self.headers, json=body)
        return res.text
    
    def most_positive_sentences(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        most_positive_sentences_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.MOST_POSITIVE_SENTENCES
        return self._post_req(most_positive_sentences_url, **kwargs)

    def most_negative_sentences(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        most_negative_sentences_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.MOST_NEGATIVE_SENTENCES
        return self._post_req(most_negative_sentences_url, **kwargs)
    
    def text_polarity(self, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        text_polarity_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.TEXT_POLARITY   
        return self._post_req(text_polarity_url, **kwargs)
    
    def polarity_by_sentence(self, text: str =None, **kwargs) -> str:
        if text:
            self.text = text
        polarity_by_sentence_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.POLARITY_BY_SENTENCE
        return self._post_req(polarity_by_sentence_url, **kwargs)
    
    def sentences_with_keywords(self, kws: list, text: str = None, **kwargs) -> str:
        if text:
            self.text = text
        sentences_with_keywords_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.SENTENCES_WITH_KEYWORDS
        return self._post_req(sentences_with_keywords_url, keywords = kws, **kwargs)
    
# TODO: implement Google
# TODO: implement Microsoft
# TODO: implement Amazon