# -*- coding: UTF-8 -*-

'''
Created on 15/09/2011

@author: periclesmiranda
'''


from DBRepository import DBRepository
from services.DBService import DBService
from StatisticsService import StatisticsService
import os
from Experiment import Experiment
from creation.SVMDBCreator import SVMDBCreator
#from creation.MLPDBCreator import MLPDBCreator
#from creation.StubDBCreator import StubDBCreator
from suggestion.SingleSolutionSuggester import SingleSolutionSuggester
#from suggestion.MultipleSolutionSuggester import MultipleSolutionSuggester

class Facade(object):

    def __init__(self, experiment_type="svm", db_name="db_name", n_objectives="single"):
        self.dbRepository = DBRepository();
        
        self.statsService = StatisticsService();
        
        self.__db_setup(db_name)
        
        self.experiment = Experiment(experiment_type)
        
        if n_objectives == "single": self.solutionSuggester = SingleSolutionSuggester()
#        elif n_objectives == "multiple": self.solutionSuggester = MultipleSolutionSuggester()
        
        if experiment_type == "svm": self.dbCreator = SVMDBCreator(self.dbService, self.statsService)
#        elif experiment_type == "mlp": self.dbCreator = MLPDBCreator(self.dbService, self.statsService)
#        elif experiment_type == "stub": self.dbCreator = StubDBCreator(self.dbService, self.statsService)
        
    def __db_setup(self, db_name):
        
        
        self.path = "C:/Users/Péricles/Documents/Projetos - Eclipse/Projects/Meta-Learner/src/datasets/";
        
        self.table_features = "table_features";
        self.table_operators = "table_operators";
        
        self.db_name = db_name
        self.path = self.path + db_name;
        
        self.dbService = DBService(self.path);
    
    def createMetaBase(self, tables_created=True):
        if not os.path.exists(self.path) or (not tables_created):
            self.dbCreator.create_db(self.table_features, self.table_operators);
            
        for db in self.dbRepository.databases:
            print db[0] + "sendo criada";
            self.dbCreator.populate(db[0], self.table_features, self.table_operators, self.experiment.clf, self.experiment.params, db[1]);
            print db[0] + " finalizada";
            
    def createMetaBaseFrom(self, features_path, operators_path, tables_created=True):
        self.dbCreator.create_db(self.table_features, self.table_operators);
            
        self.dbCreator.populate(self.db_name, self.table_features, self.table_operators, features_path, operators_path, self.experiment.params)
    
    def createConfigMatrix(self, filter=None):
        return self.dbCreator.createMatrix(self.table_operators, filter)
            
    def generateSuggestions(self, feature, dbs_per_features, dbs_per_operators, n_suggestions, n_problems=None):
        return self.solutionSuggester.generate_suggestions(feature, dbs_per_features, dbs_per_operators, n_suggestions, n_problems)
                    