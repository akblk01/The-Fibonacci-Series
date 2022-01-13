"""
The Fibonacci Series creates a new number as the sum of the previous two numbers.

1,1,2,3,5,8,13,21,34...............
"""
first_number = 1

second_number = 1

fibonacci = [first_number,second_number]
for i in range(20):


    first_number,second_number = second_number,first_number + second_number

    fibonacci.append(second_number)

print(fibonacci)

