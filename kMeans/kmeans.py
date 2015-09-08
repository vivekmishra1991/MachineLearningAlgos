from numpy import * 

def loadData(file):
	datMat=[]
	fr=open(file)
	for line in fr.readlines():
		curline=line.strip().split('\t')
		fltline=map(float,curline)
		datMat.append(fltline)
	return mat(datMat)	

def euclidDist(VecA,VecB):
	return sqrt(sum(power((VecA - VecB),2)))

def randCent(dataSet,k):
	n=dataSet.shape[1]
	centroids=mat(zeros((k,n)))

	for j in range(n):
		minJ=min(dataSet[:,j])
		rangeJ=float(max(dataSet[:,j])-minJ)
		centroids[:,j]=mat(minJ+rangeJ * random.rand(k,1))
	return centroids

def kmean(dataSet,k,calcCent=randCent,distMeas=euclidDist):
	m=dataSet.shape[0]
	clusterAss=mat(zeros((m,2)))

	centroids=calcCent(dataSet,k)
	clusterChanged=True
	while clusterChanged:
		clusterChanged=False
		for i in range(m):
			minDist=Inf; minIndex=-1
			for j in range(k):
				distJI=distMeas(centroids[j,:],dataSet[i,:])
				if distJI<minDist: 
					minDist=distJI
					minIndex=j
			if clusterAss[i,0] !=minIndex: clusterChanged=True
			clusterAss[i,:]=minIndex,minDist**2
		print centroids

		for cent in range(k):
			ptsInClust=dataSet[nonzero(clusterAss[:,0].A==cent)[0]]
			centroids[cent,:]=mean(ptsInClust,axis=0)
	return centroids,clusterAss			
