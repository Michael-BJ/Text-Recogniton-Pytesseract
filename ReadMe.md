# How it's works
1. Import the libary that we need
````
import cv2
import pytesseract
````
2. Install the Tesseract OCR to your device (https://github.com/UB-Mannheim/tesseract/)
````
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
````
3. Make the program to read the image
````
img = cv2.imread('test.jpg')
````
4. Change the image into string
````
img_string = pytesseract.image_to_string(img) 
````
5. Show the text to the terminal
````
print(img_string)
````