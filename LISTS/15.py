# Find the index of a given element using index() and print it.

my_list = []

size = int(input("Enter The Size Of List : "))

for i in range(size):
    x = input(f"Enter {i} Index Value : ")
    my_list.append(x)

print(my_list)

find = input("Which Value's Index Do You Want :")


index = my_list.index(find) 

print(index)