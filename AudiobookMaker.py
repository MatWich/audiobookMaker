import pyttsx3 as mp3
import os

class AudiobookMaker:
    def __init__(self, pathToPDFFile = None):
        self.pathToFile = pathToPDFFile
        self.set_up()

        # if False automaticly exits the program
        self.run = None
        self.engine = None



    def set_up(self):
        if self.pathToFile is None or self.pathToFile[-4:] != '.pdf':
            print('Unable to reach pdf file')
            exit(0)
        self.get_name_of_the_file()

        self.engine = mp3.init()
        self.run = True

    def mainloop(self):
        pass

    def draw_menu(self):
        self.print_name_of_the_file()
        print("1. Read whole file.")
        print("2. Read selected page")
        print("3. Create a mp3 file from the given one")
        print("4. Create an mp3 file from selected page")
        print("4. Change Voice")
        print("5. Change Volume")
        print("6. Change Rate")
        print("0. QUIT ")

    def option_handler(self, selectedOption):
        pass

    def get_name_of_the_file(self):
        self.fileName = ""
        i = 0
        while True:
            if self.pathToFile[-i] == '/' or self.pathToFile[-i] == '\\':
                break
            self.fileName = self.pathToFile[-i:]
            i += 1

    def print_name_of_the_file(self):
        print('Current File \"' + self.fileName + "\"")

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit(self):
        print('Until the next time')
        self.run = False
        exit(0)
