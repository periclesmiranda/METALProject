'''
Created on 03/09/2011

@author: periclesmiranda
'''
from repositories_.SQLiteRepository import SQLiteRepository
from sqlite3 import dbapi2 as sl

class DBService(object):

    def __init__(self, path):
        conn = sl.connect(path);
        self.cursor = conn.cursor();
        #self.cursor = None
        
        self.repository = SQLiteRepository(conn, self.cursor);
        pass
        
    def save(self, table_name, *data):
        self.repository.save(table_name, data);
        
    def clear(self, table_name):
        self.repository.clear(table_name);
        
    def delete_table(self, table_name):
        self.repository.delete_table(table_name)    
    
    def delete(self, table_name, column, keyword):
        self.repository.delete(table_name, column, keyword);
        
    def database(self, table_name):
        return self.repository.database(table_name);
        
    def show(self, table_name):
        self.repository.show(table_name);
        
    def showAccording(self, table_name, column, keyword):
        return self.repository.showAccording(table_name, column, keyword);

        