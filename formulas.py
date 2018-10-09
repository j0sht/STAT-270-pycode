from math import factorial as fact

# Permutation formula
def npr(n,r):
    return fact(n) // fact(n-r)

# Combination formula
def ncr(n,r):
    return fact(n) // (fact(r)*fact(n-r))

# Binomial Probability
#  n = number of trials
#  r = number of successes
#  p = probability of success
def binomial_probability(n,r,p):
    # ncr(number of trials, successes) * p^successes * (1-p)^(trials-successes)
    return ncr(n,r)*(p**r)*((1-p)**(n-r))
