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