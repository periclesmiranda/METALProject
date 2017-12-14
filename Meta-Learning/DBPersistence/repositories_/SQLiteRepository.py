'''
Created on 03/09/2011

@author: periclesmiranda
'''

from util_.Util import Util

class SQLiteRepository(object):
    
    def __init__(self, conn, cursor):
        self.conn = conn;
        self.cursor = cursor;
    

    def save( self, table_name, data ):
            query = 'insert into ' + table_name + ' values ' + Util.formatValuesAccording(len(data));
            self.execute(self.conn, self.cursor, query, data);
        
    def clear(self, table_name):
        query = 'delete from ' + table_name;
        self.execute(self.conn, self.cursor, query);
        
    def delete_table(self, table_name):
        query = 'drop table ' + table_name;
        self.execute(self.conn, self.cursor, query);
        
    def delete(self, table_name, column, keyword):
        query = 'delete from ' + table_name + ' where ' + column + '=?';
        self.execute(self.conn, self.cursor, query, (keyword,));
        
    def database(self, table_name):
        self.cursor.execute('select * from ' + str(table_name));
        return self.cursor.fetchall();
    
    def show(self, table_name):
        db = self.database(table_name);
        for line in db: print(str(line) + '\n')
        
    def showAccording(self, table_name, column, keyword):
        query = 'select * from ' + table_name + ' where ' + column + '=?';
        self.execute(self.conn, self.cursor, query, (keyword,));
        db = self.cursor.fetchall();
        for line in db: print(str(line) + '\n')
       
    def execute(self, conn, cursor, query, data=None):
        #try:
            cursor.execute(query, () if data == None else data);
            conn.commit();
        #except:
        #    conn.rollback();
