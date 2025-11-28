import random
from decimal import Decimal
a = 1
b = 2
c = 3
s = a+c+b
print(s)
# Operations on Number 
# We can perform multiple operations on a number like addition,multiplication,division,floor division,exponent

num1 = 4
num2 = 5
# Addition
print(num1 + num2)
#  Subtraction
print(num1-num2)
# Division
print(num1/num2)
#Floor Division
print(num1//num2)
# multiplication
print(num1*num2)
# Exponent(power)
print(num1**num2)
# Remainder(Modulus)
print(num1 % num2)
print(num2 % num1)

# The output of above code till line 25 will be
# (6
# 9
# -1
# 0.8
# 0
# 20
# 1024
# 4
# 1)


# Repr(),str(),print()

print(repr('chai'))
print((str('chai')))
print('chai')

# str() → Converts an object into a human-readable string.

# repr() → Converts an object into a developer-friendly, unambiguous string (often valid Python code).

# print() → Displays the string output to the screen (uses str() internally).


# Comparison 

print(1<2)
print(5.0 == 5)
print(4.0 != 4)

x,y,z = 1,2,3
print(x<y<z)
# x<y<z written as x<y and y<z


# Interview Question
# 1 == 2 < 3 resulted in false why
# 1 == 2 and 2 < 3 then the final result is false 

# Math class functions
# math.floor:-choti value dega\
# math.trunc:-towards zero value dega

print((2+1j) * 3)
# Output (6+3j)
# Octal Number
print(0o20) 
# Output 16

# to calculate the octal and hexadecimal value

print(oct(16),hex(16),bin(64))
l1 = ['masala','ginger','mint','lemon']
print(random.random())
print(random.randint(1,100))
print(random.choice(['masala','ginger','mint','lemon']))
print(random.shuffle(l1))
s = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') -Decimal('0.3')
print(s)

