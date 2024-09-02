# COLOR_CONVERSIONS_OF-IMAGE

## Aim:
To write a python program using OpenCV to do the following image manipulations.

i) Read, display, and write an image.

ii) Access the rows and columns in an image.

iii) Cut and paste a small portion of the image.

iv)To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.


## Software Required:

Anaconda - Python 3.7

## Algorithm:
### Step1:
Choose an image and save it as a filename.jpg.

### Step2:
Use imread(filename, flags) to read the file.

### Step3:
Use imshow(window_name, image) to display the image.

### Step4:
Use imwrite(filename, image) to write the image.

### Step5:
End the program and close the output image windows.

### Step6:
Convert BGR and RGB to HSV and GRAY

### Step7:
Convert HSV to RGB and BGR

### Step8:
Convert RGB and BGR to YCrCb

### Step9:
Split and Merge RGB Image

### Step10:
Split and merge HSV Image


## Program:
```
Developed By: Gopika R
Register Number: 212222240031
```
### i)Read and Display an Image
```
import cv2
image=cv2.imread('Gopika.jpg')
image=cv2.resize(image,(340,400))
cv2.imshow('Gopika', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Output:

![Screenshot 2024-09-02 081513](https://github.com/user-attachments/assets/ff518d94-3f24-4eb4-8c14-e66542eecc86)


### ii)Write the Image
```
import cv2
image=cv2.imread('Gopika.jpg')
cv2.imwrite('b.jpg',image)
```
#### Output
![Screenshot 2024-09-02 130301](https://github.com/user-attachments/assets/1c8f0071-7ad2-4613-a250-e979d95375bb)


### iii)Shape of the Image
```
import cv2
image=cv2.imread('Gopika.jpg')
print(image.shape)
```
#### Output
![Screenshot 2024-09-02 130430](https://github.com/user-attachments/assets/8590e39e-8995-4816-8a74-ca2e63f486e7)


### iv)Access rows and columns
```
import random
image=cv2.resize(image,(340,400))
for i in range (150,200):
    for j in range(image.shape[1]):
        image[i][j]=[random.randint(0,255),
                     random.randint(0,255),
                     random.randint(0,255)] 
cv2.imshow('Gopika(1)',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Output
![Screenshot 2024-09-02 083922](https://github.com/user-attachments/assets/cb1fe998-8987-4570-9793-c4091a5bc837)


### v)Cut and paste portion of image
```
image=cv2.imread('Gopika.jpg',1)
image=cv2.resize(image,(340,400))
tag =image[125:195,105:185]
image[110:180,120:200] = tag
cv2.imshow('Gopika(2)',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Output

![Screenshot 2024-09-02 084856](https://github.com/user-attachments/assets/6730fe6a-8b7e-48bc-8c09-d6c948920ec1)

### vi)BGR and RGB to HSV and GRAY
```
img = cv2.imread('Gopika.jpg',1)
img = cv2.resize(img,(300,350))
cv2.imshow('Original Image',img)
hsv1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv1)
hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)
gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray1)
gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### Output
![Screenshot 2024-09-02 092904](https://github.com/user-attachments/assets/44600e96-eea1-4ca5-8154-797059e4db0f)


### vii)HSV to RGB and BGR
```
img = cv2.imread('Gopika.jpg')
img = cv2.resize(img,(300,350))
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('Original HSV Image',img)
RGB = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
cv2.imshow('2HSV2BGR',RGB)
BGR = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Output
![Screenshot 2024-09-02 131150](https://github.com/user-attachments/assets/0df751ad-1009-4e10-85e6-ab42e30f0997)

### viii)RGB and BGR to YCrCb
```
img = cv2.imread('Gopika.jpg')
img = cv2.resize(img,(300,350))
cv2.imshow('Original RGB Image',img)
YCrCb1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)
YCrCb2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
cv2.imshow('BGR-2-YCrCb',YCrCb2)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Output
![Screenshot 2024-09-02 131522](https://github.com/user-attachments/assets/6fc02bc2-1de0-4aaf-bed4-a9f5d451ef59)


### ix) Split and merge RGB Image
```
img = cv2.imread('Gopika.jpg',1)
img = cv2.resize(img,(300,350))
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]
cv2.imshow('R-Channel',R)
cv2.imshow('G-Channel',G)
cv2.imshow('B-Channel',B)
merged = cv2.merge((B,G,R))
cv2.imshow('Merged RGB image',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Output

![Screenshot 2024-09-02 132821](https://github.com/user-attachments/assets/c3c35dad-9946-4564-8cd6-250bcdd598c2)



### x) Split and merge HSV Image
```
img = cv2.imread("Gopika.jpg",1)
img = cv2.resize(img,(300,350))
img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
H,S,V=cv2.split(img)
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)
merged = cv2.merge((H,S,V))
cv2.imshow('Merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
#### Output

![Screenshot 2024-09-02 133150](https://github.com/user-attachments/assets/6cd94803-d5b4-49ba-9cd6-389b46e2b8c7)


## Result:
Thus the images are read, displayed, and written ,and color conversion was performed between RGB, HSV and YCbCr color models successfully using the python program.






