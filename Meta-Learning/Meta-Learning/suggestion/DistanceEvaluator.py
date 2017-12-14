'''
Created on 07/09/2011

@author: periclesmiranda
'''

from scipy.spatial import distance

class DistanceEvaluator(object):

    @staticmethod
    def euclidian(positions_vector1, positions_vector2):
        return distance.euclidean(positions_vector1, positions_vector2);