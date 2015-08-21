def fibonacci(max_value,divisor):
    val_pair = [1,2]
    i = 0
    seq = 0
    sum_chosen = 2
    while seq < max_value:
        seq = val_pair[0] + val_pair[1]
        val_pair[i] = seq
        i = 1 - i
        if seq % divisor == 0 and seq < max_value:
            sum_chosen += seq
            print seq
    print "...."
    return sum_chosen

print fibonacci(4000000,2)
