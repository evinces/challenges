"""Calculating with Functions

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

JavaScript:

    seven(times(five())); // must return 35
    four(plus(nine())); // must return 13
    eight(minus(three())); // must return 5
    six(dividedBy(two())); // must return 3

Ruby:

    seven(times(five)) # must return 35
    four(plus(nine)) # must return 13
    eight(minus(three)) # must return 5
    six(divided_by(two)) # must return 3

Requirements:

    - There must be a function for each number from 0 ("zero") to 9 ("nine")
    - There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby)
    - Each calculation consist of exactly one operation and two numbers
    - The most outer function represents the left operand, the most inner function represents the right operand
    - Divison should be integer division, e.g eight(dividedBy(three()))/eight(divided_by(three)) should return 2, not 2.666666...

"""


def do_math(num1, num2, op):
    if op == "+":
        return num1 + num2
    if op == "-":
        return num1 - num2
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1 / num2

def zero(pair=None):
    return do_math(0, pair[0], pair[1]) if pair else 0
def one(pair=None):
    return do_math(1, pair[0], pair[1]) if pair else 1
def two(pair=None):
    return do_math(2, pair[0], pair[1]) if pair else 2
def three(pair=None):
    return do_math(3, pair[0], pair[1]) if pair else 3
def four(pair=None):
    return do_math(4, pair[0], pair[1]) if pair else 4
def five(pair=None):
    return do_math(5, pair[0], pair[1]) if pair else 5
def six(pair=None):
    return do_math(6, pair[0], pair[1]) if pair else 6
def seven(pair=None):
    return do_math(7, pair[0], pair[1]) if pair else 7
def eight(pair=None):
    return do_math(8, pair[0], pair[1]) if pair else 8
def nine(pair=None):
    return do_math(9, pair[0], pair[1]) if pair else 9

def plus(num):
    return (num, "+")
def minus(num):
    return (num, "-")
def times(num):
    return (num, "*")
def divided_by(num):
    return (num, "/")
