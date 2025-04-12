# Perform union and update operations between two sets.
my_sets={1,'a',3,'n'}
my_sets_2={5,'h',7,"Thala"}


my_sets_3 = my_sets.union(my_sets_2)

print(my_sets_3)

my_sets_3.update({18,"Virat-Kholi"})

print(my_sets_3)