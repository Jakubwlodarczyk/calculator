#!/usr/bin/python3
import sys

def pytanie():
    print("Enter first number(or letter to exit): ")
    numer = input()
    if numer.isdigit():
        return numer
    else :
        exit()


def operator(numer1):
    print("Enter an operation (+,-,*,/):")
    operation = input()
    if operation == "+":
        return dodawanie(numer1)
    elif operation == "-":
        return odejmowanie(numer1)
    elif operation == "*":
        return mnozenie(numer1)
    elif operation == "/":
        return dzielenie(numer1)
    else:
        print("Invalid sign! Try again!")
        main()

def dodawanie(numer1):
    print("Enter another number: ")
    numer2 = input()
    if numer2.isdigit():
        return int(numer1) + int(numer2)
    else:
        print("You must enter number!")
        dodawanie(numer1)

def odejmowanie(numer1):
    print("Enter another number: ")
    numer2 = input()
    if numer2.isdigit():
        return int(numer1) - int(numer2)
    else:
        print("You must enter number!")
        odejmowanie(numer1)

def mnozenie(numer1):
    print("Enter another number: ")
    numer2 = input()
    if numer2.isdigit():
        return int(numer1) * int(numer2)
    else:
        print("You must enter number!")
        mnozenie(numer1)

def dzielenie(numer1):
    print("Enter another number: ")
    numer2 = input()
    if numer2.isdigit():
        return int(numer1) / int(numer2)
    else:
        print("You must enter number")
        dzielenie(numer1)

def main():
    result = 0
    numer = pytanie()
    result = operator(numer)
    print("Result: ", result, end="\n\n")
    main()

if __name__ == "__main__": 
    main()
