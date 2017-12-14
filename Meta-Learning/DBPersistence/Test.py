'''
Created on 03/09/2011

@author: periclesmiranda
'''

from sqlite3 import dbapi2 as sqlite
from services import DBService
from services.IOService import IOService

if __name__ == '__main__':
    pass

'''
conn = sqlite.connect("teste.db");
cu = conn.cursor();
#cu.execute('create table Pessoa(idade int, name varchar(30))');
'''

dbService = DBService.DBService('C:/Documents and Settings/periclesmiranda/Meus documentos/eclipse-jee-ganymede-SR2-win32/Projects/DBPersistence/src/datasets/final')
dbService.show('table_features')
