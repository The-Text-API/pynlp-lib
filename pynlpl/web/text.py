import requests
import json

class TheTextAPI:
    """Implements an abstracted interface for The Text API. (https://www.thetextapi.com)

    Attributes
    ----------

    Methods
    ----------

    """

    MOST_POSITIVE_SENTENCES = "most_positive_sentences"
    MOST_POSITIVE_SENTENCES = "most_negative_sentences"
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
    def __init__(self, apikey: str = None, connection=None, **kwargs):
        '''Implements an abstracted version of The Text API
        
        Parameters:
        ----------
        apikey: str
            the API key from The Text API, can be added later

        connection: None (optional)
            connection pool for async requests
            TODO: optimize/refactor for clearer use

        **kwargs: 
            here for extensibility reasons lol

        Returns: an object to handle requests to The Text API

        '''

        if apikey:
            self.apikey = apikey
            self.headers = {
                "Content-Type": "application/json",
                "apikey": apikey
            }
        if connection:
            self.connection = connection
    
    def use_key(self, apikey: str):
        '''Updates the objects API key'''

        self.apikey=apikey
        self.headers = {
                "Content-Type": "application/json",
                "apikey": apikey
            }
    
    def load_text(self, text: str):
        '''Updates the objects stored text value'''

        self.text = text
    
    def _post_req(self, endpoint: str, **kwargs) -> json:
        '''Sends a standardized post request'''

        body = {
            "text": self.text
        }
        for kw, arg in kwargs.items():
            body[kw] = arg
        res = requests.post(url=endpoint, headers=self.headers, json=body)
        return json.loads(res.text)

    def summarize(self, text: str = None, **kwargs) -> json:
        '''Produces an extractive summary
        
        **kwargs:
            proportion: defaults to 0.3
            represents how much of the text we want to keep'''

        if text:
            self.text = text
        summarize_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.SUMMARIZE
        return self._post_req(summarize_url, **kwargs)
    
    def ner(self, text: str = None, **kwargs) -> json:
        '''Gets the Named Entities in a Text
        
        **kwargs:
            doctype: str, REVIEW and ARTICLE are accepted constants
            REVIEW is the default
            
            key_list: list of types of entities

        Note: doctype constant key lists are:
            REVIEW = ["ORG", "PERSON", "LOC", "DATE", "TIME", "MONEY", "EVENT"]
            ARTICLE = ["PERSON", "NORP", "ORG", "GPE", "LOC", "LAW", "DATE", "TIME", "MONEY"]
            '''
        if text:
            self.text = text
        ner_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.NER
        return self._post_req(ner_url, **kwargs)
    
    def most_common_phrases(self, text: str = None, **kwargs) -> json:
        '''Gets the most common phrases in a text
        
        **kwargs:
            num_phrases: int, defaults to 3
            Number of phrases you want to get'''

        if text:
            self.text = text
        most_common_phrases_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.MOST_COMMON_PHRASES   
        return self._post_req(most_common_phrases_url, **kwargs)
    
    def least_common_phrases(self, text: str = None, **kwargs) -> json:
        '''Gets the least common phrases in a text
        
        **kwargs:
            num_phrases: int, defaults to 3
            Number of phrases you want to get'''

        if text:
            self.text = text
        least_common_phrases_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.LEAST_COMMON_PHRASES
        return self._post_req(least_common_phrases_url, **kwargs)
    
    def similarity_by_sentences(self, texts: list, include_current_text: bool = True, **kwargs) -> json:
        '''Compares list of texts by sentence similarity'''

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
    
    def most_positive_sentences(self, text: str = None, **kwargs) -> json:
        '''Finds the most positive sentences

        **kwargs:
            num_sentences: int, defaults to 3
            Number of sentences you want to get'''

        if text:
            self.text = text
        most_positive_sentences_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.MOST_POSITIVE_SENTENCES
        return self._post_req(most_positive_sentences_url, **kwargs)

    def most_negative_sentences(self, text: str = None, **kwargs) -> json:
        '''Finds the most negative sentences

        **kwargs:
            num_sentences: int, defaults to 3
            Number of sentences you want to get'''

        if text:
            self.text = text
        most_negative_sentences_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.MOST_NEGATIVE_SENTENCES
        return self._post_req(most_negative_sentences_url, **kwargs)
    
    def text_polarity(self, text: str = None, **kwargs) -> json:
        '''Finds the polarity of the passed text'''

        if text:
            self.text = text
        text_polarity_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.TEXT_POLARITY   
        return self._post_req(text_polarity_url, **kwargs)
    
    def polarity_by_sentence(self, text: str =None, **kwargs) -> json:
        '''Returns sentences with marked polarity scores
        
        **kwargs:
            num_sentences: int, defaults to 3
            Number of sentences you want to get'''

        if text:
            self.text = text
        polarity_by_sentence_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.POLARITY_BY_SENTENCE
        return self._post_req(polarity_by_sentence_url, **kwargs)
    
    def sentences_with_keywords(self, kws: list, text: str = None, **kwargs) -> json:
        '''Returns all the sentences containing the passed in keywords
        
        **kwargs
            include_after: bool
            Should we include the sentence after the one with the keyword
            
            include_before: bool
            Should we include the sentence before the one with the keyword'''
        if text:
            self.text = text
        sentences_with_keywords_url = TheTextAPI.TEXT_API_ENDPOINT+TheTextAPI.SENTENCES_WITH_KEYWORDS
        return self._post_req(sentences_with_keywords_url, keywords = kws, **kwargs)
    
# TODO: implement Google
# TODO: implement Microsoft
# TODO: implement Amazon