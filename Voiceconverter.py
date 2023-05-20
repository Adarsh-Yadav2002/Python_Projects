import speech_recognition as s;

sr = s.Recognizer();
print("Bolo Prabhu aap kya kahana chahate hai  ??")
with s.Microphone() as m:
    audio = sr.listen(m)
    query = sr.recognize_goggle(audio, language="eng-in")
    print(query)