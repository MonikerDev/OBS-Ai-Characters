from google import genai
import speech_recognition as sr

from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

import AICharacter as Characters

import random

numBots = 5

conversationRounds = 10

def conversation():
    prompt = "discuss hit game amogus, try to keep it brief"
    conversation = prompt + "\n"
    yosukeResponse = "Yosuke said, \"" + Characters.respondToText(prompt, Characters.Yosuke()) + "\"\n"
    conversation += yosukeResponse
    lastThingSaid = yosukeResponse
    lastNumber = 1
    for i in range(conversationRounds):
            rng = random.randrange(0,100) % numBots
            while(lastNumber == rng):
                 rng = random.randrange(0,100) % numBots
            print(rng)
            if(rng == 0):
                fuukaResponse = "Fuuka said, \"" + Characters.respondToText(lastThingSaid, Characters.Fuuka()) + "\"\n"
                conversation += fuukaResponse
                lastThingSaid = fuukaResponse
                lastNumber = 0
            elif(rng == 1):
                yosukeResponse = "Yosuke said, \"" + Characters.respondToText(lastThingSaid, Characters.Yosuke()) + "\"\n"
                conversation += yosukeResponse
                lastThingSaid = yosukeResponse
                lastNumber = 1
            elif(rng == 2):
                morganaResponse = "Morgana said, \"" + Characters.respondToText(lastThingSaid, Characters.Morgana()) + "\"\n"
                conversation += morganaResponse
                lastThingSaid = morganaResponse
                lastNumber = 2
            elif(rng == 3):
                peterResponse = "Peter Grifin said, \"" + Characters.respondToText(lastThingSaid, Characters.PeterGriffin()) + "\"\n"
                conversation += peterResponse
                lastThingSaid = peterResponse
                lastNumber = 3
            elif(rng == 4):
                 imposterResponse = "Sus Imposter said, \"" + Characters.respondToText(lastThingSaid, Characters.SusImposter()) + "\"\n"
                 conversation += imposterResponse
                 lastThingSaid = imposterResponse
                 lastNumber = 4
    print(conversation)

conversation()