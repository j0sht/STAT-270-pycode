from math import factorial as fact

# Permutation formula
def npr(n,r):
    return fact(n) // fact(n-r)

# Combination formula
def ncr(n,r):
    return fact(n) // (fact(r)*fact(n-r))
