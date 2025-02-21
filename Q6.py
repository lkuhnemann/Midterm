# Please explain what it means that a list is mutable and a string is not mutable (imutable).
# Give some code that shows the difference. Use your own words

# Lists are mutable because you can modify their elements, add/remove items after creation
# Strings are immuatable because once a string is created, you can't change its chartacters

#creating a list
my_list = [1, 2, 3]
print("Original list:", my_list)

#change element
my_list[0] = 99
print("Modified list:", my_list)

#create string
my_string = "lara"
print("Original string:", my_string)

#attempting to mutate the string (will cause an error)
try:
    my_string[0] = "c"
except TypeError as a:
    print("Modified string:", a)