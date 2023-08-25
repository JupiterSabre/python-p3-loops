#!/usr/bin/env python3

#Write a function happy_new_year() using a while loop that outputs numbers starting at 10 and counting down to 1. After reaching 1, print out "Happy New Year!"
def happy_new_year():
    i = 10
    while i >= 1:
        print(i)
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return [x ** 2 for x in int_list]
    
    

def fizzbuzz():
    for i in range(1,101):
        if not i % 15:
            print("FizzBuzz")
        elif not i % 5:
            print("Buzz")
        elif not i % 3:
            print("Fizz")
        else:
            print(i)

