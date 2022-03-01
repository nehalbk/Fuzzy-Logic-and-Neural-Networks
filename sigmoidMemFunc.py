# @author Nehal Kankanawadi <nehalbk333@gmail.com> 
# Sigmoid Membership Function

import math

# co-ordinates
a=int(input("Enter the value for slope (a): "))
b=int(input("Enter the value for b (y=0.5): "))

# x values
x=int(input("Enter the value for x: "))

# Using trignometry
y=round(1/(1+math.exp(-a*(x-b))),4)

print('Membership Function Value : ',y)