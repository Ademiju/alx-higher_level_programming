#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10 if number > 0 else number % -10
if last_num > 5:
    result = "and is greater than 5"
elif last_num == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_num, result))
