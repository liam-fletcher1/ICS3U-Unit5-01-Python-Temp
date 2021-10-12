#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program converts degrees celsius to farhrenheit


def fahrenheit():
    # convert user celsuis to farhrenheit

    # input
    user_temp = input("Enter a temperature (°C): ")
    print("")

    # process
    try:
        user_temp_int = int(user_temp)
        convert_far = (9 / 5) * user_temp_int + 32
        print("{0}°C is equal to {1}°F".format(user_temp_int, convert_far))

    except Exception:
        print("This is an invaild number!")

    finally:
        print("\nDone.")


def main():
    # this function just calls other functions

    # call finction
    fahrenheit()


if __name__ == "__main__":
    main()
