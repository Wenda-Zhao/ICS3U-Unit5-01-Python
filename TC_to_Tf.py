#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program for TC to Tf


def fahrenheit():
    # This funtion is for TC to Tf

    # input

    TC = input("Enter the Celsius degree (integer): ")

    # process & output
    try:
        TC_int = int(TC)
        Tf = (9/5) * TC_int + 32
        print("{0}°C = {1}°F".format(TC_int, Tf))
    except Exception:
        print("It is not a integer")


def main():
    # this function just calls other functions

    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
