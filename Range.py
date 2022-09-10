# Range
# 1 argument
one_input = range(5)

for num in one_input:
    print(num)

# 2 arguments
two_input = range(5,10)

for num in two_input:
    print(num)

# 3 arguments
three_inputs = range(1,20, 3)

for num in three_inputs:
    print(num)

three_input = range(1,20, -3)

for num in three_input:
    print(num)

for num in range(1, 51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)