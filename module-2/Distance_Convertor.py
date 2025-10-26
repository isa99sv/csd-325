# Colton Stone, August 28 2025, Module 4.2 Assignment

# The purpose of this program is to receive an inputted number from the user and then convert it to kilometers.


# This exception stops the user from entering zero as input.

class ZeroInputError (Exception):
    pass


def distance_convertor():
    mi_total_distance = miles_driven
    km_total_distance = mi_total_distance * 1.609344
    print("\nYou have driven for a total of " + str(mi_total_distance) + " miles or " + str(km_total_distance)  + " kilometers.")


# In the code below the exception blocks will check the users' input and then return errors if an invalid input
# such as a character or symbol is entered instead of a number.
# And the "while True" condition creates a while loop that will repeat infinitely until the user enters a valid number.

while True:
    try:
        miles_driven = float(input("\nEnter the number of miles that you have driven: "))
        if miles_driven == 0:
            raise ZeroInputError("\nZero is not valid input, try again and only enter natural numbers")

    except ZeroInputError as e:
        print(e)
    except ValueError as e:
        print(e)
        print("\nInvalid input, try again and only enter numbers")
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
        print("\nAn error was made in your input")
    else:
        distance_convertor()
        break




