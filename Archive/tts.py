import pyttsx3

engine = pyttsx3.init()
text = input("Hello, welcome what do you want to convert to speech to? : ")

engine.say(text)
engine.runAndWait

choice = str.lower(input("Do you want to save the text as an mp3? y/n: "))

if choice == 'y':
    name = str(input("File Name is: ")) + ".mp3"
    engine.save_to_file(text, name)
else:
    pass
