import re
import numpy
import numpy as np
from scipy import stats
import scipy.stats as st
import sys
import csv
import os

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

i=0
MidwayMatch=[]
Midway2=[]
while i<len(dataMid2):
    j=0
    while j<len(dataMid1):
        if dataMid2[i][0] == dataMid1[j][0]:
            tempList=[]
            tempList=dataMid1[j]+dataMid2[i]
            MidwayMatch.append(tempList)
            break
        else:
            if j==len(dataMid1)-1:
                Midway2.append(dataMid2[i])
        j+=1
    i+=1

i=0
Midway1=[]
while i<len(dataMid1):
    j=0
    while j<len(dataMid2):
        if dataMid1[i][0] == dataMid2[j][0]:
            break
        else:
            if j==len(dataMid2)-1:
                Midway1.append(dataMid1[i])
        j+=1
    i+=1

fn = 'MidwayMatch_Rpackages.csv'
with open(fn, 'wb') as myfile:
    outputFile = csv.writer(myfile)
    i=1
    outputFile.writerow(['Midway 1 Package', 'Midway 1 Package Version', 'Midway 2 Package', 'Midway 2 Package Version'])
    while i<len(MidwayMatch):
        outputFile.writerows([MidwayMatch[i]])

        
        i+=1
        
    myfile.close()

fn = 'Midway1_R_3.2.1_unique.csv'
with open(fn, 'wb') as myfile:
    outputFile = csv.writer(myfile)
    i=1
    outputFile.writerow(['Midway 1 Package', 'Midway 1 Package Version'])
    while i<len(Midway1):
        outputFile.writerows([Midway1[i]])

        
        i+=1
        
    myfile.close()

fn = 'Midway2_R_3.3.2_unique.csv'
with open(fn, 'wb') as myfile:
    outputFile = csv.writer(myfile)
    i=1
    outputFile.writerow(['Midway 2 Package', 'Midway 2 Package Version'])
    while i<len(Midway2):
        outputFile.writerows([Midway2[i]])

        
        i+=1
        
    myfile.close()
