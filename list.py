my_list = []
my_list.extend([10,20,30,40])
my_list.insert(1, 15)
my_list.extend([50,60,70])
# Remove the last element from the list
my_list.pop()
my_list.sort()
# Find and print the index of the value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

print("Final list:", my_list)
