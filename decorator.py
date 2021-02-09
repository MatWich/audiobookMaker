class MessageDecorator:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[33m'
    OKRED = '\033[91m'
    OKGREY = '\33[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\33[5m'

    def err(self, text):
        if not self.is_string(text):
            print(self.OKRED + "Agrument \" text \" is not a string type" + self.ENDC)
            exit(-1)

        print(self.OKRED + text + self.ENDC)

    def created(self, text):
        if not self.is_string(text):
            print(self.OKRED + "Agrument \" text \" is not a string type" + self.ENDC)
            exit(-1)

        print(self.OKGREEN + text + self.ENDC)

    def dist(self, text):
        if not self.is_string(text):
            print(self.OKRED + "Agrument \" text \" is not a string type" + self.ENDC)
            exit(-1)

        print(self.BOLD + text + self.ENDC)

    def goodbye(self, text):
        if not self.is_string(text):
            print(self.OKRED + "Agrument \" text \" is not a string type" + self.ENDC)
            exit(-1)
        print(self.OKYELLOW + text + self.ENDC)

    def is_string(self, text):
        return True if isinstance(text, str) else False
