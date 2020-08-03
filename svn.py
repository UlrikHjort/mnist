import mnist
import numpy as np
from sklearn import svm

m = mnist.MNIST()

m.deSerializeData()

print("Go ...")
subSet = 20000
trainImages = np.array(m.trainImages[:subSet])
trainLabels = m.trainLabels[:subSet]

testImages = np.array(m.testImages[:subSet])
testLabels =  m.testLabels[:subSet]

nsamples, nx, ny = trainImages.shape
trainImages = trainImages.reshape((nsamples,nx*ny))

nsamples, nx, ny = testImages.shape
testImages = testImages.reshape((nsamples,nx*ny))

print("Fit ...")
clf = svm.SVC(kernel='rbf', C=1.0)
clf.fit(trainImages,trainLabels)

hits = 0
noOftests = 2000
print ("Running ...")
for i in range (noOftests):
	if trainLabels[i] == clf.predict([testImages[i]])[0]:
		hits += 1
	
print(str(hits*100/noOftests) +"% Hits")

print ("Done ...")