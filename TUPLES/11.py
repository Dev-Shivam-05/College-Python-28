# Find a pair of numbers in a tuple that add up to a target sum.

my_tuples = ( 1 , 2 , 3 , 4 , 5)

x = list(my_tuples)

for i in range(len(x)):
    for j in range(len(x)):
        if (x[i] + x[j] == 5):
            print(f"{x[i]} And {x[j]}")