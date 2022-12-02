import speech_recognition as sr

SAMPLE = sr.AudioFile(input('Путь к файлу: '))

NAME = input('введите имя файла: ')


def transliter(audio):
    with SAMPLE as file:
        recog = sr.Recognizer()
        audio_content = recog.record(file)
        trans = recog.recognize_google(audio_content, language='ru-RU')
        return trans


def wraiting():
    with open(NAME, 'w') as file:
        file.write(transliter(SAMPLE))



wraiting()
