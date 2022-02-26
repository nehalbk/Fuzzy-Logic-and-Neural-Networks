# Triangular Membership function
#         *
#       * | *
#      *  |   *
#     *   |     *           ^
#    *    |       *         |
#   *     |         *       |
#  *      |           *     |
# ***********************   y
# a       b             c
#   x ----->

# co-ordinates
a=10
b=30
c=100

# x values
x=100

# Membership Function = y

# Using trignometry
if x<=b:
    m=1/(b-a)
    y=m*(x-a)
else:
    m=-1/(c-b)
    y=m*(x-b)+1


# Using fuzzy rule
ytria=max(min((x-a)/(b-a),(c-x)/(c-b)),0)

print('Membership Function Value using trignometry:',y)
print('Membership Function Value using fuzzy rule:',ytria)