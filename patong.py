import os
import webbrowser
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names())

def func_run():
    text = "ถ้าคุณต้องการค้นหา เว็ปไซต วิดีโอ แผนที่ หรือ รูปภาพ ให้พูดหัวข้อที่จะค้นหาตามนี้ "
    tts = gTTS(text,lang= "th")
    tts.save("0.mp3")
    playsound ("0.mp3")
    os.remove("0.mp3")

    with sr.AudioFile("translate_tts.wav") as source:
        print('|---> System: Waiting your voice.')
        audio = r.record(source)
        try:
            response = str(r.recognize_google(audio,language="th-TH"))
        except sr.RequestError as error:
            raise Exception('RequestError : '+error)
        except sr.UnknownValueError as error:
            raise Exception('UnknownValueError : could not understand audio')
        finally:
            print('|---> Microphone: '+response)
        if response.find("เว็บไซต์") != -1:
            print('|---> System: OK, you want you visit on wensite.')
            tts = gTTS ("โอเค ค้นหา เว็ปไซต กรุณาพูดคำที่จะค้นหา ",lang= "th")
            tts.save("0.mp3")
            playsound ("0.mp3")
            os.remove("0.mp3")
            try:
                # audio = r.record(source)
                response = str(r.recognize_google(audio,language="th-TH"))
                print('|---> Microphone: '+response)
                print('|---> System: Search wite this keyword '+ response)
                z = "https://www.google.co.th/search?q=" + response
                print('|---> System: Visit on '+ z)
                webbrowser.open(z)
            except sr.RequestError as error:
                raise Exception('RequestError : '+error)

if __name__ == "__main__":
    func_run()    