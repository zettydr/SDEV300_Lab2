"""This program uses multiple functions and helper functions to calculate
and return different calculations within an options menu. It allows the user
to generate a secure password, calculate percentages from a fraction,
calculate the days between the current date and july, 4th, 2025, calculate the law
of cosine of a triangle,and calculate the volume of a right cylinder.
 """

import string
import secrets
from datetime import datetime
import math


def generate_password(length=12):
    """Creates a password character format and uses the user input of length
    to generate the password a string."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def get_length():
    """Helper method to generate_password which returns
    the user input for password character length."""
    while True:
        try:
            length = int(input("Enter the desired password length (8 characters or greater): "))
            if length <= 7:
                print("Password length must be 8 characters or greater")
            else:
                return length
        except ValueError:
            # Validates that user input follows prompt guidelines
            print("Invalid input. Please enter a valid number")


def calculate_percentage():
    """Asks the user to inout a fraction and allows the user
    to select how many decimal places to be rounded.
    Calculates the decimal and converts it to a percentage"""
    while True:
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            decimal_points = int(input("Enter the number of decimal points for formatting: "))
            if denominator == 0:
                print("Denominator cannot be zero")
            else:
                # divides the numerator and denominator and multiples by 100
                percentage = (numerator / denominator) * 100
                formatted_percentage = f"{percentage:.{decimal_points}f}%"
                return f"{numerator} is {formatted_percentage} of {denominator}"
        except ValueError:
            # Validates that user input follows prompt guidelines
            print("Invalid input. Please enter valid numbers")


def days_til_july_4_2025():
    """Calculates the number of days between the current date and July 4th 2025
    using the datetime import function"""
    future_date = datetime(2025, 7, 4)
    current_day = datetime.today()
    # Subtracts the desired date from the current date and translates that to days
    days_remaining = (future_date - current_day).days
    return f"Days until July 4,2025: {days_remaining} days"


def get_side_length(side_name):
    """Retrieves the side name from law of cosines and
    prompts the user to input the side lengths"""
    while True:
        try:
            side = float(input(f"Enter the length of side '{side_name}': "))
            if side <= 0:
                print(f"Side '{side_name}' length must be greater than 0.")
            else:
                return side
        except ValueError:
            # Validates that user input follows prompt guidelines
            print("Invalid input. Please enter a valid number")


def law_of_cosines():
    """Retrieves the side lengths from get_side_length and uses those in collaboration
    with the angle of C to calculate the law of cosine """
    a = get_side_length('a')
    b = get_side_length('b')
    while True:
        try:
            angle_c = float(input("Enter the angle 'C' in degrees: "))
            c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle_c)))
            return f"The length of the third side is {c:.2f}"
        except ValueError:  # Validates that user input follows prompt guidelines
            print("Invalid input. Please enter a valid number for the angle")


def get_positive_number(prompt):
    """ Validates if the user entry is positive for the volume_right_cylinder function """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be a positive number")
            else:
                return value
        except ValueError:  # Validates that user input follows prompt guidelines
            print("Invalid input. Please enter a valid number")


def volume_right_cylinder():
    """Calculates the volume of a right cylinder using user inputs for the radius and height"""
    radius = get_positive_number("Enter the radius of the cylinder: ")
    height = get_positive_number("Enter the height of the cylinder:")
    volume = math.pi * radius ** 2 * height
    return f"Volume of the cylinder is {volume:.2f} cubic units"


def main():
    """Runs and generates the main options menu
    accounting for the user choice and pulling from the functions associated with each option """
    while True:
        print("Please select and input a letter from the list of options below: ")
        print("a. Generate Secure Password")
        print("b. Calculate and Format a Percentage")
        print("c. How many days from today until July 4,2025 ?")
        print("d. Use the Law of Cosines to calculate the leg of a triangle")
        print("e. Calculate the volume of a Right Circular Cylinder")
        print("f. exit program")

        user_choice = input("Please select a letter from the options menu")
        if user_choice == 'a':
            length = get_length()
            print("Generated password:", generate_password(length))
        elif user_choice == 'b':
            print(calculate_percentage())
        elif user_choice == 'c':
            print(days_til_july_4_2025())
        elif user_choice == 'd':
            print(law_of_cosines())
        elif user_choice == 'e':
            print(volume_right_cylinder())
        elif user_choice == 'f':
            print("Exiting program.")
            break
        else:  # Validates that user input follows prompt guidelines
            print("Invalid choice, please select a valid option.")


main()
