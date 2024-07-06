# states_of_america=["Delaware","Pennsylvania","Texas","Arizona","Wyoming"]
# print(states_of_america[2])#start from the beginning and count starts at 0
# print(states_of_america[-1])#start the count from the end
# states_of_america[1]="Pencilvania"
# print(states_of_america)
# states_of_america.append("unknown state")
# states_of_america.extend(["unknown state1","unknown state2","unknown state3"])
# print(states_of_america)
# print(len(states_of_america))
# print(states_of_america[1])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[0]) 
# print(dirty_dozen[1][1])

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put your treasure? Type abc and 123: ") # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
letter=position[0].lower()
abc=["a","b","c"]
letter_index=abc.index(letter)
number_index=int(position[1])-1
map[number_index][letter_index]='X'



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")