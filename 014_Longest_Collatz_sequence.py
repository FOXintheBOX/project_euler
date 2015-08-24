def collatz(n):
    counter = 1
    even = lambda x: x/2
    odd = lambda x: 3*x + 1
    while n > 1:
        if n % 2 == 0:
            n = even(n)
        else:
            n = odd(n)
        counter += 1
    return counter

max_len = 0
for i in range(1,1000000):
    j = collatz(i)
    if j > max_len:
        max_len = j
        print [i,j]
