import cv2 as cv
from cv2 import waitKey
import numpy as np
import PIL
from PIL import Image,ImageFilter
import numpy
filters=[]
params=[]
backRmapi='yMp43NNBqnCosi67pj5y87F5'
w,h=200,300
pt2=np.float32([[0,0],[w,0],[0,h],[w,h]])
pt1=[]

def val(x):
    return x


def plainRGB(img1,i=0):
    b, g, r = cv.split(img1)
    if i==0:
        b[:]=0
    elif i==1:
        g[:]=0
    else:
        r[:]=0

    return cv.merge((b, g, r))
# cv.imshow('B',plainRGB(img2,0))
# cv.imshow('R',plainRGB(img2,1))
# cv.imshow('G',plainRGB(img2,2))
# cv.waitKey(000)

# cv.createTrackbar('B','params',0,255,val)
# cv.createTrackbar('R','params',0,255,val)
# cv.createTrackbar('G','params',0,255,val)

def blurImga(imgi,pt1,pt2,size):
    imt=Image.fromarray(cv.cvtColor(imgi,cv.COLOR_BGR2RGB))
    cropped=imt.crop((pt1[0],pt1[1],pt2[0],pt2[1]))
    blur=cropped.filter(ImageFilter.GaussianBlur(size))
    imt.paste(blur,(pt1[0],pt1[1],pt2[0],pt2[1]))
    imt.show()
    return imgi
# def addpoint(event,x,y,flag,params):
#     global pt1
#     if event==cv.EVENT_LBUTTONDOWN:
#         pt1.append([x,y])
#         cv.circle(img,(x,y),2,(255,0,0),thickness=-1)
#         cv.imshow('Image',img2)
#         if len(pt1)==2:
#             blurImga(img2.copy(),pt1[0],pt1[1],5)
#             pt1=[]
#         print(pt1)
#     elif event== cv.EVENT_MOUSEMOVE:
#         if len(pt1)==1:
#             imgt=img2.copy()
#             cv.rectangle(imgt,pt1[0],(x,y),(255,0,0),thickness=1)
#             cv.imshow('Image',imgt)
# def __blurImg(img):
#     cv.imshow("Image", img)
#     cv.setMouseCallback('Image', addpoint)
#     cv.waitKey(0)

# __blurImg(img)



def defFilters(imgi,fils):
    filterss = [cv.COLOR_BGR2GRAY, cv.COLOR_BGR2RGB]
    return cv.cvtColor(imgi,filterss[fils])

def plainNEGRGB(img1,i=0):
    b, g, r = cv.split(img1)
    if i==0:
        b=255-b
    elif i==1:
        g=255-g
    else :
        r=255-r

    return cv.merge((b, g, r))

def wrapContent(img,pt1):
    pt=np.float32(pt1)
    mat=cv.getPerspectiveTransform(pt,pt2)
    cpy=img.copy()
    im2=cv.warpPerspective(cpy,mat,(w,h))
    cv.imshow("Tried",im2)
    img=cpy.copy()
    cv.imshow("Test",img)
    pt1.clear()




def cropImg(img,pt1,pt2):
    return img[pt1[0]:pt2[0],pt1[1]:pt2[1]]

PILFilters=[ImageFilter.UnsharpMask(100),ImageFilter.SMOOTH
    ,ImageFilter.DETAIL]
def filter1(img,filter):
    imt1=Image.fromarray(img)
    imt2=imt1.filter(filter=PILFilters[filter])
    open_cv_image = numpy.array(imt2) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image


# filter1(cv.cvtColor(img2,cv.COLOR_RGB2BGR))
# cv.imshow('crop',cropImg(img2,(0,0),(200,200)))
def Pixalete(img,size=16):
    imt=Image.fromarray(img)
    small=imt.resize((size,size),resample=Image.BILINEAR)
    res=small.resize(imt.size,Image.NEAREST)
    # res.show()
    # res.save('../static/images/test1.jpg')
    open_cv_image = numpy.array(res) 
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy() 
    return open_cv_image
def AutoEnhance(img):
    imt1 = Image.fromarray(img)
    imt1.show()
    imt2 = imt1.filter(filter=ImageFilter.SMOOTH)
    imt3=imt2.filter(ImageFilter.SHARPEN)
    imt4=imt3.filter(ImageFilter.UnsharpMask)
    imt5=imt4.filter(filter=ImageFilter.UnsharpMask(10))
    imt5.show()
def removeBack(imgLoc):
    import requests

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(imgLoc, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': backRmapi},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
def mergeWithFilter(imgFore,imgBack):
    if(len(imgBack.shape)<3):
        imgBack=cv.merge((imgBack,imgBack,imgBack))
    x,y,_=imgBack.shape
    imgF=cv.resize(imgFore,(y,x))
    added_image = cv.addWeighted(imgBack,0.3,imgF,1,0)

    return added_image
def HBFilter(imgURL,filteredIMG):
    import requests

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(imgURL, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': backRmapi},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
            imf=cv.imread('no-bg.png')
            mergeWithFilter(imf,filteredIMG)
    else:
        print("Error:", response.status_code, response.text)


if __name__=="__main__":
    img2=cv.imread(r'C:\Users\Pradhyuman Pandey\Downloads\LOC\LOC4.0_Dynamic-Developers\img_enhancer_module\test.jpeg')
    cv.imshow('t',img2)
    cv.waitKey()
    imb=defFilters(img2,0)
    imf=cv.imread(r'C:\Users\Pradhyuman Pandey\Downloads\LOC\LOC4.0_Dynamic-Developers\no-bg.png')
    img3=mergeWithFilter(imf,imb)
    cv.imshow('t',img3)
    cv.waitKey()

    # removeBack(r'C:\Users\Pradhyuman Pandey\Downloads\LOC\LOC4.0_Dynamic-Developers\img_enhancer_module\test.jpeg')
    # AutoEnhance(cv.cvtColor(img2,cv.COLOR_RGB2BGR))

# Pixalete(img2)
# Pixalete(cv.cvtColor(img2,cv.COLOR_RGB2BGR))


# cv.waitKey()

