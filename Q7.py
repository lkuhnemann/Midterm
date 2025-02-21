# Here is some code:

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("original list: ", random_numbers)

modified_numbers = [] # creates a new list for the modified numbers

for num in random_numbers:
    if num > 80:
        modified_numbers.append(-num) #replaces numbers greater than 80 with their negative value
    elif num < 40:
        digit_sum = sum(int(digit) for digit in str(num)) #replaces numbers less than 40 with the sum of the digits. Converts the numbers to a string, splits them and then sums them
        modified_numbers.append(digit_sum)
    else:
        modified_numbers.append(num) # keeps the number unchanged if it does not match the conditions

print("Modified list: ", modified_numbers)
# continue here

# Continue by replacing the numbers greater than 80 with their corresponding negative value (90 will be replaced with -90).
# Also replace the number lower than 40 with the sum of their digits: 39 is replaced by 12.
# print the list at the end
# Use only what we have learned in class . Provide some explanation in the form of comments.

