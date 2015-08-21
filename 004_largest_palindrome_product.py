import string

def is_palindrome(n):
    n_str = str(n)
    if len(n_str) % 2 != 0: return False
    else:
        return n_str[:len(n_str)/2] == n_str[:len(n_str)/2-1:-1]

def largest_pal():
    products = []
    for i in range(100,1000):
        for j in range(100,i):
            products.append(i*j)
    products.sort(reverse = True)
    for product in products:
        if is_palindrome(product):
            return product

print is_palindrome(21)
print largest_pal()
