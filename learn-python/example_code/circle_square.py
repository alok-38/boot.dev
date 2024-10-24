class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("  ***  ")
        print(" *   * ")
        print("*     *")
        print(" *   * ")
        print("  ***  ")

class Square(Shape):
    def draw(self):
        print("*****")
        print("*   *")
        print("*   *")
        print("*****")

def draw_shape(shape: Shape):
    shape.draw()

if __name__ == "__main__":
    shapes = [Circle(), Square()]

    for shape in shapes:
        draw_shape(shape)
        print()

