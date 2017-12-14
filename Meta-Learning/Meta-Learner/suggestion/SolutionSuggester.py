'''
Created on 07/09/2011

@author: periclesmiranda
'''
from suggestion.DistanceEvaluator import DistanceEvaluator
from suggestion.Normalizer import Normalizer

class SolutionSuggester(object):

    def __init__(self):
        pass
    
    def generate_suggestions(self, feature, dbs_per_features, dbs_per_operators, n_suggestions, n_problems=None):
        pass
    
    def _suggest(self, input, features_table, operators_table, n_valid_attrs, problems, n_suggestions, n_problems=None):
        features = self._suggest_feature(input, features_table, n_valid_attrs, n_suggestions, n_problems);
        suggested_operators = self._suggest_operators(features, operators_table, problems, n_suggestions, n_problems);
        return suggested_operators;
    
    def _suggest_feature(self, input, features_table, n_valid_attrs, n_suggestions, n_problems=None):
        count = 0;
        comparison_rates = {};

        normalized_data = self._pre_process(input, features_table);
        input = normalized_data[-1];
        normalized_data.remove(input);

        for meta_example in normalized_data:
            comparison_rates[count] = DistanceEvaluator.euclidian(input, meta_example);
            count = count +1;
            
        comparison_rates = sorted(comparison_rates.items(), key=lambda x: x[-1]);

        features = [];
        
        if n_problems == None:
            for i in xrange(0, n_suggestions):
                features.append(features_table[comparison_rates[i][0]]);
        elif n_problems == 1:
            features.append(features_table[comparison_rates[0][0]]);
            
        return features;
    
    def _suggest_operators(self, features, operators_table, problems, n_suggestions, n_problems):
        pass
    
    def _pre_process(self, input, features_table):
        meta_examples = (map(self._removeFirst, features_table));
        meta_examples.append(input);
        
        return Normalizer.normalize(map(self._makeList,meta_examples), 1, 0);
    
    def _removeFirst(self, data):
        return data[1:];
    
    def _makeList(self, tuple):
        return list(tuple);

    
        
