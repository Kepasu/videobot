from gtts import gTTS
import whisper


def saveaudio(input):
    tts = gTTS(input, lang = 'en', tld='com.au')
    tts.save("speech.mp3")


saveaudio("Scientists believe that with global warming, we can expect more severe weather patterns including heat waves, hurricanes, floods, and drought. The oceans may become more acid. Weather events like these can increase health risks, damage economies, destroy habitats, and affect our quality of life.")

model = whisper.load_model("base")
    #loading base model of whisper
result = model.transcribe("speech.mp3")
    #the task of transcribing the audio
    #this is a dictionary of lists dictionaries (or at least result["segments"] is a list of dictionaries)
    #dict keys: ['text', 'segments', 'language']

timestamps = (result["segments"])
#timestamps is a list of dictionaries
#now we want to extract all the values in timestamps assignes to the key "start"

for item in timestamps:
    #print(item.values())
    print(item["start"])
    #these are the starting points for our different subtitle segments
