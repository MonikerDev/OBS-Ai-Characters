from google import genai
from google.genai import types

import PIL.Image
from PIL import ImageGrab
from PIL import ImageFile

import speech_recognition as sr

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

ElevenLabsAPIKey = 'Your API Key here'
GeminiAPIKey = 'Your API Key here'

class AICharacter:
    def __init__(self, name, voiceID, prompt):
        self.name = name
        self.voiceID = voiceID
        self.prompt = prompt

def ExampleCharacter():
    return AICharacter('Example Name', 'ElevenLabs Voice ID', 'Character Prompt')

#Listens to default audio input for 10 seconds and responds
def RespondToMic(character: AICharacter):
    client = ElevenLabs(
        api_key= ElevenLabsAPIKey
    )
    writerClient = genai.Client(
        api_key = GeminiAPIKey
    )
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source, 10 , 6)
        print("Time over, thanks")
        try:
            # using google speech recognition
            audio_text = r.recognize_google(audio_text)
        except:
            print("Failed to get text")
            audio_text = "Talk about the lack of a prompt"
    response = writerClient.models.generate_content(
        model="gemini-2.0-flash", contents=character.prompt + "Respond to the following text." + audio_text 
    )
    print(response.text)
    audio = client.text_to_speech.convert(
        text=response.text,
        voice_id=character.voiceID,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    play(audio)
    print("Audio is done playing")

#Responds to given text prompt
def respondToText(text: str, character: AICharacter):
    client = ElevenLabs(
     api_key= ElevenLabsAPIKey
    )
    writerClient = genai.Client(
        api_key = GeminiAPIKey
        )
    # Initialize recognizer class (for recognizing the speech)
    response = writerClient.models.generate_content(
        model="gemini-2.0-flash", contents=character.prompt + "Respond to the following text." + text
    )
    print(response.text)
    audio = client.text_to_speech.convert(
        text=response.text,
        voice_id=character.voiceID,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    play(audio)
    return response.text

#Responds to current content on screen
def respondToImage(image: ImageFile, character: AICharacter):
    client = ElevenLabs(
     api_key= ElevenLabsAPIKey
    )
    writerClient = genai.Client(
        api_key = GeminiAPIKey
        )
    response = writerClient.models.generate_content(
        model="gemini-2.0-flash",
        contents=[character.prompt + "What are your thoughts about this image", image]
    )
    print(response.text)
    audio = client.text_to_speech.convert(
        text=response.text,
        voice_id=character.voiceID,
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )
    play(audio)
