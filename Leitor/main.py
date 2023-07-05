import pyttsx3

texto_fala = pyttsx3.init()

def falar(audio):
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate",170)
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice',voices[2].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

with open("Texto.txt", encoding="utf-8") as arquivo:
     texto = arquivo.read()
     falar(texto)