from math import log

def majorityCnt(classlist):
    classcount={}
    for value in classlist:
        if value not in classcount.key():
            classcount[value]=0
        classcount+=1

    max=0
    for value in classcount:
        if classcount[value]>max:
            max=classcount[value]
            result=value
    return result

def classshannonEnt(dataSet): #calculate shannonEnt
    number=len(dataSet)
    labelcount={}
    for line in dataSet:
        label=line[-1]
        if label not in labelcount.keys():
            labelcount[label]=0
        labelcount[label]+=1
    shannonEnt=0.0
    for key in labelcount:
        props=float(labelcount[key])/number
        shannonEnt -= props * log(props,2)
    return shannonEnt

def SplitDataSet(dataSet,axis,value):
    retdataset=[]
    for line in dataSet:
        if line[axis]==value:
            reduceFeatVec=line[:axis]
            reduceFeatVec.extend(line[axis+1:])
            retdataset.append(reduceFeatVec)
    return retdataset

def chooseBestFeatureTopSplit(dataSet):
    numFeatures=len(dataset[0])-1
    baseEntropy=classc(dataSet)
    bestInfoGain=0.0 bestFeature=-1
    for i in range(numFeatures):
        featlist=[example[i] for example in dataSet]
        uniquefeat=set(featlist)
        newEntropy=0.0
        for value in uniquefeat:
            subdataSet=SplitDataSet(dataSet,i,value)
            prob=len(subdataSet)/float(len(dataSet))
            newEntropy +=prob * classshannonEnt(subdataSet)
        infoGain=baseEntropy-newEntropy
        if (infoGain>bestInfoGain):
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

def createTree(dataSet,labels):
    classlist=[example[-1] for example in dataSet]
    if classlist.count(classlist[0])==len(classlist):
        return classlist[0]
    if len(dataSet[0])==1:
        return majorityCnt(classlist)
    BestFeat=chooseBestFeatureTopSplit(dataSet)
    bestFeatLabel=labels[BestFeat]
    myTree={bestFeatLabel:{}}
    del(label[BestFeat])
    valuelist=[example[BestFeat] for example in dataSet]
    Unique=set(valuelist)
    for value in Unique:
        sublabels=labels[:]
        myTree[bestFeatLabel][value]=creatTree(SplitDataSet(dataSet,BestFeat,value),sublabels )
    return myTree

def classify(inputTree,featLabels,testVec):
    firstStr=inputTree.key()[0]
    secondDict=inputTree[firstStr]
    featIndex=featLabels.index(firstStr)
    for key in secondDict.key():
        if testVec[featIndex]==key:
            if type(secondDict[key]).__name__=="dict":
                classify(secondDict[key],featLabels.testVec)
            else:
                return secondDict[key]



def createdataSet():  #testing...delete later
    detaSet=[[1,1,"yes"],[1,0,"no"],[0,1,"no"],[0,1,"no"]]
    test=SplitDataSet(detaSet,0,1)
    print(test)

createdataSet()

