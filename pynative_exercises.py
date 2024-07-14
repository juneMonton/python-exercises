#given:
# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
num1=int(input("First number:"))
num2=int(input("Second number:"))
prod=num1*num2
sum=num1+num2
if prod<=1000:
    print(prod)
else:
    print(sum)
