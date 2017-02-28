import re
import numpy
import numpy as np
from scipy import stats
import scipy.stats as st
import sys
import csv
import os

fn0 = 'Midway_AllPackages.csv'
with open(fn0, 'r') as myfile:
    skylineFile = csv.reader(myfile, dialect='excel')
    dataAll = []
    for row in skylineFile:
        dataAll.append(row)
    myfile.close()

fn1 = 'Midway1_R_3.2.1_pack_installed.csv'
with open(fn1, 'r') as myfile:
    skylineFile = csv.reader(myfile, dialect='excel')
    dataMid1 = []
    for row in skylineFile:
        dataMid1.append(row)
    myfile.close()

fn2 = 'Midway2_R_3.3.2_pack_installed.csv'
with open(fn2, 'r') as myfile:
    skylineFile = csv.reader(myfile, dialect='excel')
    dataMid2 = []
    for row in skylineFile:
        dataMid2.append(row)
    myfile.close()


def Merge(dat,datMid):
    i=0
    MidwayMerge=[]
    while i<len(dat):
        j=0
        while j<len(datMid):
            if dat[i][0] == datMid[j][0]:
                MidwayMerge.append(datMid[j][1])
                break
            else:
                if j==len(datMid)-1:
                    MidwayMerge.append('NA')
            j+=1
        
        i+=1
    return MidwayMerge


midway1=Merge(dataAll, dataMid1)
midway2=Merge(dataAll, dataMid2)
fn = 'MidwayMatch_Rpackages.csv'
with open(fn, 'wb') as myfile:
    outputFile = csv.writer(myfile)
    i=1
    outputFile.writerow(['Midway Package', 'Midway 1 Package Version', 'Midway 2 Package Version'])
    while i<len(midway1):
        outputFile.writerow([dataAll[i][0], midway1[i], midway2[i]])
        
        i+=1
        
    myfile.close()

