import pytesseract
from PIL import Image

#print tesserocr.tesseract_version()  # print tesseract-ocr version
# print tesserocr.get_languages()  # prints tessdata path and list of available languages

image = Image.open('./new.jpeg')
# print tesserocr.image_to_text(image)  # print ocr text from image
# # or
# print tesserocr.file_to_text('sample.jpg')
text = pytesseract.image_to_string(image)
print('text is:' + text)