class Dog():
    pass

my_dog = Dog()
print(type(my_dog))

class Dog():
    def __init__(self,breed):
        self.breed = breed

my_dog = Dog(breed = "Golden Retriever")
print(my_dog.breed)

print("\n--------------------\n")

class Dog():
    species = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog('Husky','Simba',True)
print(my_dog.species)

print("\n--------------------\n")

class Dog():
    species = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    def bark(self):
        print("Woof!")

my_dog = Dog('Husky','Simba',True)
my_dog.bark()

print("\n--------------------\n")

class Dog():
    species = 'mammal'
    def __init__(self,breed,name,spots):
        self.breed = breed
        self.name = name
        self.spots = spots
    
    def bark(self,number):
        print(f"Woof! My name is {self.name}, number = {number}")

my_dog = Dog('Husky','Simba',True)
my_dog.bark(3)

print("\n--------------------\n")

class Circle():
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = Circle.pi*radius*radius

    def get_circumfrence(self):
        return 2*Circle.pi*self.radius
    
my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumfrence())

print("\n--------------------\n")

class Animal():
    def __init__(self):
        print("Animal Created")
    
    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    
    def who_am_i(self):
        print("I am a dog")

mydog = Dog()
mydog.eat()
mydog.who_am_i()

print("\n--------------------\n")

class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' says meow!'
    
simba = Dog("Simba")
Felix = Cat("Felix")

print(simba.speak())
print(Felix.speak())

print("\n--------------------\n")

# class Sample():
#     pass

# mysample = Sample()
# print(len(mysample))
# print(mysample)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages


b = Book('Python','The Silent Defender',200)
print(b)
print(len(b))