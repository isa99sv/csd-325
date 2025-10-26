# Colton Stone, October 26, 2025, Module 1.3 Assignment

# I will be creating a program that counts backwards based on user input and displays the lyrics to a counting song in the output

class ZeroInputError(Exception):
    pass

def countdown(bottles, total):
    if bottles > 1:
        for bottles in range(bottles, 0, -1):
            print("\n" + str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer.")
            print("\n" + "Take one down and pass it around, " + str(bottles - 1) + " bottles of beer on the wall.")

        else:
            print("\n" + str(bottles) + " bottle of beer on the wall.")
            print("\n" + "Go to the store and buy some more, " + str(total) + " bottles of beer on the wall.")


while True:
    try:
        bottles = int(input("\nPlease enter the number of beer bottles that you have: "))
        total = bottles
        if bottles == 0:
            raise ZeroInputError("\nZero is an invalid input, only enter natural numbers ")

    except ZeroInputError as e:
        print(e)
    except ValueError as e:
        print(e)
        print("\nInvalid input, only enter numbers ")
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        countdown(bottles, total)
        break