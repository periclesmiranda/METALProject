'''
Created on 07/09/2011

@author: periclesmiranda
'''

class FeaturesExtractor(object):

    def __init__(self, statsService):
        self.statsService = statsService;
    
    def extract(self, data):
        
        examples, target = data.data, data.target;
        
        n_examples, n_attrs = data.data.shape;  
        n_class = len(set(target))
        mean_corr = self.statsService.mean_correlation(examples, n_attrs);
        gmean = self.statsService.geometric_mean(examples);
        skewness = self.statsService.skewness(examples);
        kurtosis = self.statsService.kurtosis(examples);
        entropy = self.statsService.entropy(list(set(target)), target)
        
        return [n_examples, n_attrs, n_class, mean_corr, gmean, skewness, kurtosis, entropy];
    
    def evaluateScores(self, clf, data, k):
        pass