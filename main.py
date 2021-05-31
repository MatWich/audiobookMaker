from AudiobookMaker import AudiobookMaker
import os
from os import path


def main():
    pa = path.dirname(__file__)
    PATH = path.join(pa, "pdfs")
    file_list = os.listdir(PATH)
    for index, file in enumerate(file_list):
        print(f"{index}. {file}")

    choice = int(input('Choose a .pdf file from the list or first add some to the directory:'))
    file_name = file_list[choice]
    readme = path.join(PATH, file_name)
    am = AudiobookMaker(readme)
    am.mainloop()


if __name__ == '__main__':
    main()

