#!/usr/bin/env python3\
# Created By:Kamche
# Created on: October 27, 2026
# This program asks the grandparents to ask the user
# for an approved age to date
# and checks if it is a valid integer or not
import constants


def main():
    # get the user dating age as a string
    user_age_str = input("Enter your dating age : ")
    print("")

    try:
        # cast the user dating age to an integer
        user_age_int = int(user_age_str)

        # check if it is valid or not
        if user_age_int > constants.MIN and user_age_int < constants.MAX:
            print("You can date my grandaugther")
        elif user_age_int < 0:
            print("This is a valid integer, but not a real number to date.")
        elif user_age_int <= constants.MIN and user_age_int >= 0:
            print("You are too young to adte my grandaugther")
            print("We do not approve this relationship")
        elif user_age_int >= constants.MAX:
            print("You are too old to date my grandaughter")
            print("We do not approve this relationship")
    except ValueError:
        print("{} is not an integer".format(user_age_str))
    finally:
        print("Thank you for your interest")


if __name__ == "__main__":
    main()
