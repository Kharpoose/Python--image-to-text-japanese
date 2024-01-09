import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'add local '
from PIL import Image

img = Image.open('text.png')
text = tess.image_to_string(img)

print(text)