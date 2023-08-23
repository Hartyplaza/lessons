class Car:
    #the __init__ fuction will construct object for use
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model    #Attributes of our car
        self.year = year
        self.color = color

    #object can have methods so we define the methods
    def drive(self):
        print("this car is driving")
    def stop(self):
        print("this car is stopped")