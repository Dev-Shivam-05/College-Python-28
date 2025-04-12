#Append elements to a list dynamically using user input.

my_list = []

size = int(input("Enter The Size Of List : "))

for i in range(size):
    x = int(input(f"Enter {i} Index Value :"))
    my_list.append(x)
    
print(my_list)

