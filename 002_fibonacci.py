def fibonacci(max_value,divisor):
    vals = [1,2]
    i = 0
    seq = 0
    sum_chosen = 0
    while vals[i] < max_value:
        if vals[i] % divisor == 0:
            sum_chosen += vals[i]
            print vals[i]
        vals[i] = sum(vals)
        i = 1 - i
    print "...."
    return sum_chosen

print fibonacci(4000000,2)
