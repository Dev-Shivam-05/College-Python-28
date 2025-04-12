#Copy a list and show the difference between original and copied list

or_list = []

size = int(input("Enter The Size Of List : "))

for i in range(size):
    x = input(f"Enter {i} Index Value : ")
    or_list.append(x)

cpy_list = or_list.copy()
print(f"This is Copied List : {cpy_list}")

or_list = []

for i in range(size):
    x = input(f"Re-Enter {i} Index Value : ")
    or_list.append(x)

print(f"This Is Orignal List : {or_list}")

