'''
Created on 22/11/2011

@author: periclesmiranda
'''
from operator import itemgetter as getItems
import random
import math

class SolutionGenerator(object):

    @staticmethod
    def createAdditionalSuggestions(number_of_additional, values):
        additionals = [];
        
        lower_bound = [];
        upper_bound = [];
        
        for i in range(0, len(values[0])):
            getColumn = getItems(i);
            column = map(getColumn, values);
            
            max_column = max(column);
            min_column = min(column);
            
            upper_bound.append(max_column);
            lower_bound.append(min_column);
        
        for i in range(0, number_of_additional):
            rand_values = [math.ceil(random.uniform(lower_bound[0], upper_bound[0])), math.ceil(random.uniform(lower_bound[1], upper_bound[1]))];
            additionals.append(rand_values);
        return additionals;        