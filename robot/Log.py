class Log:

    def __init__(self):
        # Opens and clears the file
        self.log = ""
        self.last_line = ""

    def write(self, text: str = ""):
        if self.last_line is not text:
            self.log += text + "\n"
            self.last_line = text

    def read(self):
        return self.log

    def reset(self):
        self.log = ""
        self.last_line = ""


log = Log()
