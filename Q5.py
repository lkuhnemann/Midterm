# Write a function that finds all the occurrences of a certain pattern, that starts with “un” has unlimited number of letters and ends with “an”
# The function takes 1 parameter: the text to look into and returns the number of matches.
# Use only the things we have learned in class. Give some explanations besides the code.

def count_pattern_words(text):
    """
    Counts the number of words that start with "un" and end with "an" in the given text
    :param text: the input string to search
    :return: the amount of words that matach the pattern
    """

    punctuation = ",.?!<>+*'/-:;"
    for p in punctuation: #loop over each punctuation character
        text = text.replace(p, " ") #removes the punctuation and adds a space instead.

    words = text.split() #splits the modified text into a list of words
    count = 0 #starts the counter at 0

    for word in words: #loops through each word in the text
        if word.startswith("un") and word.endswith("an"): #checks if the word starts with un and ends with an
            count += 1 #increases the count by 1 if the word matches the criteria
        return count #returns the final count of words that follow the criteria