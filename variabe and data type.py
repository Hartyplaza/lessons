#slicing strings
#name = "Hart bassey"
#first_name = name[0:4]
#last_name = name[5:]
#funcy_name = name[::3]
#reversed_name = name[::-1]
#print(first_name)
#print(last_name)
#print(funcy_name)
#print(reversed_name)


#using slic fuction
#website1 = "http://google.com"
#website2 = "http://wikipedia.com"

#slice = slice(7,-4)
#print(website1[slice])


#if statement = is a block of code the will execute if it's condition is true
#age = int(input("how old are you: "))
#if age > 30:
    #print("you are old enough")
#elif age < 3:
    #print("you havent been born yet")
#else:
    #print("you are a child")


#logical operators (and, or, not)
#used to check if two or more conditional if statement
#temp = int(input("what is the temperature outside?: "))
#if temp >= 0 and temp <= 30:
    #print("temperature is good today!")
    #print("go outside")
#elif temp < 0 or temp> 30:
    #print("temperature is hot today!")
    #print("stay inside")


 #while loop
#while 1 == 1:
    #print("i am stock here ")

    #for loop
#for i in range(10):
    #print(i)
#programe the simulate a count down
#import time
#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("wake up")


#nested loop
#row = int(input("how many rows: "))
#colums = int(input("how many colums: "))
#symbol = input("enter a symbol: ")
#for i in range(row): # outter loop
    #for j in range(colums): #inner loop
        #print(symbol, end="")#(end="") prevent cursor from moving down next line
    #print()

    #loop control statement
#while True: #break
    #name = input("enter a name: ")
    #if name != "":
        #break

        #continue
#phone_number = "16546-654-876"
#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end="")

    #pass == dose nothing it acts as a placeholder
#for i in range(1,13):
    #if i == 7:
        #pass
    #else:
        #print(i, end="")

        #list
#food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
#print(food[2]) #access element in a list
#food[2] = "rice" #change element in a list
#for x in food: # accessing all element in a list
    #print(x)

        #2D list
#drinks = ["coffee", "soda", "tea"]
#dinner = ["pizzer", "hamburger", "hotdog"]
#dessert = ["coke", "ice cream"]
#food = [drinks, dinner, dessert]
#print(food[0][2])

    #set
#utensile = {"fork", "spoon", "knife"}
#for x in utensile:
    #print(x)


        #indexing
#name = "hart bassey"
#if(name[0].islower()):
    #name = name.capitalize()
#print(name)
#first_name = name[0:4].upper()
#print(first_name)
#last_name = name[4:].upper()
#print(last_name)


            #FUCTIONS
#def hello():
    #print("hello hart")
    #print("have a nice day")

#hello()

#def hello(first_name, last_nmae, age):
    #print("hello " +first_name+" "+last_nmae)
   #print("you are "+str(age)+" years old")
    #print("have a nice day")

#hello("hart", "bassey", 21)

            #keyword argument
#def hello(first, last, age):
    #print("hello " + first + " " + last + "you are "+ age +" years old")


#hello(first="hart",last="bassy",age= str(21))


            #nested fuctions
#num = input("enter a whold positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#print(round(abs(float(input("enter a whole positive numbeer: ")))))


            #scope variable
#name = "bassey" #global scope (available inside and outside a fuction
#def display_name():
    #name = "hart"  #local scope (avalable only inside this fuction)
    #print(name)


#display_name()
#print(name)


            #*args
#def add(*args):
    #sum = 0
    #for i in args:
        #sum += i
    #return sum

#print(add(1,2,3,4,5,6,7,8,9))


#to change a value in *args, we change it to a list cauz args are tupls
#def add(*args):
    #sum = 0
    #args = list(args)
    #args[0] = 2
    #for i in args:
        #sum += i
    #return sum

#print(add(1,2,3,4,5,6,7,8,9))

            #**kwargs
#def hello(**kwargs):
    #print("hello " + kwargs['first'] + " " + kwargs['last'])

#hello(first="hart", middle="bassey", last="ofigwe")


#def hello(**kwargs):     #base on the amount of keyword psaaed using a for loop
    #print("hello",end=" ")
    #for key,value in kwargs.items():
        #(value,end=" ")

#hello(title="mr",first="hart", middle="bassey", last="ofigwe")

            #formate method
#animal = "cow"
#item = "moon"
#print("the {} jumped over the {}".format(animal,item))
#print("the {1} jumped over the {0}".format(animal,item))
#print("the {animal} jumped over the {item}".format(animal='cow',item='moon'))

#text = "the {} jumped over the {}"
#print(text.format(animal,item))

            #formatinf a number
#number = 3.14159
#print("the number pi is: {:.2f}".format(number)) #last two number after decimal
#number = 1000
#print("the number is {:,}".format(number)) #adding a comma
#print("{:b}".format(number))
#print("{:o}".format(number))


            #Random module
#import random
#x = random.randint(1,6)    #genarate a randon intiger
#print(x)


#y = random.random()     #generate a random floating number
#print(y)

#my_list = ['rock', 'paper', 'secissor']
#z = random.choice(my_list)
#print(z)

#cards = [1,3,5,4,6,5,"A","Q"]     #the shuffle method
#random.shuffle(cards)
#print(cards)


              #EXECEPTIONS


#import os
#path = "C:\\Users\\USER\\Desktop\\test.txt"

#if os.path.exists(path):
    #print("that location exist!")
#else:
    #print("location dosent exist!")



         #Reading files in python
#with open('text.txt') as file:
     #print(file.read())
    # print(file.closed)


    #writting a file in python
#book = "i'm a manchester united fan"
#with open('book.txt','a') as file:
    #file.write(book)import shutil


    #Copy files using python
#import shutil
#shutil.copy('book.txt','copy.txt')

            #moving a file

#import os
#source = "copy.txt"
#destinamtion = "C:\\Users\\USER\\Desktop\\text.txt"
#try:
    #if os.path.exists(destinamtion):
       # print("file already exist")
    #else:
       # os.replace(source,destinamtion)
       # print(source+ " was moved")
#except fileNotfoundError:
   # print(source+ "was not found")


            #delectig a file
#import os
#path = "text.txt"
#os.remove(path)


      #inheritance in python
#class Animal:     #the parent class

    #alive = True   #the class variable

    #def eat(self):
        #print("this animal is eating ")
    #def sleep(self):                               #methods
        #print("this animal is sleeping ")


#class rabbit(Animal):
    #def run(self):
       # print("this fish is running")
#class fish(Animal):       #the child class
    #def swim(self):
       # print("this fish is swimming")
#class hawk(Animal):
   # def fly(self):
        #print("this hawk is flying")

#rabbit = rabbit()
#Fish = fish()         #objects from the classes
#Hawk = hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.sleep()

#rabbit.run()
#Fish.swim()
#Hawk.fly()


                #METHOD CHANING
#class Car:

    #def turn_on(self):
      #  print("you ve start the engine")
       # return self

    #def drive(self):
       # print("you drive the car")
        #return self

   # def brake(self):
      #  print("you step on the brake")
      #  return self

    #def turn_off(self):
       # print("you turn off the engine")
        #return self

#car = Car()
#car.brake().drive().turn_off().turn_on()


                #ABSTRACT CLASS IN PYTHON
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

class motocycle(Vehicle):
    def go(self):
        print("you ride the motocycle")

vehicle = Vehicle()
car = Car()
motocycle = motocycle()

vehicle.go()
car.go()
motocycle.go()






