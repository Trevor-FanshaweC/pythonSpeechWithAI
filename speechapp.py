import pyaudio, wave, subprocess
import speech_recognition as speechify
from commands import Controller

running = True

def say(text):
    subprocess.call('say ' + text, shell = True)

def play_audio(filename):
    chunk = 1024 #split our file into 1 meg chunks
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

mySpeech = speechify.Recognizer()
cntlr = Controller()

def initSpeech():
    print('Listening...')

    with speechify.Microphone() as source:
        play_audio("./audio/alert1.wav")
        print("Say something!")
        audio = mySpeech.listen(source)

    play_audio('./audio/alert2.wav')

    command = ""

    try:
        print('Trying speech recoginition service...')
        command = mySpeech.recognize_google(audio)        
    except:
        print("I didn't understand that. Could you try again?")

   # print("You said:", command)
    #say('You said: ' + command)

    if command in ["quit", "exit", "goodbye"]:
        global running
        running = False
    else:
        cntlr.discover(command)

while running == True:
    initSpeech()


#play_audio("./audio/alert2.wav")
