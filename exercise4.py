class line:
    def __init__(self, length, x, y):
        self.length = length
        self.x = x
        self.y = y

    def draw(self):
        print("Drawing...")

    def display(self):
        print("Display...")

line1 = line(5,1,2)

print(line1.length)

line1.draw()

        