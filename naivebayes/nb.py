import numpy as np


def loadDataSet():
		postingList=[['my', 'dog', 'has', 'flea', \
		'problems', 'help', 'please'],
		['maybe', 'not', 'take', 'him', \
		'to', 'dog', 'park', 'stupid'],
		['my', 'dalmation', 'is', 'so', 'cute', \
		'I', 'love', 'him'],
		['stop', 'posting', 'stupid', 'worthless', 'garbage'],
		['mr', 'licks', 'ate', 'my', 'steak', 'how',\
		'to', 'stop', 'him'],
		['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
		classVec = [0,1,0,1,0,1]
		#1 is abusive, 0 not
		return postingList,classVec


def createVocabList(dataset):
		vocabSet=set([])
	
		for document in dataset:
			vocabSet=vocabSet | set(document)
    
    		return list(vocabSet)


def set2Vec(vocabList,input):
	
	retrunVec=len(vocabList)*[0]

	for word in vocabList:
		if word in input:
			retrunVec[vocabList.index(word)]=1
		else:
			#print "%s not in list" %word
			pass

	return retrunVec





def trainNB(trainMatrix,trainClass):
	numWords=len(trainMatrix[1])

	pAbusiveDoc=float(sum(trainClass))/len(trainClass)
	print pAbusiveDoc
	
	#intialization
	p0Num=np.ones(numWords); p1Num=np.ones(numWords)
	p0Denom=2.0 ;p1Denom=2.0

	for i in range(len(trainClass)):
		if trainClass[i]==1:
			p1Num+=trainMatrix[i]
			p1Denom+=sum(trainMatrix[i])
		else:
			p0Num+=trainMatrix[i]
			p0Denom+=sum(trainMatrix[i])
	
	p0V=np.log(p0Num/p0Denom)		
	p1V=np.log(p1Num/p1Denom)		

	return pAbusiveDoc,p0V,p1V

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
	p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
	p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0




listOPosts,listClasses = loadDataSet()
myVocabList = createVocabList(listOPosts)
trainMat=[]
for postinDoc in listOPosts:
	trainMat.append(set2Vec(myVocabList, postinDoc))



pAb,p0V,p1V=trainNB(trainMat,listClasses)




testEntry = ['stupid', 'my']
thisDoc = np.array(set2Vec(myVocabList, testEntry))
print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)