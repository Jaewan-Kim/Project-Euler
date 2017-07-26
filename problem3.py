def isprime(number):

    for x in range(2, number-2):
        if float(number%x)==0:
            return False

    return True

list1 = []
for y in range(3, int(600851475143/2)):
    if float(600851475143%y)==0 & isprime(y):
        print(y)
        list1.append(y)
print(list1)
