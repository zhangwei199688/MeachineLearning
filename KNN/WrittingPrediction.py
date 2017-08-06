from __future__ import division
import os
from numpy import *

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqrdiffMat = diffMat ** 2
    sqDistance = sqrdiffMat.sum(axis=1)
    Distance = sqDistance ** 0.5
    sortedDistIndicies = argsort(Distance)
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    max = 0
    for key in classCount:
        if classCount[key] > max:
            max = classCount[key]
            class1 = key
    return class1

def img2vector(filename):
    vec=zeros((1,1024))
    with open(filename) as fp:
        for i in range(32):
            read=fp.readline()
            for j in range(32):
                vec[0,32*i+j]=int(read[j])
    return vec

def test():
    trainlabel,testlabel=[],[]
    trainfilelist = os.listdir(r"C:\Users\ZhangV\workshop\MachineLearning\KNN\data\\trainingDigits")
    trainarray=zeros((len(trainfilelist),1024))
    for i in range(len(trainfilelist)):
        trainarray[i, :] = img2vector(r"C:\Users\ZhangV\workshop\MachineLearning\KNN\data\\trainingDigits\\" + trainfilelist[i])
        trainlabel.append(trainfilelist[i].split("_")[0])

    testfilelist=os.listdir(r"C:\Users\ZhangV\workshop\MachineLearning\KNN\data\\testDigits")
    sucess,fail,k=0,0,20
    for j in range(len(testfilelist)):
        testimg=img2vector(r"C:\Users\ZhangV\workshop\MachineLearning\KNN\data\\trainingDigits\\" + testfilelist[j])
        predictlabel=classify0(testimg,trainarray,trainlabel,k)
        truelabel=testfilelist[j].split("_")[0]
        if predictlabel==truelabel:
            sucess+=1
            print("sucess:{0},total:{1}".format(sucess,(sucess+fail)))
        else:
            fail+=1

    total=float(sucess+fail)
    accuracy=float(sucess)/total
    print("accuracy:%f"%accuracy)

#sucess:911,total 946,accuracy:0.963002