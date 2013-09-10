__author__ = 'stepan'
import numpy as np
#import matplotlib as plt
#import datetime
#from itertools import groupby
#from scipy import stats
#import datetime
from pylab import *

#"normally" distributed vector with no negative components
def safe_randn(means, vars, size):
    k=size*10
    sample_len = 0
    while (sample_len < size):
        sample = sqrt(vars)*np.random.randn(k)+means
        sample = sample[sample > 0]
        sample_len = sample.shape[0]
    return sample[:size]

  # Function to estimate average traffic per hit and its variance
  # atom_mean - mean amount of traffic per single hit based on full count of hits and traffic
  # atom_mean_var - estimated variance of atom_mean,
  # cumh - full number of hits
def var_estimate(d_sum, d_h):
    cumsum = np.sum(d_sum)
    cumh = np.sum(d_h)
    if  (cumh == 0):
        print "missing hit count"
    atom_mean = cumsum/cumh
    d = d_sum
    e = d_h
    corr_coeff = np.sum((cumh - e[e!=0])/e[e!=0]/cumh)
    #print 'corr_coeff=', corr_coeff
    nom=np.sum((d[d!=0]/e[e!=0] - atom_mean)**2)
    #print 'nom', nom
    atom_mean_var = np.sum((d[d!=0]/e[e!=0] - atom_mean)**2)/corr_coeff
    return {'atom_mean': atom_mean, 'atom_mean_var':atom_mean_var, 'cumh': cumh}

#creates a sample of artificial data
def sample(period, mean_h =  200.0, mean_t = 500, var_a = 10000):
    data = []
    for mday in range(period):
        hit_count = float(np.random.poisson(mean_h))
        total_traffic = np.sqrt(var_a*hit_count)*np.random.randn() + mean_t*hit_count
        data.append((total_traffic, hit_count))
    return data



if __name__ == "__main__":

    mean_s, var_s = 500, 10000

    data = sample(1000, mean_t= mean_s, var_a=var_s)
    t = np.array([z[0] for z in data])
    h = np.array([z[1] for z in data])
    estimate = var_estimate(t, h)
    print "Results of mean and variance estimation per visit\n", estimate
    print "Actual mean and variance of traffic per visit", mean_s, var_s
    #TODO: testing the model using large number of data samples, add some visualisation





