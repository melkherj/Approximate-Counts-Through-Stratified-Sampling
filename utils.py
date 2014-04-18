from pylab import *
import random

def kl2(q,p):
    return q*log(q/p) + (1-q)*log((1-q)/(1-p))

def choose_alpha(p):
    ''' Choose alpha for the best quadratic lower bound for the kl divergence '''
    if p < 0.49999:
        return kl2(1-p,p)/(1-2*p)**2
    else:
        return 1/(2*p*(1-p))
    
def choose_min_alpha(p):
    p = min(p,1-p)
    return choose_alpha(p)

def sample_dist(dist, samples=10):
    ''' Given a discrete distribution, eg [0.1,0.2,0.7], generate <samples>
        samples from the distribution, eg [0,1,2,1,2,2,2,1,0] '''
    cumulative = cumsum(dist)
    return [nonzero(cumulative > r)[0][0] for r in rand(samples)]

def sample_bernouli(p,samples=10):
    dist = array([1-p,p])
    return sample_dist(dist, samples=samples)
