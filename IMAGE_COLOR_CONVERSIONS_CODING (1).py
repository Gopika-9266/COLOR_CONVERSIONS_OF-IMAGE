

# import cv2
# from google.colab.patches import cv2_imshow

# In[ ]:


#1.	Read and Display an Image
import cv2
image=cv2.imread('cat.jpg',1)
cv2.imshow('Image Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[ ]:


#2.	Draw Shapes and Add Text
(1) Draw a line from the top-left to the bottom-right of the image.

import cv2
img = cv2.imread("cat.jpg")
res = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (200, 100, 205), 10)
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

(2) Draw a circle at the center of the image.

import cv2

# Load the image
img = cv2.imread("cat.jpg")

# Get the dimensions of the image
height, width, _ = img.shape

# Calculate the center of the image
center_coordinates = (width // 2, height // 2)

# Draw a circle at the center of the image
res = cv2.circle(img, center_coordinates, 150, (255, 0, 0), 10)

# Display the image with the circle
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

(3) Draw a rectangle around a specific region of interest in the image.

import cv2

# Load the image using the correct path
img = cv2.imread("cat.jpg")

# Define the start and stop points of the rectangle (Region of Interest)
# These coordinates should encapsulate the region you want to highlight
start = (150, 100)  # top-left corner of the rectangle
stop = (400, 300)   # bottom-right corner of the rectangle

# Define the color and thickness of the rectangle
color = (100, 255, 100)  # Green rectangle
thickness = 10           # Thickness of the rectangle

# Draw the rectangle on the image
res_img = cv2.rectangle(img, start, stop, color, thickness)

# Display the resulting image with the rectangle
cv2.imshow('Image Window', res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

(4) Add the text "OpenCV Drawing" at the top-left corner of the image.

import cv2

# Load the image
img = cv2.imread("cat.jpg")

# Define the text to be added and its position
text = "OpenCV Drawing"
position = (10, 50)  # Positioning the text at the top-left corner

# Set the font, scale, color, and thickness of the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  # White color
thickness = 2

# Add the text to the image
res = cv2.putText(img, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

# Display the image with the text
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


#3.Image Color Conversion

(1) Convert the image from RGB to HSV and display it

import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

(2) Convert the image from RGB to GRAY and display it.

import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()

(3) Convert the image from RGB to YCrCb and display it.

import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
YCrCb1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)
cv2.waitKey(0)
cv2.destroyAllWindows()

(4) Convert the HSV image back to RGB and display it.

import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
BGR = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()

# In[ ]:

#4.Access and Manipulate Image Pixels

import cv2

# Load and resize the image
img = cv2.imread('cat.jpg', 1)
img = cv2.resize(img, (300, 200))

# Show the original image
cv2.imshow('Original Image', img)

(1) Access and print the value of the pixel at coordinates (100, 100)
pixel_value = img[100, 100]
print(f"Pixel value at (100, 100): {pixel_value}")

(2) Modify the color of the pixel at (199, 199) to white
img[199, 199] = [255, 255, 255]  # Setting the pixel value to white (BGR)

# Display the modified image
cv2.imshow('Modified Image', img)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()



# In[ ]:

#5.Image Resizing

width=700
height=600
half_width=300
half_height=400
resized_img = cv2.resize(image, (300, 400))
cv2.imshow('Original',image)
cv2.imshow('resized',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:

#6.	Image Cropping
# In[ ]:
import cv2

# Load the image
image1=cv2.imread('cat.jpg',1)

# Define the starting point and size of the ROI
x, y = 50, 50
width, height = 100, 100

# Crop the ROI
roi = image1[y:y + height, x:x + width]

# Display the cropped ROI
cv2.imshow('Cropped Image', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


#7.Image Flipping

(1) Flip the original image horizontally and display it.

import cv2
img = cv2.imread("cat.jpg")
img = cv2.resize(img,(300,200))
res=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('Original',img)
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

(2) Flip the original image vertically and display it.

import cv2
img = cv2.imread("cat.jpg")
img = cv2.resize(img,(300,200))
res=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# Display the HSV image
cv2.imshow('Original',img)
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

   
# In[ ]:

#8.Write and Save the Modified Image

import cv2
img = cv2.imread("cat.jpg")
img = cv2.resize(img,(300,200))
cv2.imwrite('pet.jpg',img)
   
# In[ ]:
