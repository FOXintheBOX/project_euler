def fibonacci(max_value):
    vals = [1,2]
    i = 0
    seq = 0
    sum_even = 0
    while vals[i] < max_value:
        if vals[i] % 2 == 0:
            sum_even += vals[i]
            print vals[i]
        vals[i] = sum(vals)
        i = 1 - i
    print "...."
    return sum_even

print fibonacci(4000000)
