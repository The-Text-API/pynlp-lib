# PyNLP Lib (or PyNLPL, pronounced "pineapple")
PyNLP Lib is an open source Python Natural Language Processing library that provides functionality for both web and local development. It offers a wide range of functionality from text analysis to audio transcription to (planned) language generation. Also called "PyNLPL" (actually this was taken too), "PyNLP-L", "PyNLP-Lib", "PyNLPLib" (the official package name), or "PyNLP Library". This package would have been named PyNLP if that name wasn't taken by a third party wrapper library for Stanford NLP.

__*IF YOU ARE LOOKING FOR THE STANFORD NLP PACKAGE GO TO THE OFFICIAL STANFORD NLP PYTHON PACKAGE*__ - [Stanza](https://stanfordnlp.github.io/stanza/).

## PyNLP Lib README Navigation
- [PyNLP Library Installation](#pynlp-library-installation)
- [Usage for PyNLPL](#pynlp-l-usage)
- [External Docs for PyNLP-Lib Tooling](#external-documentation-for-pynlp-lib)
- [PyNLP-Lib Functionality](#pynlp-lib-functionality)
- [PyNLP-L module breakdown](#pynlp-l-module-breakdown)
- [PyNLP Lib Online/Web API Backends](#pynlp-lib-onlineweb-api-backends)
- [Local Backends for PyNLPL](#local-backends-for-pynlpl)
- [Roadmap for PyNLP Lib Development](#roadmap-for-pynlp-lib-development)
- [Timeline for PyNLP Lib so far](#timeline-for-pynlp-lib-development-so-far)

## PyNLP Library Installation
PyNLP-Lib can be installed from pip with the line

`pip install pynlp-lib`

## PyNLP-L Usage
EVEN THOUGH WE INSTALL PYNLP-LIB, WE MUST `import pynlpl`! DASHES ARE FORBIDDEN IN IMPORTS

The following code snippets assume you are using a `.env` file with your API keys for these online backends stored there under the shown keynames. (Deepgram key stored under `deepgram_key`, The Text API key stored under `textapi_key`)

Transcribing an Audio File on the Web with Deepgram:
```
from pynlpl.web import audio
from dotenv import load_dotenv
import os, asyncio, json

load_dotenv()
deepgram = audio.Deepgram(os.getenv("deepgram_key"))

async def main():
    # Initializes the Deepgram SDK
    # Open the audio file of https://www.youtube.com/watch?v=sQuFl0PSoXo
    # download with youtube_dl script, found on
    # github here: https://gist.github.com/ytang07/9b8317f268ffcf97cd47950aa7f94282 
    with open("./tests/Watch a professional software engineer live code a web scraper.mp3", 'rb') as audio:
        # ...or replace mimetype as appropriate
        source = {'buffer': audio, 'mimetype': 'audio/mp3'}
        response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
        print(json.dumps(response, indent=4))

asyncio.run(main())
```

Online Text Analysis with The Text API:
```
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
```

## External Documentation for PyNLP Lib
This section includes external documentation for the tools used in PyNLP Lib. 

### The Text API
Included in Beta

Resources:
* [Build an AI Text Summarizer](https://pythonalgos.com/build-your-own-ai-text-summarizer-in-python/)
* [Build an AI Content Moderation System](https://pythonalgos.com/how-to-build-an-ai-content-moderation-system/)
* [Text Sentiment Analysis](https://pythonalgos.com/text-sentiment-analysis-and-how-to-do-it/)
* [Best Way to do Named Entity Recognition (NER) Python](https://pythonalgos.com/the-best-way-to-do-named-entity-recognition-ner/)
* [NLP: What is Text Polarity?](https://pythonalgos.com/natural-language-processing-what-is-text-polarity/)
* [NLP Stop Words and How to Use Them](https://pythonalgos.com/nlp-stop-words-when-and-why-to-use-them/)

Example Projects:
* [What are the Most Common Phrases on YouTube?](https://pythonalgos.com/what-are-the-most-common-phrases-on-youtubes-front-page/)
* [Black Friday: How Does Twitter Feel?](https://pythonalgos.com/black-friday-how-does-twitter-feel/)
* [Using NLP to Analyze Obama Headlines](https://pythonalgos.com/ask-nlp-the-media-on-the-obama-presidency-over-time/)
* [Use NLP to get Insights from Twitter](https://pythonalgos.com/using-nlp-to-get-insights-from-twitter/)

### Deepgram
Included in Beta

Resources for the SDK:
* [Create Readable Transcripts for Your Podcasts](https://developers.deepgram.com/blog/2022/08/create-readable-transcripts-for-podcasts/)
* [Topic Detection](https://developers.deepgram.com/blog/2022/08/topic-detection-with-python/)

Example Projects:
* [Play the Piano with Your Voice](https://developers.deepgram.com/blog/2022/08/voice-controlled-music-with-python/)

### TorchAudio
Coming in 2023

Resources:
* [Local Speech Recognition with PyTorch TorchAudio](https://developers.deepgram.com/blog/2022/07/python-speech-recognition-locally-torchaudio/)

Example Projects:

### spaCy
Coming late 2022
### NLTK
Coming late 2022
### Stanford NLP/Stanza
Coming in 2023 (flex add)
### DeepSpeech
Coming late 2022

Resources:
* [DeepSpeech Local Speech Recognition](https://developers.deepgram.com/blog/2022/08/guide-deepspeech-speech-to-text/)

Example Projects:

### Microsoft Text
Coming in 2023
### Microsoft Audio
Coming in 2023
### Google Text
Coming in 2023
### Google Audio
Coming in 2023
### Amazon Text
Coming in 2023
### Amazon Audio
Coming in 2023

## PyNLP-Lib functionality
PyNLPL is the comprehensive module for NLP in Python. It is an open source NLP module with multiple backends. Currently, PyNLP Lib is maintained by the team at [The Text API](https://www.thetextapi.com). 

As of the August 2022 release, PyNLP Lib includes functionality for online text and audio processing. See [Roadmap](#roadmap-for-pynlp-lib-development) for planned future functionality. Ideally, we will add Natural Language Generation, Natural Language Understanding, Optical Character Recognition, and Conversational AI backends as well as additional backends for the existing text/audio features through 2023.

## PyNLP-L module breakdown
PyNLP Lib has two high level modules - `web` and `local`. The `web` module provides access to the web APIs that are used as the backend of PyNLPL. The `local` module provides access to tools that allow you to do NLP on your device.

Inside of the modules are individual backends. As of the beta release (0.1.0), the `web` backend contains `text` and `audio` submodules. Each of these submodules contain [classes](https://pythonalgos.com/the-simplest-way-to-get-started-with-python-classes/) for different backends. `web.text` currently has [The Text API](https://www.thetextapi.com) with future plans to extend to include Google, Amazon, and Microsoft Cloud products. `web.audio` currently has [Deepgram](https://www.deepgram.com) with future plans to extend to include Google, Amazon, and Microsoft Cloud products.

### PyNLP Lib Online/Web API Backends
Current online backends are Deepgram (audio) and The Text API (text)

Planned online backends include: Google Cloud, Azure, Microsoft

### Local Backends for PyNLPL
Local backends planned include: spaCy, NLTK, Stanford NLP, and Deepspeech

## Roadmap for PyNLP Lib Development
__This roadmap assumes no one helps add to this open source library! However, we'd LOVE help, so please feel free to contribute!__

* August 2022 - Initial Public Beta Release (0.1.0)
* September 2022 - Add Deepspeech for local audio transcription (0.2.0)
* October 2022 - Add spaCy backend for local text analysis (0.3.0)
* November 2022 - Add NLTK backend for local text analysis  (0.4.0)
* December 2022 - Add TorchAudio for local audio transcription (0.5.0)
* January 2023 - Add Google Cloud Natural Language AI for online text analysis (0.6.0)
* February 2023 - Add Azure Text Analysis for online Text Analysis (0.7.0)
* March 2023 - Add an online Translation API (0.8.0)
* April 2023 - Add Google Online Speech Transcription for audio transcription (0.9.0)
* May 2023 - Add an online Text Generation API (0.10.0)
* June 2023 - Add Amazon Transcribe for online audio transcription (0.11.0)
* July 2023 - Add an online Conversational AI API (0.12.0)
* August 2023 - Add an online OCR API, upgrade version for official release (1.0.0)

## Timeline for PyNLP Lib Development so far
* August 2022 - Initial Beta Release
