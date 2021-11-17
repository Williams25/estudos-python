class Maior:
    def __init__(self, * num):
        self.num = num
        self.maior_num = 0

    def maior(self):
        for i in self.num:
            print(i, end=" ")
            if i > self.maior_num:
                self.maior_num = i

        print(f"foram informados {len(self.num)} valores ao todo")
        print(f"o maior numero é {self.maior_num}")


Maior(10, 20, 2, 13).maior()
