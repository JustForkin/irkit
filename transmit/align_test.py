from SimpleCV import *
#monkey patch the SimpleCV class to fix homography calculation in 
#Image.findKeypointMatch
from ImageClass2 import Image2 as Image 
import cv2
import cv
import numpy
import os

def align(img1, img2):
    """align img1 against img2 by applying a perspective warp transform"""
    h1,w1 = img1.size()
    h2,w2 = img2.size()
    h = min(h1,h2)
    w = min(w1,w2)
    
    #extract the homography matrix using keypoint matching
    #print "Finding matching features ..."
    match = img2.findKeypointMatch(img1)

    if match!=None:
        homo  = match[1]

        img1_array = numpy.array(img1.getMatrix())
        res_array = cv2.warpPerspective(src   = img1_array,
                                    M     = homo,
                                    dsize = (w,h),
                                    flags = cv2.INTER_CUBIC,
                                   )
                                   
        #res_img = Image(res_array,colorSpace = ColorSpace.RGB).toBGR()
        res_img = Image(res_array)
        return res_img
    else:
        return None

    
################################################################################
# TEST CODE
################################################################################    
if __name__ == "__main__":

    #IM1 = "test_images/a0.png"
    #IM2 = "test_images/a1.png"
    #IM1 = "test_images/wave1.jpg"
    #IM2 = "test_images/wave2.jpg"
    path="imgs"
    dirList=sorted(os.listdir(path))
    i=0
    while i<len(dirList):

        IM1NAME=dirList[i]
        IM2NAME=dirList[i+1]
        
        IM1="imgs/"+IM1NAME
        IM2="imgs/"+IM2NAME
        
        print "merging ", IM1NAME, " and ", IM2NAME
        img1 = Image(IM1)
        img2 = Image(IM2)
    
        #alignment
        a1_2 = align(img1,img2)         
        a2_1 = align(img2,img1)

        img1OutName="pic_"+str(i)+"_1.png"
        img2OutName="pic_"+str(i)+"_2.png"
        img1.save(img1OutName)
        img2.save(img2OutName)
        if (a1_2!=None): # i.e., we found a match, and could align
            o1_2 = a1_2.blit(img2,alpha=0.5)  #overlay
            o1_2NAME="pic_"+str(i)+"_merged_o1_2.png"
            o1_2.save(o1_2NAME)
        else:
            print "couldn't align img1 with img2"
        if (a2_1!=None): # i.e., we found a match, and could align
            o2_1 = a2_1.blit(img1,alpha=0.5)  #overlay
            o2_1NAME="pic_"+str(i)+"_merged_o2_1.png"
            o2_1.save(o2_1NAME)
        else:
            print "couldn't align img2 with img1"

        i=i+2
    

    
    
