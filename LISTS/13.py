# Use pop() to remove and display the last item

my_list = []

size = int(input("Enter The Size Of List : "))

for i in range(size):
    x = input(f"Enter {i} Index Value : ")
    my_list.append(x)

print(f"Orignal List Is : {my_list}")

my_list.sort()

print(f"Acending Order List Is : {my_list}")

my_list.reverse()

print(f"Decending Order List Is : {my_list}")
