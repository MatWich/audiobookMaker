from AudiobookMaker import AudiobookMaker
from os import path


if __name__ == '__main__':
    pa = path.dirname(__file__)
    readme = path.join(pa, "costam.pdf")
    print(pa)
    print(readme[-4:])
    am = AudiobookMaker(readme)
    am.clear_console()
    am.draw_menu()
