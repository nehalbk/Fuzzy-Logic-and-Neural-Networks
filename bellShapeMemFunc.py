# @author Nehal Kankanawadi <nehalbk333@gmail.com> 
# Bell Shaped Membership Function

# co-ordinates
a,c,b=[float(i) for i in input("Enter the value for width, center and slope: ").split()]

# x values
x=float(input("Enter teh value for x: "))

# Using trignometry
y=round(1/(1+(abs((x-c)/a)**(2*b))),4)
print('Membership Function Value : ',y)