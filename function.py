# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


#Simple Function
# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

#Function that allows for input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print (f"How do you do {name}?")

# greet_with_name("June")

#parameter is like a variable
#the value is the argument the actual value of the data

#Functions with more than 1 input:

#Positional argument
# def greet_with(name,location): 
#     print (f"Hello {name}")
#     print (f"What is it like in {location}?")


# greet_with("June","Cebu")


#Keyword argument
def greet_with(name,location): 
    print (f"Hello {name}")
    print (f"What is it like in {location}?")


greet_with(location="Cebu",name="June")