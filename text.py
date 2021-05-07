import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('test.jpg')
img_string = pytesseract.image_to_string(img) 
print(img_string)


# img_boxes= pytesseract.image_to_boxes(img)
# # print(img_boxes)

# imgH, imgW,_ = img.shape
# for i in img_boxes.splitlines():
#     i = i.split(' ')
#     # print(i)
    
#     x,y,w,h = int(i[1]),int(i[2]),int(i[3]),int(i[4])
#     cv2.rectangle(img,(x,imgH-y),(w,imgH-h),(0,255,0),3)
    
# cv2.imshow("Text recognition", img)
# cv2.waitKey(0)