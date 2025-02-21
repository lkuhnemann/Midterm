# Here is a function that determines if a number is palindrome or not:
def palindrome(word):
    word = str(word) #convert the input into a string
    if word == word[::-1]:
        return True
    else:
        return False

num= int(input("Enter a number "))
if palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")


# Which of the below is NOT a palindrome?
# a. "6892149109325320763773670235239019412986"
# b. "9847255590886266818998186626880955527489"
# c. "6800923757255865070000705685527573290086"
# d. "1414884937242655719669145562427394884141"