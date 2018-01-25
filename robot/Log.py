class Log:

    def __init__(self):
        # Opens and clears the file
        self.log = ""
        self.last_line = ""

    def write(self, text: str = ""):
        """Write a line to the log string but only if the new line differs from the previous"""
        if self.last_line is not text:
            self.log += text + "\n"
            self.last_line = text

    def read(self):
        """Return the log. Quite useless really"""
        return self.log

    def reset(self):
        """Reset the log"""
        self.log = ""
        self.last_line = ""


log = Log()
