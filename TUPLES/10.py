# Check if two tuples are anagrams (same elements in different order).

my_tuples = ( 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 )
my_tuples_2 = ( 21 , 13 , 8 , 5 , 3 , 2 , 1 , 1 )

x=list(my_tuples)
y=list(my_tuples_2)

if (len(x) == len(y)):    
    for i in range(len(x)):
        if(y[i] in x):
            result = "Yes It Is Anagram"
        else:
            result = "No,It Is Not An Anagram"
else:
    result = "No It Is Not A Anagram"

print(result)