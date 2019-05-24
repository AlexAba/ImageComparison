from PIL import Image
import glob
import numpy
from scipy.spatial import distance
import sys

def main():
    #   Path, where images stored.
    path  = "../../dev_dataset"
    imageList = GetImages(path)
    chekedImages = []
    for im1 in imageList:
        for im2 in imageList:
            if(im1.filename != im2.filename) and (im2 not in chekedImages):
                arr1 = numpy.asarray(im1.histogram())
                arr2 = numpy.asarray(im2.histogram())
                dist =  abs(distance.euclidean(arr1, arr2))
                if(dist <= 10000):
                    chekedImages.append(im1)
                    print(im1.filename + "\t\t" + im2.filename)

def GetImages(path):
    imageList = []
    for file in glob.glob(path + "/*.jpg"):
        im = Image.open(file)
        imageList.append(im)
    return imageList

main()