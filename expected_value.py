# xs: List of possible x-values
# probs: List of associated probabilities
# NOTE: Both must be of same len
def expected_value(xs, probs):
    ev = 0
    for i in range(0,len(probs)):
        ev += xs[i]*probs[i]
    return ev

# xs, probs - same as above
# mean - the expected value, calculated using xs and probs
#  unless given a different value
def variance(xs,probs,mean=0):
    if (mean == 0):
        mean = expected_value(xs,probs)
    v = 0
    for i in range(0,len(probs)):
        v += (((xs[i]-mean)**2)*probs[i])
    return v

def standard_deviation(xs,probs,mean=0):
    from math import sqrt
    if (mean == 0):
        mean = expected_value(xs,probs)
    return sqrt(variance(xs,probs,mean))
