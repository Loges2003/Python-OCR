from PIL import Image
import pytesseract
print pytesseract.image_to_string(Image.open('1.jpg'))

from pdf2image import convert_from_path
pages = convert_from_path('scanned.pdf', 500)
for page in pages:
    page.save('out.jpg', 'JPEG')
