# Find all duplicate elements in a tuple.

my_tuples = ( 1 , 1 , 2 , 3 , 3 , 5 , 8 , 13 , 21 )

result = []
my_tuple = []

for i in my_tuples:
    if i not in result:
        result.append(i)
    else :
        my_tuple.append(i)

t=tuple(result)
print(t)