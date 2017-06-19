import csv
import datetime
import copy


def factorial(number,leading_space):

    

    if number > 1:
        print (leading_space, number, "! = ", number, " * ", number-1, "!", sep='')
        more_space = leading_space + "         "
        smaller_factorial = factorial(number-1, more_space)        
        answer = number * smaller_factorial
    else:
        print (leading_space, "1! = 1", sep='')
        answer = 1

    print (leading_space, answer, sep='')
    return answer 
    
def main():
    newnum = factorial(4,"")
    return


main()
