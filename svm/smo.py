"""
An Implementation of John Platt's SMO algorithm in python 
Author : Vivek Mishra
"""
import random as rd
import numpy as np

def loadDataSet(fileName):
	X = []; labels = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = line.strip().split('\t')
		X.append([float(lineArr[0]), float(lineArr[1])])
		labels.append(float(lineArr[2]))
	return X,labels

def selectRandJ(i,m):
	start = 1
	r=range(start, i) + range(i+1, m)
	return rd.choice(r)

def BoundAplhaj(H,L,aj):
	if aj>H:
		aj=H
	if aj<L:
		aj=L
	return aj


def computeLH(lablesI,labelsJ,alphaI,alphaJ,C):
	if lablesI !=labelsJ:
		L = max(0, alphaJ-alphaI ); H = min(C, C + alphaJ-alphaI)
	else:	
		L = max(0, alphaI+alphaJ-C ); H = min(C,alphaI+alphaJ)
	return H,L	


def SimplifiedSMO(X,labels,C,tol,max_passes):
	m,n=np.shape(np.mat(X))
	X = np.mat(X)
	labels = np.mat(labels).transpose()
	alphas=np.mat(np.zeros((m,1)))
	b=0
	passes=0
	

	while (passes < max_passes):
		num_changed_alphas = 0.

		for i in range(m):
 			fXi = float(np.multiply(alphas,labels).T*(X*X[i,:].T)) + b
 			Ei=fXi-float(labels[i])

			if ((labels[i]*Ei<-tol and alphas[i]< C) or (labels[i]*Ei >tol and alphas[i]> 0)):
				j=selectRandJ(i,m)

				fXj = float(np.multiply(alphas,labels).T*(X*X[j,:].T)) + b
 				Ej=fXj-float(labels[j])
		
				#saving old alphas 
				alphaIold=alphas[i].copy()
				alphaJold=alphas[j].copy()

				H,L=computeLH(labels[i],labels[j],alphas[i],alphas[j],C)
				if (L == H): print "L==H"; continue


				eta=2.0*(X[i,:]*X[j,:].T)-(X[i,:]*X[j,:].T-(X[i,:]*X[j,:].T))
				if eta>=0 : print "eta>=0" ; continue

				alphas[j]-=labels[j]*(Ei-Ej)/eta
				alphas[j]=BoundAplhaj(H,L,alphas[j])

			
				if (abs(alphas[j] - alphaJold) < 0.00001): print "j not moving enough" ; continue

				alphas[i] += labels[j]*labels[i]*(alphaJold - alphas[j]) 

				b1=b-Ei-labels[i]*(alphas[i]-alphaIold)*(X[i,:]*X[i,:].T)-labels[j]*(alphas[j]-alphaJold)*(X[i,:]*X[j,:].T)

				b2=b-Ej-labels[i]*(alphas[i]-alphaIold)*(X[i,:]*X[j,:].T)-labels[j]*(alphas[j]-alphaJold)*(X[j,:]*X[j,:].T)


				if (0 < alphas[i]) and (C > alphas[i]): b = b1	
 				elif (0 < alphas[j]) and (C > alphas[j]): b = b2
 				else: b = (b1 + b2)/2.0 
				
				num_changed_alphas+=1	
		

		if (num_changed_alphas == 0):
			passes = passes + 1
		else:
			passes = 0		

	return b,alphas