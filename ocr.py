import cv2
import pytesseract

# Path to the image file
image_path = 'card.jpg'
# Read the image using OpenCV
image = cv2.imread(image_path)
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Use Tesseract to do OCR on the image
extracted_text = pytesseract.image_to_string(gray_image)
# Print the extracted text
print(extracted_text)
