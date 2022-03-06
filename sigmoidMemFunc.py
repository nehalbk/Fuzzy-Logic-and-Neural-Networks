# @author Nehal Kankanawadi <nehalbk333@gmail.com> 
# Sigmoid Membership Function

import math

# co-ordinates
a=float(input("Enter the value for slope (a): "))
b=float(input("Enter the value for b (y=0.5): "))

# x values
x=float(input("Enter the value for x: "))

# Using trignometry
y=round(1/(1+math.exp(-a*(x-b))),4)

print('Membership Function Value : ',y)