'''
Created on 02/01/2012

@author: periclesmiranda
'''
#from scikits.learn.svm import SVC
#from pybrain.tools.shortcuts import buildNetwork

class Experiment(object):

    def __init__(self, type):
        if type == "svm":
            self.__svm_setup()
        elif type == "mlp":
            self.__mlp_setup()
        elif type == "stub":
            self.__stub_setup()

    def __svm_setup(self):
        #self.clf = SVC();
        self.params = [[-5, 15], [-15, 3]]
        
    def __mlp_setup(self):
        self.clf = None;
        self.params = [[2,100],[0.01,0.5],[0,1]]
        
    def __stub_setup(self):
        self.clf = None;
        self.params = [[-5, 15], [-15, 3]]