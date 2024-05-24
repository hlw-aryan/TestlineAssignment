import cv2
import pytesseract
from PIL import Image
import numpy as np

def load_image(image_path):
    image = cv2.imread(image_path)
    return image

def extract_text(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text

if __name__ == "__main__":
    image_path = 'image.jpg'
    image = load_image(image_path)
    text = extract_text(image)
    print("Extracted Text:")
    print(text)
