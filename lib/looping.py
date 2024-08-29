#!/usr/bin/env python3

def happy_new_year():
    count = 10 
    while(count > 0):
       print(count)
       count -= 1
       print('Happy New Year!')
happy_new_year()
     

def square_integers(int_list):
    square_ints = [int*int for int in int_list]
    return (square_ints)


def fizzbuzz():
    i = 0
    while i < 100:
        i +=1
        if i%3 == 0 and i%5 ==0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
fizzbuzz()

