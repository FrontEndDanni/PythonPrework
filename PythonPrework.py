line = "Hello World"
print(line)

#QUESTION 1: Write a function to print "hello_USERNAME!"
def hello_name(user_name):
    print("hello_" + user_name + "!")
hello_name("user_name")

#QUESTION 2: Write a python function, first_odds that prints out odd numbers from 1 - 100 and returns nothing.
def first_odds():
    a = 1
    while a<= 100:
        print(a)
        a += 2
first_odds()

#QUESTION 3: Please write a Python function, max_num_in_list to return the max number in a given list. 
def max_num_in_list(a_list):
    return max(a_list)

#QUESTION 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    div_by_4 = a_year % 4 == 0
    div_by_100 = a_year % 100 == 0 
    div_by_400 = a_year % 400 == 0
    if not div_by_4:
        return False
    else: 
        if div_by_100:
            if div_by_400:
                return True
            else:
                return False
        else:
            return True
print(is_leap_year(2016))
print(is_leap_year(2011))
print(is_leap_year(2000))
print(is_leap_year(1900))



#QUESTION 5: Write a function to check to see if all the n umbers in a list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consectuive numbers, but [1,2,4,5] are not. The return should be boolean Type.
def is_consecutive(a_list):
    num1 = a_list[0] - 1
    for number in a_list:
        if number != num1 + 1:
            return False 
        num1 = number
    return True
print(is_consecutive([2,3,4,5]))
print(is_consecutive([2,5,6,7]))