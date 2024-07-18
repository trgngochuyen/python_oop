class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.area = width * height

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area > other.area
        elif isinstance(other, (float, int)):
            return self.area > other
        else:
            raise ValueError(f"> is not supported between Rectangle and {other.__class__.__name__}")
        
r1 = Rectangle(3,5)
r2 = Rectangle(4,6)

if r1 > r2:
    print("r1 is bigger than r2")
else:
    print("r2 is bigger than r1")

if r1 > 5:
    print("it's a large rectangle")

if r1 > 'kjshfd':
    print('ok')