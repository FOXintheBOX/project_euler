def multiple_sum(x,y,max):
    sum = 0
    for i in range(1,max):
        if i % x == 0 or i % y ==0:
            sum += i
    return sum

print multiple_sum(3,5,1000)
