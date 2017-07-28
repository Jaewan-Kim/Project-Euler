def isprime(number):

    for x in range(2, number-2):
        if float(number%x)==0:
            return False

    return True

list1 = list(range(2,1999999))

sum=0
for x in list1:
    if (isprime(x)):
        print(x)
        y = x+x
        while(y<2000000):
            if y in list1:
                list1.remove(y)
                print(y)
                y+=x
        sum+=x

print(x)