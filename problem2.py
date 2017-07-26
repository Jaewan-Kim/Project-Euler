def fib(index):
    if index > 2:
        return fib(index-1) + fib(index-2)
    elif index == 2:
        return 2
    elif index == 1:
        return 1

sum =0
lastfib = 0
index = 1
while lastfib <= 4000000:
    lastfib= fib(index)
    if float(lastfib%2) == 0:
        sum += lastfib
    index +=1

print(sum)