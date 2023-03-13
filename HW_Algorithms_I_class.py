def find_sum(number: int):
    result = 1
    for i in range(2, number + 1):
       result += i

    print(f'The sum of digits from 1 to {number} is {result}')


num_a = 13
find_sum(num_a)


def max_of_three(a, b, c):
    if (a > b) and (a > c):
        max_num = a
    elif (b > a) and (b > c):
        max_num = b
    else:
        max_num = c
    return max_num


a = 20
b = 25
c = 5
result = max_of_three(a, b, c)
print(f'Max number is {result}')
max_of_three(a, b, c)



#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560,
# then 3 digits will be even (4, 6, and 0)
# and 2 odd digits (3 and 5).

number = 34560
num_list = [int(i) for i in str(number)]
print(num_list)

evens = 0
odds = 0

for num in num_list:
    if num % 2 == 0:
          evens += 1
    else:
        odds += 1

print('Count of odds', odds)
print('Count of evens', evens)




#codewars: This kata is about multiplying a given number
# by eight if it is an even number
# and by nine otherwise.


def kata_one(number: int):
    if number % 2 == 0:
        print(number * 8)
    else:
        print(number * 9)

kata_one(6)

# You are given the length and width of a 4-sided polygon.
# The polygon can either be a rectangle or a square.
# If it is a square, return its area.
# If it is a rectangle, return its perimeter


def kata_two(a: int, b: int):
    if (a == b):
        print('This is a square and its area is', a ** 4)
    else:
        print('Ths is rectangle and its perimeter is', 2*(a + b))

kata_two(5,5)


#Write function bmi that calculates body mass index (bmi = weight / height2).
#if bmi <= 18.5 return "Underweight"
#if bmi <= 25.0 return "Normal"

def calculate_bmi(weight, height):

    bmi = weight / (height/100) ** 2
    if bmi <= 18.5:
        print("Underweight")
    elif bmi <= 25.0:
        print ("Normal")
    else:
        print("Overweight")

calculate_bmi(70, 170)




