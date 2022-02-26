# Trapezoidal Membership function
#         * * * * * * * 
#       * |           | *
#      *  |           |  *
#     *   |           |   *        ^
#    *    |           |    *       |
#   *     |           |     *      |
#  *      |           |      *     |
# * * * * * * * * * * * * * * *    y
# a       b           c       d
#   x ----->

# co-ordinates
a=10
b=30
c=100
d=400

# x values
x=400

# Using trignometry
if x<=b:
    m=1/(b-a)
    y=m*(x-a)
elif x>b and x<=c:
    m=0
    y=m*(x-b)+1
else:
    m=-1/(d-c)
    y=m*(x-c)+1

# Using fuzzy rule
ytria=round(max(min((x-a)/(b-a),1,(d-x)/(d-c)),0),3)
y=round(y,3)

print('Membership Function Value using trignometry:',y)
print('Membership Function Value using fuzzy rule:',ytria)