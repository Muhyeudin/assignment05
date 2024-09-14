# Function to check if a number is even or odd, and positive, negative, or zero
def check_number(num):
    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")
    
    # Check if the number is positive, negative, or zero
    if num > 0:
        print(f"{num} is Positive.")
    elif num < 0:
        print(f"{num} is Negative.")
    else:
        print(f"{num} is Zero.")

# Main program
# Input a number from the user
number = float(input("Enter a number: "))

# Call the function to check the number
check_number(number)

# ===============================================

# Function to check divisibility by 2 and 3
def check_divisibility(num):
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3.")
    elif num % 2 == 0:
        print(f"{num} is divisible by 2 but not by 3.")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3 but not by 2.")
    else:
        print(f"{num} is not divisible by either 2 or 3.")

# Function to check voting eligibility
def check_voting_eligibility(age):
    if age >= 18:
        nationality = input("Do you have Pakistani nationality? (yes/no): ").strip().lower()
        if nationality == "yes":
            print("You are eligible to vote.")
        else:
            print("Please obtain a valid ID to vote.")
    else:
        print("You are not eligible to vote yet.")

# Main program
# Input a number from the user for divisibility check
number = int(input("Enter a number: "))
check_divisibility(number)

# Input age from the user to check voting eligibility
age = int(input("Enter your age: "))
check_voting_eligibility(age)
#=================================================

# Function to determine the age group
def determine_age_group(age):
    if 0 <= age <= 12:
        print("You are a Child.")
    elif 13 <= age <= 19:
        print("You are a Teenager.")
    elif 20 <= age <= 59:
        print("You are an Adult.")
    elif age >= 60:
        print("You are a Senior Citizen.")
    else:
        print("Invalid age entered.")

# Function to print the number of days in a month
def days_in_month(month):
    # Dictionary mapping month number to the number of days
    days_in_month_dict = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month in days_in_month_dict:
        print(f"Month {month} has {days_in_month_dict[month]} days.")
    else:
        print("Invalid month entered. Please enter a number between 1 and 12.")

# Function to check if a year is a leap year or not
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# Main program

# 1. Input age and determine age group
age = int(input("Enter your age: "))
determine_age_group(age)

# 2. Input month number and print the number of days
month = int(input("Enter a month (1-12): "))
days_in_month(month)

# 3. Input a year and check if it's a leap year
year = int(input("Enter a year: "))
check_leap_year(year)

