def nofdiv(x):
    divs = 0;
    print('x = ' , x)
    for i in range(2, x+1):
        if x % i == 0:
            divs += 1
            print (i)
    print('nofdiv = ', divs)
    if divs >= 500:
        return True;
    else:
        return False;

triangle = 1;
index = 1;
boolcheck = False;

while boolcheck!= True :
    index +=1
    triangle += index
    boolcheck = nofdiv(triangle)


print(triangle)