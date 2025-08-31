"""
Tuples is a collection of items/values/elements
they are enclosed within the parenthesis or
open brackets() seperated by(,)
a tuples are immutable it mean we can't change
so when the data is fixed we can go with tuples
"""
#eg1:
mytuple=(13,12,11)
print(type(mytuple))
mytuple2=()
print(type(mytuple2))
mytuple3=(10)
print(type(mytuple3))
"""
NOTE:when you wanna create a tuple with single value
it should be seperated by so that the compiler
treats as tuple or else it just treats as integer
"""
#creation of tuple
#syntax: tuplevariable=(val1,val2,.....,valn)
mytuple4=(12,23,34,45+6j,[12,45],"hlo",(123,"ece"))
print(mytuple4)
mytuple5=(45,)
#creating a touple with a single element
mytuple6=(49,)
print(type (mytuple6))
#creating a tople with a list 
t=[34,56,"vv"]
print(t)
k=tuple(t)
print(k)
#creating the with "touple predefined word"
t=tuple#it consider as empty tuple
print(t)
#accesing the tuple in a list :
#using the index we can access 
#index syntax (start :stop)
mytuple8=(11,22,44,55,77,(78,89))
print(type(mytuple8))
print(mytuple8)
print(mytuple8 [2])
print(mytuple8[3])
mytuple9=([12,13,14],(89,90,78))
print(mytuple[1])
#slicing--it is used to retrive the element
#from a particular range the elements 
#syntax (start:stop:skip)
mytuple10=(11,12,33,44,55,77,88,99,"hello","agri","ece")
print (mytuple10[3:9:3])
mytuple11=(22,33,44,66,77,88,99,)
print(mytuple11[5:10:5])
mytuple12=("hello",123,456,45,34.45,56+76j,"ists","agri","ece", 345.9,"dept",12,23,34,67,90)
print(mytuple12[-1])
print(mytuple[7:-2:2])
#note:index are of two types
#1)positive indexing
#or
#forward indexing wich all are starts with zero from left hand side directions
#2)negative indexing 
#orbackward indexing which are starts with -1 from right hand direction 
#program
mytuple=(12,13,14,15(16,17,18)[12,13,14])
print((mytuple))
print(mytuple[2][1])
print((mytuple))

