from numpy import *
import operator


def classify0(self,inX,dataSet,labels,k):
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


