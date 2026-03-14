from pdf2image import convert_from_path
from PIL import ImageChops

def compare_pdfs(pdf1, pdf2):

    pages1 = convert_from_path(pdf1)
    pages2 = convert_from_path(pdf2)

    if len(pages1) != len(pages2):
        return False

    for img1, img2 in zip(pages1, pages2):
        diff = ImageChops.difference(img1, img2)

        if diff.getbbox():
            return False

    return True