'''
Created on 03/09/2011

@author: periclesmiranda
'''

class DBCreator(object):
    
    def __init__(self, dbService, statsService):
        self.dbService = dbService;
        self.cursor = self.dbService.cursor;
        #self.featureExtractor = FeaturesExtractor(statsService);
    
    def create_db(self, table_features, table_operators):
        pass
            
    def populate(self, db_name, table_features, table_operators, classifier, params, data):
        pass
    
    def createMatrix(self, table_operators):
        pass