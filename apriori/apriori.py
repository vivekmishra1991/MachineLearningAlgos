def loadDataset(filename):
	dataMat=[]
	fr=open(filename)
	for line in fr.readlines():
	    curline=line.strip().split()
	    dataMat.append(curline)			
	return dataMat
