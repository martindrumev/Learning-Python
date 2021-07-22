import pyaudio
import wave
import speech_recognition as sr

def play_aduio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()

def initSpeech():
    print("Listening...")

    play_aduio("./audio/pristine-609.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_aduio("./audio/open-ended-563.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you, bro")
    print("Your command:")
    print(command)

initSpeech()

