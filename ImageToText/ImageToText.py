## INSTALL TESSERACT-OCR
## pip install pytesseract

from PIL import Image
from pytesseract import *

pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
data = open("ImageToText.txt", "a")

for chap in range(2):
    chapter = f"Chapter {chap + 1}"
    print(f"=== Starting at {chapter} ===")
    for less in range(2):
        lesson = f"Lesson {less + 1}"
        print(f"-- Reading {lesson} ---")
        for page in range(5):
            pages = f"{page + 1}.jpg"
            try:
                image = Image.open(f"{chapter}/{lesson}/{pages}")
                text = pytesseract.image_to_string(image)
                data.write(text + "\n")
                print(f"Done writing page: {pages}")
            except:
                print("No other Pages Found!")
                continue
        else:
            print(f"Done Writing Pages in {lesson}!")
    else:
        print(f"--- {lesson} Done! ---")
else:
    print("=== Chapter Done! All Done! ===")
    data.close()
    
