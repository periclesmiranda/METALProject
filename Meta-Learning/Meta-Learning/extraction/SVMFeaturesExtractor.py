'''
Created on 02/01/2012

@author: periclesmiranda
'''
from extraction.FeaturesExtractor import FeaturesExtractor

class SVMFeaturesExtractor(FeaturesExtractor):

    def evaluateScores(self, clf, data, k):
        classification_rate = self.statsService.cross_validation(clf, data.data, data.target, k);
        n_support_vectors = self.statsService.number_of_support_vectors();
        
        return classification_rate, n_support_vectors;
        