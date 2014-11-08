# This is a comment.  A line beginning with a # symbol is a comment.
# Comments are not executed by the python interpreter.

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

# Code Example:
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
#      - You code should be readable and concise that adheres to our python
#        style guide.

# Notes
#   - The variable values provided below for testing will not be the same ones
#     used for grading.
#   - This is an individual project.  You must complete all work on your own.
#   - Good Luck!!!

# Problem 1:
# Value - 20
a = 1
b = 2
c = 3
# Task: Check to see if a is between b and c.  Make a variable output that is
#       True if a is between b and c, but False otherwise.
#
# Solution:
output = ((c >= a and a >= b) or (b >= a and a >= c))


# Problem 2: 
# Value - 20
a = 18473
# Task: Store the hundredth digit in a in a variable named output.
#       Example: If a = 123456 then output should be 4.
# Solution:
output = ( a / 100 ) % 10

# Problem 3:
# Value - 20
num = 37
# Task: Store num rounded to the nearest multiple of 10 in output.
#
# Solution:
output = ((num + 5) / 10) *10


# Problem 4:
# Value - 20
value1 = 'one'
value2 = 'two'
# Task: Swap value1 and value2. Given value1 and value2 above make sure that you
#       swap value1 to be value2, and value2 to be value1.
#
#       Hint: Make sure you preserve both values during the swap.
#       Example:
#              Before Swapping: value1 = 'f' and value2 = 'g'
#              After Swapping: value1 = 'g' and value2 = 'f'
# Solution:
value_1 = value1
value_2 = value2
value1 = value_2
value2 = value_1


# Problem 5:
# Value - 20
time = 17
# Task: Convert time from military to standard time and store it back in the
#       time variable.
#       Example: If time = 22 then once converted time should be 10.
# Solution: 
time = ((((time % 12) + 12) % 12.1 ) +.1 ) // 1


# Problem BONUS:
# Value - 10
x1 = 0
y1 = 0
x2 = 0
y2 = 0
# Task: Calculate the distance between two points (x1, y1) and (x2, y2) and
#       store it in output.
#
# Solution:
output = ((y1 - y2) ** 2 + (x1 - x2) ** 2) **0.5


# Problem BONUS:
# Value - 10
a = 33
# Task: Using only bit operators multiply a by 2 and store it in a variable
#       named output.
#
# Solution:
output = (a << 1)
