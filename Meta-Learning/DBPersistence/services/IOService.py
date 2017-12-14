'''
Created on 25/11/2011

@author: periclesmiranda
'''

import shelve as sh

class IOService(object):

    def __init__(self, path, file_name):
        self.path = path;
        self.file_name = file_name;
        self.file_path = path + file_name;
    
    def create(self, list_of_database):
        db = sh.open(self.file_path);
        if db == {}:
            for base in list_of_database:
                db[base[0]] = [];    
        db.close();
        
    def write(self, key, value, file_path):
        db = sh.open(file_path);
        
        db[key] = value;
        db.close();
        
    def read(self):
        db = sh.open(self.file_path);
        return db;
        
    
    '''
    
    
    def __write(self, key, value, file_name):
        with open(self.path + file_name, 'r+b') as f:
            f.seek(0);
            dic = cp.load(f);
            dic[key].append(value);
            return dic;
            
    def read(self, file_name):
        self.file_name = file_name;
        with open(self.path + file_name, 'rb') as f:
            f.seek(0);
            return cp.load(f);
    '''
    
    ''''
    def __init__(self, path, file_name):
        self.path = path;
        self.file_name = file_name;
        self.file_path = path + file_name;
    
    def create(self, dict):
        with open(self.file_path, 'r+b') as f:
            if f.read() == "":
                cp.dump(dict, f, protocol=-1);
    
    def write(self, key, value, file_name):
        dict = self.__write(key, value, file_name);
        with open(self.path + file_name, 'wb') as f:
            cp.dump(dict, f, protocol=-1);
    
    def __write(self, key, value, file_name):
        with open(self.path + file_name, 'r+b') as f:
            f.seek(0);
            dic = cp.load(f);
            dic[key].append(value);
            return dic;
            
    def read(self, file_name):
        self.file_name = file_name;
        with open(self.path + file_name, 'rb') as f:
            f.seek(0);
            return cp.load(f);
   '''