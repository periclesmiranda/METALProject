'''
Created on 16/09/2011

@author: periclesmiranda
'''
from operator import itemgetter as getItems

class Normalizer(object):

    @staticmethod
    def normalize(data, max_limit, min_limit):        
        for i in range(0, len(data[0])):
            getColumn = getItems(i);
            column = map(getColumn, data);
            
            max_column = max(column);
            min_column = min(column);
            
            for j in range(0, len(data)): 
                data[j][i] = ((data[j][i] - min_column)/(max_column - min_column)) * (max_limit - min_limit) + min_limit;
        return data;
        