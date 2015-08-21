def find_triplet(target):
    for i in range(1,target/3):
        for j in range(i+1,(target+i+1)/2):
            k = target - i - j
            if i**2 + j**2 == k**2: return i*j*k

print find_triplet(1000)
