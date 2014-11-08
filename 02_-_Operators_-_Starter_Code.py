# Make sure you read all of the comments in this file carefully!

# This project will test your understanding of variables and operators.
# Operators (General Definition):
#       http://en.wikipedia.org/wiki/Operator_(computer_programming)

# You will be given a series of mathematical and logical tasks.  Implement these
# ONLY using variables and operators.  No loops, conditionals, functions or data
# structures should be used.  You will only be working with the basic data
# types: Integer, Float, String, and Boolean.

# Operators that you can use:
#       +, -, *, /, %, **, //,
#       ==, !=, <>, >, <, >=, <=,
#       =, +=, -=, *=, /=, %=, **=, //=,
#       and, or, not,
#       &, |, ^, ~, <<, >>

# Format for each problem: (READ THIS CAREFULLY)
#   # Problem <problem number>:
#   # Value -  <how many points this problem is worth for your grade>
#   <input variables for the problem>
#   # Task: <description of the problem>
#   # Solution:
#   # Replace this code with your solution.

# Format Example:
#   # Problem 1:
#   # Value -  5
#   a = 1
#   b = 1
#   # Task: Add 'a' and 'b' and store the result in a variable named output.
#   # Solution:
#   # Replace this comment with your solution.


# A Correct Solution to the Problem 1 example above:
#   # Problem 1:
#   # Value -  5
#   a = 1
#   b = 1
#   # Task: Add 'a' and 'b' and store the result in a variable named output.
#   # Solution:
#   output = a + b

# A WRONG Solution to the Problem 1 example above:
#   # Problem 1:
#   # Value -  5
#   a = 1
#   b = 1
#   # Task: Add 'a' and 'b' and store the result in a variable named output.
#   # Solution:
#   output = 2
#
# Note how output would be wrong a = 5  and b = 1.

# Grading Rubric:
#   Problems: 80pts
#      - For each problem you solve correctly you will get the points assigned
#        to it.
#   Problem Efficiency: 10pts
#      - Many problems can be solved many ways.  You will be graded on the
#        number of variables and operators used. The fewer the better!
#   Readability and Style: 10pts
#      - You code should be readable and concise.

# Notes:
#   - The variable values provided below for testing will not be the same ones
#     used for grading.
#   - This is an individual project.  You must complete all work on your own.
#   - Good Luck!

# Problem 1:
# Value - 5
a = 5
# Task: Cube 'a' and store the result in a variable named output.
#       Example: if  a = 3 then output should be 27
# Solution:
output = a ** 3

# Problem 2:
# Value - 5
a = 9
# Task: Calculate the square root of 'a' and store the result in a variable named
#                output.
#                 Example: if  a = 4 then output should be 2
# Solution:
output = a ** 0.5

# Problem 3:
# Value - 5
a = 10
b = 3
# Task: Implement xor (abbreviation for 'exclusive or'). Xor should be true if a
#       and b are not the same. Store the value of a xor b in a variable named
#       output.
#       Example: 2 xor 9 = True
# Solution:
output = (a != b)


# Problem 4:
# Value - 5
a = 'apple'
b = 'banana'
c = 'coconut'
# Task: Combine a, b, and c to form a sentence (string) and store the result
#                in a variable named output. Any sentence will do! Remember
#       during grading a, b and c will be different than above.
#
# Solution:
output = 'An' + a + 'a' + b + 'and a' + c + 'had a party together.' 


# Problem 5:
# Value - 5
numerator = 18
denominator = 5
# Task: Calculate the remainder of the division of the numerator by the denominator and
#         store the result in a variable named output.
#         Example: If numerator = 10 and denominator = 3, output should be 1
# Solution:
output = numerator % denominator
