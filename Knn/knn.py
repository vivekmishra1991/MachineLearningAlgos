# coding: utf-8
from numpy import *
import operator
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def knnClassify(inp,dataset,labels):

	size=dataset.shape[0]
	   
	diff=tile(inp,(size,1))-dataset
	sqdiff=diff**2
	sqDiffSum=sqdiff.sum(axis=1)
	dist=sqDiffSum**0.5
	sortedDistIdx=dist.argsort()
	classCount={}
    
    
	for i in range(3):
    		voteIlabel = labels[sortedDistIdx[i]]
    		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]


dataset,labels=createDataSet()
print knnClassify([0,0],dataset,labels)
