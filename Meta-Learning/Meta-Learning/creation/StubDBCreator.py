'''
Created on 03/01/2012

@author: periclesmiranda
'''
from creation.DBCreator import DBCreator

class StubDBCreator(DBCreator):
    
    def __init__(self, dbService, statsService):
        super(StubDBCreator, self).__init__(dbService, statsService);
    
    def create_db(self, table_features, table_operators):
        self.cursor.execute('create table ' + table_features + '(db_name varchar(30), n_examples int, n_attrs int, ratio_examples int, corr_matrix int, corr_attr int, ratio_dev int, n_cont_attr int, prop_attr_out int, coe_var_targ int, targt_spar int, targt_out int, stat_targt int, r2_regr_without_sym int, r2_regr_with_byn int, avg_corr_attr int, avg_corr_attr_targt int, avg_disp_gain int, mean_diag int, var_diag int, kernel_targt int)');
        self.cursor.execute('create table ' + table_operators + '(db_name varchar(30), c real, gamma real, error_rate real)');
            
    def populate(self, db_name, table_features, table_operators, features_path, operators_path, params):
        features = self.__format(features_path)
        operators = self.__format(operators_path)
        
        self.__populate_features(db_name, table_features, features);
        self.__populate_operators(db_name, table_operators, operators, params);
    
    def __populate_features(self, db_name, table_features, features):
        for i in range(1, len(features)):
            self.dbService.save(table_features, features.keys()[i-1], features[i][0], features[i][1], 
                              features[i][2], features[i][3], features[i][4], features[i][5], features[i][6],
                              features[i][7],features[i][8],features[i][9],features[i][10],features[i][11],
                              features[i][12],features[i][13],features[i][14],features[i][15],features[i][16],
                              features[i][17],features[i][18],features[i][19]);
    
    def __populate_operators(self, db_name, table_operators, operators, params):
        for i in range(1, len(operators)):
            j = 0
            for p1 in range(params[0][0], params[0][1] +1):
                C = 2**p1;
                for p2 in range(params[1][0], params[1][1] +1):
                    gamma = 2**p2;
                    
                    self.dbService.save(table_operators, operators.keys()[i-1], C, gamma, operators[i][j]);
                    j += 1
            
    def createMatrix(self, table_operators):
        instances = self.dbService.database(table_operators);
        l = [];
        for i in range(0, len(instances)):
            li = list(instances[i]);
            l.append([li[0], li[1], li[2], li[3]]);
        return l;
            
    def __format(self, path):
        content = {}
        i = 1
        f = open(path, 'r')
        for line in f:
            content[i] = []
            
            curr_line = line.split('\t')
            for item in curr_line:
                content[i].append(float(item))
            i += 1
        return content
            