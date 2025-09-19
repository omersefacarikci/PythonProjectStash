import pyttsx3

engine = pyttsx3.init()

text = input("Sesli okunmasını istediğiniz metni girin: ")

engine.say(text)
engine.runAndWait()

print("Metin başarıyla seslendirildi!")
