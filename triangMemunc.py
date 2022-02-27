# @author Nehal Kankanawadi <nehalbk333@gmail.com>
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
print(' Triangular Membership function')
print('         *')
print('        *| *')
print('       * |  *')
print('      *  |   *')
print('     *   |     *          ^')
print('    *    |       *        |')
print('   *     |        *       |')
print('  *      |          *     |')
print(' ***********************   y')
print(' a       b             c')
print('   x ----->')

# co-ordinates input
a,b,c = [int(x) for x in input("Enter the values for a,b and c: ").split()]

# x value input
x=int(input("Enter the values for x: "))

# Membership Function = y

# Using trignometry
if x<=b:
    m=1/(b-a)
    y=m*(x-a)
else:
    m=-1/(c-b)
    y=m*(x-b)+1


# Using fuzzy rule
ytria=round(max(min((x-a)/(b-a),(c-x)/(c-b)),0),4)
y=round(y,4)

print('Membership Function Value using trignometry:',y)
print('Membership Function Value using fuzzy rule:',ytria)