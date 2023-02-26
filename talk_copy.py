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


#text = (result["text"]) this is unimportant; it just gives us the entire text as string
timestamps = (result["segments"])
#segments contains the info about the split parts
#timestamps is a list of dictionaries
#now we want to extract all the values in timestamps assignes to the key "start"



from moviepy.editor import *

video = VideoFileClip("white.mp4")

textclipdict ={}

i=0
for item in timestamps:
    #textclipdict["text{0}".format(i)] = TextClip(item["text"], fontsize = 40).subclip(item["start"], item["end"])
    
    textclipdict["text{0}".format(i)] = TextClip(item["text"], fontsize = 10, font = "Nexa-Heavy").set_start(item["start"]).set_duration(item["end"] - item["start"]).set_position("center")
    
    i+=1
     #dictionary of all textclips


audio = AudioFileClip("speech.mp3")

#good:
merged = CompositeVideoClip([video, textclipdict["text0"], textclipdict["text1"], textclipdict["text2"], textclipdict["text3"], textclipdict["text4"]]).set_duration(audio.duration) #find a way to not have to list them like that

#merged = CompositeVideoClip([video, *textclipdict]).set_duration(audio.duration) #use all dictionary values as arguments python? #doesnt work yet..sumn like that, though

merged.audio = audio
merged.write_videofile("merged.mp4")

