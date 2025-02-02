name = input("Enter your name:")
age = int(input("Enter you age:"))

from datetime import datetime
current_age = datetime.now().year

turn_100_years = current_age + (100 - age)
print(f"Your name is {name} and your age is {age} you will turn 100 in {turn_100_years}.")