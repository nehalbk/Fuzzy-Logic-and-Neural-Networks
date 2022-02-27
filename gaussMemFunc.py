# @author Nehal Kankanawadi <nehalbk333@gmail.com> 
# Gaussian Membership Function

import math

# co-ordinates
mean=int(input("Enter the value for mean: "))
stdDev=int(input("Enter the value for Standard Deviation: "))

# x values
x=int(input("Enter teh value for x: "))

# Using trignometry
y=round(1/(math.exp(0.5*(((x-mean)/stdDev)**2))),4)

print(y)