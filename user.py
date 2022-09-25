
class Car:
    def __init__(self,model = None, color = None):
        self.model = model
        self.color = color

    def Show(self):
        print("Hello")
        print("Model is", self.model)
        print("Color is", self.color)


#if __name__ == "__main__":
ferrari = Car("Audi", "blue")
Bmw = Car("BMW", "white")
Blank = Car()
ferrari.Show()
Bmw.Show()
Blank.Show()


    #rect = Rectangle(10)
    #print(rect.Area())
# addig the comment here
# TOD0 : add proper list here
