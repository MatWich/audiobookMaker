import pyttsx3 as mp3
import os

class AudiobookMaker:
    def __init__(self, pathToPDFFile = None):
        self.pathToFile = pathToPDFFile
        if self.pathToFile is None or self.pathToFile[-4:] != '.pdf':
            print('Unable to reach pdf file')
            exit(0)

        #self.engine = mp3.init()
        #self.run = True


