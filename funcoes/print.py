class Print:
    def __init__(self, msg):
        self.msg = msg
        self.length = len(self.msg)+4

    def escreva(self):
        print(f"~"*self.length)
        print(f"  {self.msg}")
        print(f"~"*self.length)


Print("Olá, Mundo!").escreva()
