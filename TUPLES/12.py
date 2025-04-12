# Count frequency of elements in a tuple and store in a dictionary.

my_tuples = ( 1 , 1 , 2 , 3 , 5 , 4 , 1 , 3 , 2 , 1 )
my_dictionary = {}

for element in my_tuples:

    if element in my_dictionary:
        my_dictionary[element] += 1
    else:
        my_dictionary[element] = 1

print(my_dictionary)