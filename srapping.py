import pytesseract
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\BRI\AppData\Local\Tesseract-OCR\tesseract.exe'
def convert_pdf_to_img(pdf_file) :
    return convert_from_path(pdf_file, 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
def convert_image_to_text(file):
    text = image_to_string (file)
    return text
def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img (pdf_file)
    final_text = ""
    for pg, img in enumerate (images) :

        final_text += convert_image_to_text (img)
        #print("Page n{}".format(pg))
        #print(convert_image_to_text(img))

    return final_text
path_to_pdf = r'C:\Users\BRI\Documents\project code\testaja2.pdf'
print(get_text_from_any_pdf(path_to_pdf))

