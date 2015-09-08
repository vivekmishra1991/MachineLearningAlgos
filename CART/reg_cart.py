import numpy as np
from numpy import *

def loadData(fileName):
    dataMat=[]	
    f=open(fileName)
    for line in f.readlines():
	    line=line.strip().split('\t')
	    fltLine=map(float,line)
	    dataMat.append(fltLine)
    dataMat=np.mat(dataMat)
    return dataMat


def binSplit(dataset,feat,val):
    mat0= dataset[np.nonzero(dataset[:,feat]>val)[0],:][0]                       
    mat1= dataset[np.nonzero(dataset[:,feat]<=val)[0],:][0]
    return mat0,mat1


def regLeaf(dataSet):
    return np.mean(dataSet[:,-1])	



def regErr(dataset):
    return np.var(dataset[:,-1])*np.shape(dataset)[0]


def chooseBestSplit(dataset,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS=ops[0]; tolN=ops[1]
    if len(set(dataset[:,-1].T.tolist()[0]))==1:
        return None,leafType(dataset)
    m,n = shape(dataset)
    S = errType(dataset)
    bestS = inf; bestIdX=0; bestVal=0
    for featIdx in range(n-1):
        for splitVal in set(dataset[:,featIdx]):
            mat0,mat1=binSplit(dataset,featIdx,splitVal)
            if (shape(mat0)[0]<tolN ) or (shape(mat1)[0]<tolN): continue
            newS=errType(mat0)+errType(mat1)
            if newS < bestS:
                bestIdx=featIdx
                bestVal=splitVal
                bestS=newS
   #if the decrease (S-bestS) is less than a threshold don't do the split
    if (S - bestS) < tolS:
       return None,leafType(dataset)
    mat0,mat1 = binSplit(dataset,bestIdx,bestVal)
    if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
       return None,leafType(dataset)
    return bestIdx,bestVal



def createTree(dataset,leafType=regLeaf,errType=regErr,ops=(1,4)):
    feat,val=chooseBestSplit(dataset,leafType,errType,ops)
	
    if feat==None: return val
    retTree={}
    retTree['spIdx']=feat
    retTree['spVal']=val	
	
    lSet, rSet = binSplit(dataset, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree















