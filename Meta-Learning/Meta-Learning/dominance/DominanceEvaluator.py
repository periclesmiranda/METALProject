'''
Created on 22/11/2011

@author: periclesmiranda
'''
from dominance.Instance import Instance
import math
import sys

class DominanceEvaluator(object):

    @staticmethod
    def __createInstances(instances):
        
        obj_instances = [];
        for i in range(0, len(instances)):
            obj_instances.append(Instance(instances[i]));
        return obj_instances;
    
    @staticmethod
    def verifyDominanceUsingCrowdingDistance(instances, problems):
        externalArchive = DominanceEvaluator.verifyDominance(instances, problems)
        
        for j in xrange(0, len(externalArchive)):
            externalArchive[j].crowdingDistance = 0;

        for i in xrange(0, len(problems)):
            for j in range(0, len(externalArchive)):
                externalArchive[j].comparableDimension = i;

            if problems[i] == "min":
                externalArchive = sorted(externalArchive, key = lambda particle: particle.vector[i]);
            else:
                externalArchive = sorted(externalArchive, key = lambda particle: particle.vector[i], reverse = True);
            
            for j in xrange(0, len(externalArchive)):
                externalArchive[j].crowdingDistance = DominanceEvaluator.calculateCrowdingDistanceByDimension(externalArchive[j], externalArchive, i, j);

        externalArchive = sorted(externalArchive, key = lambda particle: particle.crowdingDistance, reverse = True);
        
        return externalArchive;
    
    @staticmethod
    def calculateCrowdingDistanceByDimension(particle, externalArchive, dimension, index):
        crowdingDistance = particle.crowdingDistance;

        valueMax = DominanceEvaluator.getDimensionMaxValue(externalArchive, dimension);
        valueMin = DominanceEvaluator.getDimensionMinValue(externalArchive, dimension);
        delta = math.fabs(valueMax - valueMin);

        #soh para 2 problemas
        size = len(externalArchive[0].vector) - 2;

        if len(externalArchive) >= 2 and delta != 0.0:
            if index == 0:
                crowdingDistance = crowdingDistance + (math.fabs(externalArchive[index].vector[size +dimension] - 
                                externalArchive[index + 1].vector[size +dimension]) + math.fabs(externalArchive[-1].vector[size +dimension] - 
                                externalArchive[index].vector[size +dimension])) / delta;
            elif index == len(externalArchive) - 1:
                crowdingDistance = crowdingDistance + (math.fabs(externalArchive[index].vector[size +dimension] - 
                                   externalArchive[0].vector[size +dimension]) + math.fabs(externalArchive[index - 1].vector[size +dimension] - externalArchive[index].vector[size +dimension])) / delta;
            else:
                crowdingDistance = crowdingDistance + (math.fabs(externalArchive[index].vector[size +dimension] - externalArchive[index + 1].vector[size +dimension]) +
                        math.fabs(externalArchive[index - 1].vector[size +dimension] - externalArchive[index].vector[size +dimension])) / delta;
        else:
            crowdingDistance = 0.0;

        return crowdingDistance;
    
    @staticmethod
    def getDimensionMaxValue(externalArchive, dimension):
        maxValue = 0;

        for j in xrange(0, len(externalArchive)):
            
            #soh para 2 problemas
            size = len(externalArchive[j].vector) - 2;
            if externalArchive[j].vector[size + dimension] > maxValue:
                maxValue = externalArchive[j].vector[size + dimension];
        return maxValue;

    @staticmethod
    def getDimensionMinValue(externalArchive, dimension):
        minValue = sys.maxint;

        for j in xrange(0, len(externalArchive)):
            #soh para 2 problemas
            size = len(externalArchive[j].vector) - 2;
            if externalArchive[j].vector[size + dimension] < minValue:
                minValue = externalArchive[j].vector[size + dimension];
        return minValue;

    @staticmethod
    def verifyDominance(instances, problems):
        obj_instances = DominanceEvaluator.__createInstances(instances);
        
        size = len(obj_instances);
        
        for i in range(0, size):
            if (not obj_instances[i].dominated):

                for j in range(0, size):
                    if obj_instances[i] != obj_instances[j] and not obj_instances[j].dominated:
                        dominance = DominanceEvaluator.__verifyDominance(obj_instances[i].vector, obj_instances[j].vector, problems);

                        if (dominance == Dominance.DOMINATES):
                            obj_instances[j].dominated = True;
                        elif (dominance == Dominance.DOMINATED):
                            obj_instances[i].dominated = True;
                            j = size;
        filtered_operators = filter(lambda op: op.dominated  == False, obj_instances);
        return filtered_operators;
        
    @staticmethod
    def __verifyDominance(instance1, instance2, problems):
        lostInAllDimension = True;
        winInAllDimension = True;

        size = len(instance1) - len(problems);
        for j in range(0, len(problems)):
            
            first_ins = instance1[size +j];
            second_ins = instance2[size +j];
            if(problems[j] == "min"):
                if (first_ins > second_ins):
                    winInAllDimension = False;

                    if (not lostInAllDimension):
                        return Dominance.INCOMPARABLE;

                elif (first_ins < second_ins):
                    lostInAllDimension = False;

                    if (not winInAllDimension):
                        return Dominance.INCOMPARABLE;

            elif(problems[j] == "max"):
                if (first_ins < second_ins):
                    winInAllDimension = False;

                    if (not lostInAllDimension):
                        return Dominance.INCOMPARABLE;

                elif (first_ins > second_ins):
                    lostInAllDimension = False;

                    if (not winInAllDimension):
                        return Dominance.INCOMPARABLE;

        if (winInAllDimension and lostInAllDimension):
            return Dominance.INCOMPARABLE;

        if (winInAllDimension):
            return Dominance.DOMINATES;
        elif (lostInAllDimension):
            return Dominance.DOMINATED;
        else:
            return Dominance.INCOMPARABLE;
        
class Dominance(object):
    INCOMPARABLE = 0;
    DOMINATES = 1;
    DOMINATED = -1;