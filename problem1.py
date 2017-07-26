sum = 0
for x in range (1,1000):
    if float(x%3)==0 or float(x%5)== 0:
        sum +=x
print(sum)