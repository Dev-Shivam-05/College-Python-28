# Remove all vowels from a string using a set.

string = input("ENter A Number : ")
vowels = {'a','e','i','o','u'}
result=""

for i in range(len(string)):
    if (string[i] not in vowels):
        result += string[i]

        print(result)
