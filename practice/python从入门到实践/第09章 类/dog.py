class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

my_dog = Dog('wangying', 31)
my_dog1 = Dog('lihongbo', 29)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()
my_dog1.sit()
my_dog1.roll_over()

