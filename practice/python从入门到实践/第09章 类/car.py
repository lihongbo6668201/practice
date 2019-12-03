class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.lic = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name)
        return long_name.title()

    def update_lic(self, lic ):
        self.lic = lic

    def read_lic(self):
        print('This car is ' + str(self.lic) + ' lic.')

my_car = Car('audi', 'a4', 1998)
print(my_car.get_descriptive_name())
my_car.update_lic(23)
my_car.read_lic()
