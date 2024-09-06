# COLOR_CONVERSIONS_OF-IMAGE

## Aim:

Write a Python program using OpenCV that performs the following tasks:

i) Read and Display an Image.

ii) 	Draw Shapes and Add Text.

iii) Image Color Conversion.

iv) Access and Manipulate Image Pixels.

v) Image Resizing

vi) Image Cropping

vii) Image Flipping

viii)	Write and Save the Modified Image


## Software Required:
Anaconda - Python 3.7

## Algorithm:

### Step 1:

Load an image from your local directory and display it.

### Step 2:

1. Draw a line from the top-left to the bottom-right of the image.
2. Draw a circle at the center of the image.
3. Draw a rectangle around a specific region of interest in the image.
4. Add the text "OpenCV Drawing" at the top-left corner of the image.

### Step 3:

1. Convert the image from RGB to HSV and display it.
2. Convert the image from RGB to GRAY and display it.
3. Convert the image from RGB to YCrCb and display it.
4. Convert the HSV image back to RGB and display it.

### Step 4:

1. Access and print the value of the pixel at coordinates (100, 100).
2. Modify the color of the pixel at (200, 200) to white.

### Step 5:

Resize the original image to half its size and display it.

### Step 6:

Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.

### Step 7:

1. Flip the original image horizontally and display it.
2. Flip the original image vertically and display it.

### Step 8:

Save the final modified image to your local directory.


## Program:
```
Developed By: Gopika R
Register Number: 212222240031
```

### i) Read and Display an Image


```
import cv2
image=cv2.imread('cat.jpg',1)
cv2.imshow('Image Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output

![Screenshot 2024-09-06 192401](https://github.com/user-attachments/assets/1b7977a9-af44-4273-935c-68314903f340)

### ii) Draw Shapes and Add Text

(1) Draw a line from the top-left to the bottom-right of the image.

```
import cv2
img = cv2.imread("cat.jpg")
res = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (200, 100, 205), 10)
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Output
![Screenshot 2024-09-06 192642](https://github.com/user-attachments/assets/f89f1bce-466e-475e-8216-24a29c3c2a13)

(2) Draw a circle at the center of the image.
```
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
```

### Output
![Screenshot 2024-09-06 192944](https://github.com/user-attachments/assets/7df52557-cf7c-43ba-a614-12cadb51fe14)


(3) Draw a rectangle around a specific region of interest in the image.
```
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
```
### Output
![Screenshot 2024-09-06 193805](https://github.com/user-attachments/assets/0f4fc22c-e41f-453a-bd00-044d876cc012)


(4) Add the text "OpenCV Drawing" at the top-left corner of the image.
```
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
```

### Output
![Screenshot 2024-09-06 194108](https://github.com/user-attachments/assets/db200108-b703-4bcb-88ba-5c39cc061acf)



### iii) Image Color Conversion

(1) Convert the image from RGB to HSV and display it
```
import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output
![Screenshot 2024-09-06 194359](https://github.com/user-attachments/assets/54a69f13-85da-4831-b76b-da884bc4a9cc)


(2) Convert the image from RGB to GRAY and display it.
```
import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Output
![Screenshot 2024-09-06 194520](https://github.com/user-attachments/assets/5c0e1689-48d1-4710-a334-31584d880755)

(3) Convert the image from RGB to YCrCb and display it.
```
import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
YCrCb1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output
![Screenshot 2024-09-06 194641](https://github.com/user-attachments/assets/314d68ea-5366-4368-8438-e66445efd7f0)

(4) Convert the HSV image back to RGB and display it.
```
import cv2
img = cv2.imread('cat.jpg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
BGR = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output

![Screenshot 2024-09-06 194949](https://github.com/user-attachments/assets/02c97608-cc1c-45aa-844c-f46bdd754c62)


### iv) Access and Manipulate Image Pixels
```
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
```
### Output
![Screenshot 2024-09-06 195719](https://github.com/user-attachments/assets/b663a289-ae9c-4c47-9458-5bd1323a2813)

![Screenshot 2024-09-06 195443](https://github.com/user-attachments/assets/811f152d-e0ff-48b7-98ff-1a772eb0609e)

### v) Image Resizing

Resize the original image to half its size and display it.
```
width=700
height=600
half_width=300
half_height=400
resized_img = cv2.resize(image, (300, 400))
cv2.imshow('Original',image)
cv2.imshow('resized',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Output:
![Screenshot 2024-09-06 221523](https://github.com/user-attachments/assets/aa1fa2d2-4b9e-4733-bd29-35cadd6f5608)


### vi) Image Cropping

Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.

```
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
```

### Output
![Screenshot 2024-09-06 201258](https://github.com/user-attachments/assets/00deed50-d17e-4dba-8e8a-38aa4a449f9b)


### vii) Image Flipping

(1) Flip the original image horizontally and display it.
```
import cv2
img = cv2.imread("cat.jpg")
img = cv2.resize(img,(300,200))
res=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow('Original',img)
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output

![Screenshot 2024-09-06 201533](https://github.com/user-attachments/assets/9b032780-bf60-4776-9029-6233537de653)



(2) Flip the original image vertically and display it.

```
import cv2
img = cv2.imread("cat.jpg")
img = cv2.resize(img,(300,200))
res=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# Display the HSV image
cv2.imshow('Original',img)
cv2.imshow('Image Window', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Output
![Screenshot 2024-09-06 221936](https://github.com/user-attachments/assets/16720292-2faa-4c54-b17b-35af4a68bbbe)


### viii) Write and Save the Modified Image

Save the final modified image to your local directory.
```
import cv2
img = cv2.imread("cat.jpg")
img = cv2.resize(img,(300,200))
cv2.imwrite('pet.jpg',img)
```
### Output

![Screenshot 2024-09-06 201829](https://github.com/user-attachments/assets/4dfec392-c489-4e71-8d6d-83e9823e0280)


## Result:
Thus the images are read, displayed, and written ,and color conversion was performed  successfully using the python program.







