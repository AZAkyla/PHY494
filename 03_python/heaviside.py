# List of x

xmax = 4
x, dx = -4.5, .5

xvalues = []
while x <= xmax:
    x += dx
    xvalues.append (x)
# print(xvalues)

def heaviside(x):
    """Heaviside step function"""

    theta = None
    if x < 0:
        theta = 0
    elif x == 0:
        theta = 0.5
    else:
        theta = 1
    
    x = xvalues
    theta = heaviside(x)
print( "Theta(" + str(x) + ") = " + str(theta))
