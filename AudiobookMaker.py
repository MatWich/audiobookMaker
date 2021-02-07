import pyttsx3 as mp3
import os
import time
import PyPDF2 as pdf

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
        self.get_pdf_info()
        text = self.get_all_text_to_string()
        self.read_text(text)

    def read_page(self):
        self.get_pdf_info()
        page = int(input(f"Select page number from 0 - {self.pages - 1}: "))
        text = self.get_text_from_single_page(page)
        self.read_text(text)


    def create_MP3_from_all(self):
        pass

    def create_MP3_from_page(self):
        pass

    def change_voice(self):
        pass

    def change_volume(self):
        pass

    def change_rate(self):
        pass

    def get_pdf_info(self):
        self.pages = self.pdfReader.numPages
        #print(self.pages)

##################################### END OF MENU OPTIONS #####################################

    def read_text(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

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



