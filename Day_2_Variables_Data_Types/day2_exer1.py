import datetime  # 1. Exercise - Age 100

#
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year

ask_name = input('What is your name ? ')
user_age = input(f'{ask_name}, how old you are? ')
import datetime

current_year = datetime.datetime.now().year

age = int(user_age)

hundred = int(current_year - age) + 100

print(f'{ask_name} in {hundred} you will be 100 years old!')


