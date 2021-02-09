x = 123
y = "Abc"

def getLength(s):
    return len(s)


class Human():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def feed(self, f):
        self.weight = self.weight + f


h1 = Human("Alex", 70, 3.3)
h2 = Human("Bravo", 65, 4.3)

print(h1.name)
print(h1.weight)

h1.feed(3)


print(h1.weight)

h1.feed(4)

print(h1.weight)

## C Style

init_weight1 = 10

def increase_weight1(f):
    init_weight1 += f

init_weight2 = 13

def increae_weight2(f):
    init_weight2 += f

init_weight3 = 13

def increae_weight3(f):
    init_weight3 += f

increase_weight1(3)
increase_weight1(4)
increae_weight2(4)
increase_weight1(5)

# OOP

class Body_checker():
    def __init__(self, init_weight):
        self.init_weight = init_weight
    
    def increase_weight(self, f):
        self.init_weight += f

    
b1 = Body_checker(10)
b2 = Body_checker(13)
b3 = Body_checker(14)

b1.increase_weight(5)
b2.increase_weight(6)

