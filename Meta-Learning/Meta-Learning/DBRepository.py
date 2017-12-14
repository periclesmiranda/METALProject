'''
Created on 15/09/2011

@author: periclesmiranda
'''
'''
from scikits.learn.datasets import load_iris
from scikits.learn.datasets import load_cancer
from scikits.learn.datasets import load_glass
from scikits.learn.datasets import load_sonar
from scikits.learn.datasets import load_wine
from scikits.learn.datasets import load_balance_scale
from scikits.learn.datasets import load_blood
from scikits.learn.datasets import load_breast_w
from scikits.learn.datasets import load_breasttissue
from scikits.learn.datasets import load_colic
from scikits.learn.datasets import load_colon
from scikits.learn.datasets import load_column_2c
from scikits.learn.datasets import load_column_3c
from scikits.learn.datasets import load_ecoli
from scikits.learn.datasets import load_haberman
from scikits.learn.datasets import load_heart
from scikits.learn.datasets import load_heart_statlog
from scikits.learn.datasets import load_hepatitis
from scikits.learn.datasets import load_hillvalley
from scikits.learn.datasets import load_hypothyroid
from scikits.learn.datasets import load_ionosphere
from scikits.learn.datasets import load_kr_vs_kp
from scikits.learn.datasets import load_letter
from scikits.learn.datasets import load_libras
from scikits.learn.datasets import load_lung_cancer
from scikits.learn.datasets import load_lymph
from scikits.learn.datasets import load_mamography
from scikits.learn.datasets import load_optdigits
from scikits.learn.datasets import load_parkinson
from scikits.learn.datasets import load_pen_digits
from scikits.learn.datasets import load_primary_tumor
from scikits.learn.datasets import load_prina_diabetes
from scikits.learn.datasets import load_red_wine_qual
from scikits.learn.datasets import load_segment
from scikits.learn.datasets import load_sick
from scikits.learn.datasets import load_vehicle
from scikits.learn.datasets import load_vote
from scikits.learn.datasets import load_white_wine_qual
from scikits.learn.datasets import load_yeast
from scikits.learn.datasets import load_zoo
'''

class DBRepository(object):

    def __init__(self):
        self.databases = [];
        
        '''
        self.databases.append(["balance_scale", load_balance_scale()]);
        self.databases.append(["blood", load_blood()]);
        self.databases.append(["breast_w", load_breast_w()]);
        self.databases.append(["breasttissue", load_breasttissue()]);        
        self.databases.append(["cancer", load_cancer()]);
        self.databases.append(["colic", load_colic()]);
        self.databases.append(["colon", load_colon()]);
        self.databases.append(["column_2c", load_column_2c()]);
        self.databases.append(["column_3c", load_column_3c()]);
        self.databases.append(["ecoli", load_ecoli()]);
        self.databases.append(["glass", load_glass()]);
        self.databases.append(["haberman", load_haberman()]);
        self.databases.append(["heart", load_heart()]);
        self.databases.append(["heart_statlog", load_heart_statlog()]);
        self.databases.append(["hepatitis", load_hepatitis()]);
        self.databases.append(["hillvalley", load_hillvalley()]);
        #self.databases.append(["hypothyroid", load_hypothyroid()]);#H
        self.databases.append(["ionosphere", load_ionosphere()]);
        self.databases.append(["iris", load_iris()]);
        #self.databases.append(["kr_vs_kp", load_kr_vs_kp()]);
        #self.databases.append(["letter", load_letter()]);
        #self.databases.append(["libras", load_libras()]);
        #self.databases.append(["lung_cancer", load_lung_cancer()]);
        self.databases.append(["lymph", load_lymph()]);
        #self.databases.append(["mamography", load_mamography()]);#H
        #self.databases.append(["optdigits", load_optdigits()]);#H
        self.databases.append(["parkinson", load_parkinson()]);
        #self.databases.append(["pen_digits", load_pen_digits()]);#H
        #self.databases.append(["primary_tumor", load_primary_tumor()]);#H
        self.databases.append(["prina_diabetes", load_prina_diabetes()]);
        #self.databases.append(["red_wine_qual", load_red_wine_qual()]);
        #self.databases.append(["segment", load_segment()]);
        #self.databases.append(["sick", load_sick()]);#H
        self.databases.append(["sonar", load_sonar()]);
        self.databases.append(["vehicle", load_vehicle()]);
        self.databases.append(["vote", load_vote()]);
        #self.databases.append(["white_wine_qual", load_white_wine_qual()]);#H
        self.databases.append(["wine", load_wine()]);
        #self.databases.append(["yeast", load_yeast()]);#H
        self.databases.append(["zoo", load_zoo()]);
        '''
        
        