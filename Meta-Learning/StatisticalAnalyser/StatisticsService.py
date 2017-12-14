'''
Created on 06/09/2011

@author: periclesmiranda
'''

import math
from scipy import stats
#from scikits.learn import cross_val
from numpy import mean, sum

class StatisticsService(object):

    def __init__(self):
        #self.kfold = cross_val.KFold(2,1);
        self.num_support_vectors = 0;
    
    def entropy(self, classes ,target):
        result = 0;
        len_classes = len(classes);
        
        for i in range(0, len_classes):
            prob = (target.tolist()).count(classes[i]) / len_classes;
            if(prob <= 0):
                log = 1;
            else:
                log = math.log(prob,2);
            result = result + prob * log;
        
        return -result;
    
    def mean_correlation(self, data, n_attrs):
        correlation = 0;
        first_column = data[:, 0];
        for i in range(1, n_attrs):
            column = data[:, i];
            correlation += stats.pearsonr(first_column, column)[1];
            
        return correlation/n_attrs;
    
    def skewness(self, data):
        return mean(stats.skew(data));
    
    def kurtosis(self, data):
        return mean(stats.kurtosis(data));
    
    def geometric_mean(self, data):
        return mean(stats.gmean(data));
        
    def cross_validation(self, classifier, examples, target, k_attr):
        length = len(examples);
        self.kfold.n = length;
        self.kfold.k = k_attr;
        
        rates = [];
        support_vectors = [];
        for train, test in self.kfold:
            rates.append(classifier.fit(examples[train], target[train]).score(examples[test], target[test]));
            support_vectors.append(classifier.support_.shape[0]);
            
        self.num_support_vectors = sum(support_vectors)/len(support_vectors);
        
        return sum(rates)/k_attr;
    
    '''
    def cross_validation(self, classifier, examples, target, k_attr):
        length = len(examples);
        self.kfold.n = length;
        self.kfold.k = k_attr;
        
        correct_predictions = cross_val.cross_val_score(classifier, examples, target, cv=self.kfold, iid=True);
        return sum(correct_predictions) / length;
    '''
    
    def number_of_support_vectors(self):
        return int(self.num_support_vectors);
    
    def cross_validation_mlp(self, classifier, examples, target, k_attr):
        pass
            