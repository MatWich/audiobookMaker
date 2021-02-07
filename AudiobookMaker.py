import pyttsx3 as mp3
import os
import time
import PyPDF2 as pdf
import random

class AudiobookMaker:
    def __init__(self, pathToPDFFile = None):
        self.pathToFile = pathToPDFFile
        # if False automaticly exits the program
        self.run = None
        # MP3
        self.engine = None

        # PDF
        self.pdfReader = None


        # List of possible options to choose from main menu
        self.possibleChoices = [0, 1, 2, 3, 4, 5, 6, 7]

        self.set_up()



    """Core of the program"""
    def set_up(self):
        if self.pathToFile is None or self.pathToFile[-4:] != '.pdf':
            print('Unable to reach pdf file')
            exit(0)
        self.get_name_of_the_file()

        self.engine = mp3.init()
        file = open(self.pathToFile, 'rb')
        self.pdfReader = pdf.PdfFileReader(file)
        self.engine.setProperty('rate', 125) # I think it is 1.0
        self.get_pdf_info()
        self.run = True

    def mainloop(self):
        while self.run:
            self.clear_console()
            self.draw_menu()
            selectedOption = int(input("Choose the number: "))
            self.option_handler(selectedOption)


    def draw_menu(self):
        #self.print_name_of_the_file()
        print(f"What would you like to do with {self.fileName} ?")
        print("1. Read whole file.")
        print("2. Read selected page")
        print("3. Create a mp3 file from the given one")
        print("4. Create an mp3 file from selected page")
        print("5. Change Voice")
        print("6. Change Volume")
        print("7. Change Rate")
        print("0. QUIT ")

    def option_handler(self, selectedOption):
        if selectedOption not in self.possibleChoices:
            self.clear_console()
            print(f"There is no option behind {selectedOption}")
            time.sleep(4.0)

        if selectedOption == 0:
            self.exit()
        elif selectedOption == 1:
            self.read_file()
        elif selectedOption == 2:
            self.read_page()
        elif selectedOption == 3:
            self.create_MP3_from_all()
        elif selectedOption == 4:
            self.create_MP3_from_page()
        elif selectedOption == 5:
            self.change_voice()
        elif selectedOption == 6:
            self.change_volume()
        elif selectedOption == 7:
            self.change_rate()
        else:
            pass


##################################### MENU OPTIONS #####################################
    def read_file(self):
        text = self.get_all_text_to_string()
        self.read_text(text)

    def read_page(self):
        page_num = int(input(f"Select page number from 0 - {self.pages - 1}: "))
        text = self.get_text_from_single_page(page_num)
        self.read_text(text)


    def create_MP3_from_all(self):
        text = self.get_all_text_to_string()
        self.save_to_MP3(text)


    def create_MP3_from_page(self):
        page_num = int(input(f"Select page number from 0 - {self.pages - 1}: "))
        text = self.get_text_from_single_page(page_num)
        self.save_to_MP3(text)

    def change_voice(self):
        self.clear_console()
        self.show_available_voices()
        choice = int(input("Choose voice: ")) - 1
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[choice].id)

    def change_volume(self):
        self.clear_console()
        print("Current volume: ", self.engine.getProperty('volume'))
        new_volume = float(input('Choose volume between 0 - 1'))
        if new_volume > 1 or new_volume < 0:
            print("In order to change volume you have to pick a number between 0 and 1")
            return
        self.engine.setProperty('volume', new_volume)



    def change_rate(self):
        self.clear_console()
        print("Current rate: ", self.engine.getProperty('rate'))
        new_rate = int(input('Choose a new voice rate'))
        self.engine.setProperty('rate', new_rate)

    # It is probably all what I need to make na audiobook
    def get_pdf_info(self):
        self.pages = self.pdfReader.numPages


##################################### END OF MENU OPTIONS #####################################

    def read_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

    def save_to_MP3(self, text='Error accured. But how is that possible?'):
        filename = "created" + str(self.generate_random_number()) + ".mp3"
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        self.engine.stop()
        self.clear_console()
        print('Succesfully created file: ' + filename)
        time.sleep(3.0)


    # helper func for read_file()
    def get_all_text_to_string(self):
        text = ""
        for page in range(self.pages):
            page = self.pdfReader.getPage(page)
            text += page.extractText()
        return text

    # helper func for read_page()
    def get_text_from_single_page(self, page):
        if not isinstance(page, int) or page >= self.pages:
            print("This PDF file doesn't have a page with this number")
            return

        page = self.pdfReader.getPage(page)
        text = page.extractText()
        return text

    def show_available_voices(self):
        voices = self.engine.getProperty('voices')
        for index, name in enumerate(voices):
            print(f"{index}. {name}")



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

    def generate_random_number(self):
        num = random.randint(20, 6958340)
        return num

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit(self):
        print('Until the next time')

        self.run = False
        exit(0)



