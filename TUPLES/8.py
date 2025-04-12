# Find the index of the first even number in a tuple.
my_tuples = ( 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 )

index=[]

for i in my_tuples:
    if(i % 2 == 0):
        index.append(i)


y=tuple(index)
print(y)