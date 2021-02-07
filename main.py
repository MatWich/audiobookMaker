from AudiobookMaker import AudiobookMaker
from os import path


if __name__ == '__main__':
    pa = path.dirname(__file__)
    readme = path.join(pa, "ANC.pdf")
    print(pa)
    print(readme[-4:])


    am = AudiobookMaker(readme)
    am.mainloop()
