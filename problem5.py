listofchecks = [3,6,7,8,9,11,12,13,14,15,16,17,18,19]

def divided(x):
    for i in listofchecks:
        if x%i != 0:
            print(i)
            return False
    return True

x = 20
checker = False
while checker==False:
    x+=20
    print('x', x)
    checker=divided(x)


print ('answer is ',x)