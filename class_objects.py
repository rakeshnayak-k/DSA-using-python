class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

class c1(Cookie):
    def __init__(self, name,color):
        super().__init__(color)
        self.name = name
    def get_name(self):
        return self.name
    

Cookie_1 = Cookie('green')
Cookie_2 = Cookie('red')
print(f"Cookie_1 Colrr: {Cookie_1.get_color()}")
print(f"Cookie_2 Colrr: {Cookie_2.get_color()}")

Cookie_1.set_color('Orange')
print(f"Cookie_1 Colrr: {Cookie_1.get_color()}")
print(f"Cookie_2 Colrr: {Cookie_2.get_color()}")

name = c1('Oreo','green')
Cookie_1 = Cookie('green')


print(name.get_name())
print(name.get_color())

