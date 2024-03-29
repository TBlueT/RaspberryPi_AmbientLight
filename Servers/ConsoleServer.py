class ConsoleServer:
    def __init__(self):

        self.__output:bool = True

    @@property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        self.__output = value

    def shy(self, value):
        if self.output:
            print(value)