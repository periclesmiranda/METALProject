'''
Created on 03/09/2011

@author: periclesmiranda
'''

class Util(object):

    '''
    According the parameter count (i.e. 2), this method creates a string (?,?)
    '''
    @staticmethod
    def formatValuesAccording(count):
        tuple = (0,)*count
        tuple = str(tuple).replace('0','?');
        return tuple;
        