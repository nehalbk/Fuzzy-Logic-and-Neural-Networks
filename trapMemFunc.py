# @author Nehal Kankanawadi <nehalbk333@gmail.com>
#  Trapezoidal Membership function
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

print(' Trapezoidal Membership function')
print('         * * * * * * * ')
print('       * |           | *')
print('      *  |           |  *')
print('     *   |           |   *        ^')
print('    *    |           |    *       |')
print('   *     |           |     *      |')
print('  *      |           |      *     |')
print(' * * * * * * * * * * * * * * *    y')
print(' a       b           c       d')
print('   x ----->')

# co-ordinates input
a,b,c,d = [float(x) for x in input("Enter the values for a,b,c and d: ").split()]

# x value input
x=float(input("Enter the values for x: "))

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
ytria=round(max(min((x-a)/(b-a),1,(d-x)/(d-c)),0),4)
y=round(y,4)

print('Membership Function Value using trignometry:',y)
print('Membership Function Value using fuzzy rule:',ytria)