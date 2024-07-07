for number in range(1,11):#range doesn't include the 2nd variable
    print(number)

for number in range(1,11,3):#range doesn't include the 2nd variable, adding a step by 3
    print(number)

#calculate the sum of all the numbers from 1 to 100
total=0
for number in range(1,101):
    total+=number
print(total)

# You are going to write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100:

# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Also, we will constrain the inputs to only take numbers from 0 to a max of 1000.

target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
# even_sum=0
# for num in range(2,target+1,2):
# #   print(num)
#   even_sum+=num
# print(even_sum)

#alternative solution
alternative_sum=0
for num in range(1,target+1):
    if num%2==0:
        alternative_sum+=num
print (alternative_sum)