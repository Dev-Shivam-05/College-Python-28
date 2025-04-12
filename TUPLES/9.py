# Swap two values in a tuple (e.g., first and third).

my_tuples = ( 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 )

y=list(my_tuples)

y[1] = y[1] + y[3]
y[3] = y[1] - y[3]
y[1] = y[1] - y[3]

x=tuple(y)

print(x)