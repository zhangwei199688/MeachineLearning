import csv
import KNN
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def classify0(inX,dataSet,labels,k):
        dataSetSize=dataSet.shape[0]
        diffMat=tile(inX,(dataSetSize,1))-dataSet
        sqrdiffMat=diffMat**2
        sqDistance=sqrdiffMat.sum(axis=1)
        Distance=sqDistance**0.5
        sortedDistIndicies=argsort(Distance)
        classCount={}
        for i in range(k):
            votelabel=labels[sortedDistIndicies[i]]
            classCount[votelabel]=classCount.get(votelabel,0)+1
        max=0
        for key in classCount:
            if classCount[key]>max:
                max=classCount[key]
                class1=key
        return class1


def fileprocess(filename):
    with open("D:\学习资料\Kaggle\data\\"+filename,"r") as csvfile:
        read=csv.reader(csvfile)
        readline=[]
        for i in read:
            readline.append(i)


    readline.pop(0)
    numbers=len(readline)
    array=zeros((numbers,2))
    labels=[]
    index=0
    for line in readline:
        labels.append(line[1])

        array[index,0:]=float(line[5])
        array[index,1:]=float(line[9])
        index+=1
    return array,labels

datarray,labels=fileprocess("train.csv")

def testprocess(filename):
    with open("D:\学习资料\Kaggle\data\\"+filename,"r") as csvfile:
        read=csv.reader(csvfile)
        readline=[]
        for i in read:
            readline.append(i)
    readline.pop(0)
    numbers=len(readline)
    array=zeros((numbers,2))
    index=0
    indexlist=[]
    for line in readline:
        array[index,0]=float(line[4])
        array[index,1]=float(line[8])
        indexlist.append(line[0])
        index+=1
    return array,numbers,indexlist
testarray,num,indexlist=testprocess("test.csv")
k=20
resultlist=[]
for i in range(num):
    resultlist0=[]
    inX=testarray[i,]
    result=classify0(inX,datarray,labels,k)
    resultlist0.append(indexlist[i])
    resultlist0.append(result)
    resultlist.append(resultlist0)

with open("D:\学习资料\Kaggle\data\\result.csv","w") as fp:
    writer=csv.writer(fp)
    for list in resultlist:
        writer.writerow(list)
#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.scatter(datarray[:,0],datarray[:,1],c=labels,s=50)
#plt.show()