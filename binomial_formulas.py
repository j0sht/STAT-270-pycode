from math import factorial as fact
from math import sqrt

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

# Expected value (mean) of Binomial variable
#  n = number of trials
#  p = probability of success
def ev(n,p):
    return n*p

# Variance of Binomial variable
def var(n,p):
    return n*p*(1-p)

# Standard deviation of Binomial variable
def std_dev(n,p):
    return sqrt(var(n,p))
