########################################################################
#                                                                           
#                                                                    
#                    MNIST data set reader and serializer
#                             mnist.py                                      
#                                                                           
#                                MAIN                                      
#                                                                           
#                 Copyright (C) 2009 Ulrik Hoerlyk Hjort                   
#                                                                           
#  MNIST data set reader and serializer is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  MNIST data set reader and serializer is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################        

from PIL import Image
import numpy as np 
import gzip
import pickle

############################################################################
#
# 
#
############################################################################
class MNIST :

    ########################################################################
    #
    # 
    #
    ########################################################################
    def __init__(self):
        self.trainLabels = []
        self.testLabels = []
        self.trainImages = []
        self.testImages = []
        self.testImageInfo = None
        self.trainImageInfo = None

        self.trainLabelsFile = "./data/train-labels-idx1-ubyte.gz"
        self.testLabelsFile = "./data/t10k-labels-idx1-ubyte.gz"
        self.trainImagesFile = "./data/train-images-idx3-ubyte.gz"
        self.testImagesFile = "./data/t10k-images-idx3-ubyte.gz"
        self.pickleFile = "./data/dataset.pkl.gz"   



    ########################################################################
    #
    # 
    #
    ########################################################################
    def getData(self):
        return (self.trainImages, self.trainLabels, self.testImages. self.testLabels, self.trainImageInfo, self.testImageInfo)

   
    ########################################################################
    #
    # 
    #
    ########################################################################
    def readLabels(self,filename, labels):
        with gzip.open(filename,'rb') as f: 
            assert int.from_bytes(f.read(4),'big') == 0x00000801, 'Error in magic number in ' + filename
            
            numberOfLabels = int.from_bytes(f.read(4),'big')
        
            for _ in range(numberOfLabels):
                labels.append(int.from_bytes(f.read(1), 'big'))
            
        
    ########################################################################
    #
    # 
    #
    ########################################################################
    def readImages(self,filename, images):
        with gzip.open(filename,'rb') as f:
            assert int.from_bytes(f.read(4),'big') == 0x00000803, 'Error in magic number in ' + filename
            numberOfImages = int.from_bytes(f.read(4),'big') 
            numberOfRows = int.from_bytes(f.read(4),'big')
            numberOfColumns = int.from_bytes(f.read(4),'big')

            for _ in range(numberOfImages):
                rows = []
                for _ in range(numberOfRows):
                    cols = []
                    for _ in range(numberOfColumns):
                        cols.append(int.from_bytes(f.read(1), 'big')) 
                    rows.append(cols) 
                images.append(rows) 
            return (numberOfRows, numberOfColumns, numberOfImages)

    ########################################################################
    #
    # 
    #
    ########################################################################
    def readData(self):
        self.trainLabels = []
        self.testLabels = []
        self.trainImages = []
        self.testImages = []
        self.readLabels(self.trainLabelsFile, self.trainLabels)
        self.readLabels(self.testLabelsFile, self.testLabels)
        self.trainImageInfo = self.readImages(self.trainImagesFile, self.trainImages)
        self.testImageInfo =self.readImages(self.testImagesFile, self.testImages)

    ########################################################################
    #
    # 
    #
    ########################################################################
    def serializeData(self):
        pickleOut = gzip.open(self.pickleFile,"wb")
        pickle.dump((self.trainLabels, self.testLabels, self.trainImages, self.testImages, self.testImageInfo, self.trainImageInfo), pickleOut)
        pickleOut.close()

    ########################################################################
    #
    # 
    #
    ########################################################################
    def deSerializeData(self):        
        pickleIn = gzip.open(self.pickleFile,"rb")
        self.trainLabels, self.testLabels, self.trainImages, self.testImages, self.testImageInfo, self.trainImageInfo = pickle.load(pickleIn)


    ########################################################################
    #
    # 
    #
    ########################################################################
    def serializeDataSet(self):        
        self.readData()
        self.serializeData()

    ########################################################################
    #
    # 
    #
    ########################################################################
    def printout(self, index, save=False):
        print (self.trainLabels[index])
        for row in self.trainImages[index]:
            for column in row: 
                print('. ' if column <= 127 else '# ', end='')
            print()

        img = Image.fromarray(np.array(self.trainImages[index]).astype('uint8'))
        img = img.convert('RGB') 
        img.show()
        if save:
            img.save('train' + str(index) + '.png') 
