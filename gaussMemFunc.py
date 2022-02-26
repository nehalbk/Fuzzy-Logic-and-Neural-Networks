#Gaussian Membership Function
# co-ordinates
import math
mean=100
stdDev=20
e=2.7182818284590452353602874713527

# x values
x=80

# Using trignometry
y=1/(math.pow(e,(0.5*math.pow(((x-mean)/stdDev),2))))

print(y)