'''
Created on 17/09/2011

@author: periclesmiranda
'''

import scipy.stats as stat
from   numpy import mean, var
# you may use the already posted version of mean and variance Python routines.
 
from   math import *


class NormalityTester(object):

    def __init__(self):
        self.pnorm = stat.norm.cdf;
     
    def adstatistic(self, X):
        """
        Returns the Anderson darling test statistic.
        """
        n = len(X)
        Y = X[:]
        ybar = mean(Y)
        yvar = var(Y)
        ysd = sqrt(yvar)
        Y = [(y- ybar)/ysd for y in Y]
        A2 = -n
        S  =0.0 
        Y.sort()  # don't forget this!!!
        for i, y in enumerate(Y):
            j = i+1
            p = self.pnorm(y)
            q = 1- p
            S += (j+j - 1)*log(p)+ (2 *(n-j)+1)* log(q)
        A2 -= S/n
     
     
        A2 *= (1.0 + 4.0/n - 25.0/n**2)
        return A2
    
    '''
    If return is True, the hypothesis that distribution is normal is not rejected,
    otherwise It is rejected.
    '''
    def AndersonDarlingTest(self, X, alpha = 0.05):
        alphas    = [0.10, 0.05,  0.025, 0.01];
        critvalue = [0.632,0.751, 0.870, 1.029];
     
        try:
            for i, a in enumerate(alphas):
                if abs(alpha - a) < 1.0e-4:
                    crit = critvalue[i]
                    teststat = self.adstatistic(X)
                    print(teststat, crit)
                    return teststat < crit
        except:
            raise Exception("Signifance level not in");
        return None
        