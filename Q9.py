# Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how many days have passed since the day you were born (without counting the days in your birth year and the current year, so just whole years).
# The function takes your birthday as a parameter in string format.
# Do not import anything, use only what we learned in class

def days_since_birthday(birthday):
    """
    Calculates how many days have passed since the birth year (excluding birth and current year, but including leap years)
    :param birthday: a string in "DD-MM-YYYY" format
    :return: Number of days passed
    """

    #extract birth year from input string
    birth_year = int(birthday[-4:]) #last 4 characters represent the birth year

    #ask user for the current year
    current_year = int(input("Enter the current year: "))

    #Calculate whole years in between (excluding birth & current year)
    whole_years = current_year - birth_year - 1

    #count number of leap years in range
    leap_years = 0
    for year in range(birth_year + 1, current_year): #exclude birth & current year
        if (year %4 == 0 and year %100 !=0) or (year %400 == 0):
            leap_years += 1 #count leap years

    #count total days (365 days for a normal year and 366 days for a leap year)
    total_days = (whole_years * 365) + leap_years

    return total_days

#tell user to enter their birthday
birthday_input = input("Enter your birthday (DD-MM-YYYY): ")

#calculate and print the total days
print("Days passed:", days_since_birthday(birthday_input))
