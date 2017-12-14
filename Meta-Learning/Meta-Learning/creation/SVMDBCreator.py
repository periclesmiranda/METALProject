'''
Created on 02/01/2012

@author: periclesmiranda
'''
from creation.DBCreator import DBCreator
from extraction.SVMFeaturesExtractor import SVMFeaturesExtractor
import math
import numpy

class SVMDBCreator(DBCreator):

    def __init__(self, dbService, statsService):
        super(SVMDBCreator, self).__init__(dbService, statsService);
        self.featureExtractor = SVMFeaturesExtractor(statsService);
    
    def create_db(self, table_features, table_operators):
        self.cursor.execute('create table ' + table_features + '(db_name varchar(30), n_examples int, n_att int, n_class int, mean_corr real, gmean real, skewness real, kurtosis real, entropy real)');
        #self.cursor.execute('create table ' + table_operators + '(db_name varchar(30), c real, gamma real, classification_rate real, n_support_vectors int)');
        self.cursor.execute('create table ' + table_operators + '(db_name varchar(30), c real, gamma real, classification_rate real)');
            
    def populate(self, db_name, table_features, table_operators, classifier, params, data):
        self.__populate_features(db_name, table_features, data);
        self.__populate_operators(db_name, table_operators, classifier, params, data);
            
    def __populate_features(self, db_name, table_features, data):
        features = self.featureExtractor.extract(data);
        
        self.dbService.save(table_features, db_name, features[0], features[1], 
                          features[2], features[3], features[4], features[5], features[6],
                          features[7]);
    
    def __populate_operators(self, db_name, table_operators, clf, params, data):
        classifier = clf.fit(data.data, data.target);
        
        count = 0
        
        #We can define the interval (In this case, 0.5)
        c_params = numpy.arange(params[0][0], params[0][1] +1, 0.5)
        gamma_params = numpy.arange(params[1][0], params[1][1] +1, 0.5)
        
        for p1 in c_params:
            classifier.C = 2**p1;
            for p2 in gamma_params:
                classifier.gamma = 2**p2;
                
                count += 1
                
                print(count)
                scores = self.featureExtractor.evaluateScores(classifier, data, 10);
                #self.dbService.save(table_operators, db_name, classifier.C, classifier.gamma, scores[0], scores[1]);
                self.dbService.save(table_operators, db_name, classifier.C, classifier.gamma, scores[0]);
                
    def createMatrix(self, table_operators, filtering=None):
        instances = self.dbService.database(table_operators);
        
        temp = []
        temp_set = set()
        
        for item in instances:
            if filtering != None:
                if item[0] not in filtering:
                    temp_set.add(item[0])
            else:
                temp_set.add(item[0])
        
        for item in temp_set:
            per_name = filter(lambda x: x[0] == item, instances)
            
            temp.append(per_name)
        
        instances = []
        items = [];
        
        for instance in temp:
            for item in instance:
                items.append([item[0], math.log(item[1],2), math.log(item[2], 2), item[3]]);
            instances.append(items)
            items = []
        return instances;
    