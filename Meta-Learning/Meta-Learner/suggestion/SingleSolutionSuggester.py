'''
Created on 03/01/2012

@author: periclesmiranda
'''
from suggestion.SolutionSuggester import SolutionSuggester
from suggestion.SolutionGenerator import SolutionGenerator
import math

class SingleSolutionSuggester(SolutionSuggester):
    
    def generate_suggestions(self, feature, dbs_per_features, dbs_per_operators, n_suggestions, n_problems=None):
        features = dbs_per_features;
        operators = dbs_per_operators;
        
        current_features = features[::];
        current_features.remove(feature);
        
        current_operators = operators[::];
        current_operators = filter(lambda op: op[0] != feature[0], current_operators)
        
        filtered_ops = self._suggest(feature[1:], current_features, current_operators, len(feature[1:]), ["max"], n_suggestions, n_problems);
        
        formatted_sugs = SuggestionFormatter.format(filtered_ops);
        
        if len(formatted_sugs) < n_suggestions:
            for i in SolutionGenerator.createAdditionalSuggestions(n_suggestions - len(formatted_sugs), formatted_sugs):
                formatted_sugs.append(i);
        return formatted_sugs;
    
    def _suggest_operators(self, features, operators_table, problems, n_suggestions, n_problems):
        resultant_ops = [];
        for i in range(0, len(features)):
            filtered_operators = filter(lambda op: op[0] == features[i][0], operators_table);
            
            if problems[0] == "min":
                operators = sorted(filtered_operators, key=lambda x: x[-1])
            if problems[0] == "max":
                operators = sorted(filtered_operators, key=lambda x: x[-1], reverse=True)
            
            if n_problems == None:
                resultant_ops.append(operators[:1][0]);
            elif n_problems == 1:
                resultant_ops = operators[:n_suggestions];
        
        return resultant_ops;
    
class SuggestionFormatter(object):
    
    @staticmethod
    def format(suggestions):
        l = [];
        for i in range(0, len(suggestions)):
            li = list(suggestions[i]);
            l.append([math.log(li[1],2), math.log(li[2], 2)]);
        return l;
    