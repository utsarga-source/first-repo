#student details
""" name = "Shinigami"
age = 67
address = "koteshwore"
#Accurate format
print("I am " +name+" I am" +str(age)+" year old. I am located at "+address)
#f-string format
print(f"I am {name}.I am {age} year old. I am located at {address}")
#old format
print("I am %s.I am %d year old. I am located at %s"%(name,age, address))
#format new version method
print("I am {0}.I am {1} year old. I am located at {2}".format(name, age, address))

#type of data hold by variable
print(type(name))

#new shit
print("hello user ")
name = input("what is your name: ")
age = int(input("how old are you: "))
address = input("enter your location: ") 

print("Your name is " +name+ ". Your age is "+str(age)+". Your address is " +address)

#add sub and multiplying shit
num1 = input("enter the num1 ") #this creates an  error if we multiply or add it gives a gisult of 23 it the number entered is 2 and 3 
num2 = input("enter number 2 ")

num3 = int(input("enter a number 3 "))
num4 = int(input("enter a number 4 "))
sum1 =num1 + num2
print(f"the sum is {sum1} and type is {type(sum1)}")
sum2 =num3 + num4
print(f"the sum is {sum2} and type is {type(sum2)}")

"""
#shit walla shit and, or thing
print(6 and 5) 

print(1 and 0)
print(0 or "")
print(0 or 5)
print(5 or 0)
print