# Count how many times a number appears in a list

my_list = []

size = int(input("Enter The Size Of List : "))

for i in range(size):
    x = int(input(f"Enter {i} Index Value : "))
    my_list.append(x)

print(f"This Is The Inputed List : {my_list}")

appear_num = int(input("Enter A Value To Check : "))

appearnce = my_list.count(appear_num)

print(appearnce)

