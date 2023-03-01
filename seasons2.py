#Write a program that takes a date as input and outputs the date's season in the northern hemisphere.
# The input is a string to represent the month and an int to represent the day.

input_month = input()
input_day = int(input())
spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'February', 'March']

# Spring: March 20 - June 20
March_spring = range(20, 32, 1)
April_spring = range(1, 31, 1)
May_spring = range(1, 32, 1)
June_spring = range(1, 21, 1)

# Summer: June 21 - September 21
June_summer = range(21, 31, 1)
July_summer = range(1, 32, 1)
August_summer = range(1, 31, 1)
September_summer = range(1, 22, 1)

# Autumn: September 22 - December 20
September_autumn = range(22, 31, 1)
October_autumn = range(1, 32, 1)
November_autumn = range(1, 31, 1)
December_autumn = range(1, 21, 1)

# Winter: December 21 - March 19
December_winter = range(21, 32, 1)
January_winter = range(1, 32, 1)
February_winter = range(1, 29, 1)
March_winter = range(1, 20, 1)

# SPRING
if (input_month in spring) and (32 > input_day > 0):

    if (input_month == 'March') and (input_day in March_spring):
        print('Spring')
    elif (input_month == 'March') and (input_day in March_winter):
        print('Winter')
    elif (input_month == 'April') and (input_day in April_spring):
        print('Spring')
    elif (input_month == 'May') and (input_day in May_spring):
        print('Spring')
    elif (input_month == 'June') and (input_day in June_spring):
        print('Spring')
    elif (input_month == 'June') and (input_day in June_summer):
        print('Summer')

elif (input_month in summer) and (32 > input_day > 0):

    if (input_month == 'July') and (input_day in July_summer):
        print('Summer')
    elif (input_month == 'August') and (input_day in August_summer):
        print('Summer')
    elif (input_month == 'September') and (input_day in September_summer):
        print('Summer')
    elif (input_month == 'September') and (input_day in September_autumn):
        print('Autumn')
    else:
        print('Invalid')

elif (input_month in autumn) and (32 > input_day > 0):

    if (input_month == 'October') and (input_day in October_autumn):
        print('Autumn')
    elif (input_month == 'November') and (input_day in November_autumn):
        print('Autumn')
    elif (input_month == 'December') and (input_day in December_autumn):
        print('Autumn')
    else:
        print('Invalid')

elif (input_month in winter) and (32 > input_day > 0):
    if (input_month == 'December') and (input_day in December_winter):
        print('Winter')
    elif (input_month == 'January') and (input_day in January_winter):
        print('Winter')
    elif (input_month == 'February') and (input_day in February_winter):
        print('Winter')

    else:
        print('Invalid')
else:
    print('Invalid')


