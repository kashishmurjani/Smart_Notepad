import NotePadFileModel
import speech_recognition as s

class File_Controller:
    def __init__(self):
        self.File_Model = NotePadFileModel.File_Model()

    def save_file(self, msg):
        self.File_Model.save_file(msg)

    def save_as(self, msg):
        self.File_Model.save_as(msg)

    def read_file(self, url=''):
        self.msg, self.base = self.File_Model.read_file(url)
        return self.msg, self.base

    def new_file(self):
        self.File_Model.new_file()

    def takeQuery(self):
        sr=s.Recognizer()
        print("Say something")
        with s.Microphone() as m:
            audio=sr.listen(m)
            text=sr.recognize_google(audio,language='en-IN')
            return text

