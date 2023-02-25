from pyChatGPT import ChatGPT
import requests

import configparser

from keywords import getkeywords

from talk import saveaudio

import whisper

config = configparser.ConfigParser()
config.read('config.ini')


token = config['KEYS']['cgpt_sessionid']
api = ChatGPT(token)

def ask(prompt):
    #function to send prompt to ChatGPT and returns its answer
    scriptdict = api.send_message(prompt)
    #this gives a dictionary: <class 'dict'>; keys are: dict_keys(['message', 'conversation_id']) (maybe that convrsation coule be useful at some point)
    return scriptdict['message']
    #this now is a <class 'str'>

scripttask = "write 120 words on a interesting history fact, starting with an attention grabber. emphasize an exciting writing style, truly focusing on guarding the listeners short attention span"
#to be used as prompt/argument in following line

script = ask(scripttask)
#saves chatgpts str answer under "script"

#plan now: generate an emphatic tts and then use whisper to work on subtitles (see ipad photos)

"""

keywords = getkeywords(script)
#calls getkeywords function from keywords.py and returns a set
print(keywords)

"""

saveaudio(script)

model = whisper.load_model("base")
#loading base model of whisper

result = model.transcribe("speech.mp3")
#the task of transcribing the audio 

print(result)