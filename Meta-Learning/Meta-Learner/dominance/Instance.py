'''
Created on 22/11/2011

@author: periclesmiranda
'''

class Instance(object):

    def __init__(self, vector):
        self.vector = vector;
        self.dominated = False;
        self.crowdingDistance = 0;
        self.comparableDimension = 0;