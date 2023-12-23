######################################################################################################################
# Name: Satyendra Raj Singh
# Date: 12/16/2023
# Description: Simple class vechile program
######################################################################################################################

# the vehicle class
# a vehicle has a year, make, and model
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.year = 2000

#accesor syntax in python
#using the decorator in python
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self,maker):
        self._make = maker


    @property
    def model(self):
        return self._model

    @model.setter
    def model(self,model):
        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,year):
        if 2000<=year<=2018:
            self._year = year
        






# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
print("v1={} {}".format(v1.make, v1.model))
print("v2={} {}".format(v2.make, v2.model))
print()

v1.year = 2016
v2.year = 2016
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))
print()

v1.year = 1999
v2.model = "Civic"
v2.year = 2007
print("v1={} {} {}".format(v1.year, v1.make, v1.model))
print("v2={} {} {}".format(v2.year, v2.make, v2.model))

