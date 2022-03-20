#import pytesseract as tess
#from PIL import Image
#tess.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
#img=Image.open("C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\5.png")
#text=tess.image_to_string(img)
#print(text)
from tkinter import *
import pytesseract
from PIL import Image
import fitz
from pdf2image import convert_from_path
from tkinter import filedialog
import os
import shutil
import pytesseract as tess
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,PDFSyntaxError)
root=Tk()
tess.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
def selectPdf():
    global pdf
    root.fileopen=filedialog.askopenfilename(initialdir="/",filetypes=(("pdf file","*.pdf"),("all files","*.*")))
    pdf=root.fileopen
        
def captureImage():
    global pdf,path,images
    images = convert_from_path(pdf,500,poppler_path=r'C:\\Program Files\\poppler-0.68.0\bin')
    directory="EXTRACTED_IMAGES"
    root.filedir=filedialog.askdirectory()
    parent_dir=root.filedir
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    print(path)
    path=path.replace("\\","/")
    print(path)
    path=path+"/"
    for i, image in enumerate(images):
        fname = "image_" + str(i) + ".png"
        fname1=path+fname
        image.save(fname1, "PNG")

def fetchImgText():
    global path,images
    i=0
    text2=""
    for i, image in enumerate(images):
        fname="image_" + str(i) + ".png"
        fname1=path+fname
        print(fname1)
        img=Image.open(str(fname1))
        text=tess.image_to_string(img)
        text2=text2+text
    print(text2)
    shutil.rmtree(path)

select_pdf=Button(text="Select",command=selectPdf).grid(row=0,column=0)
capture_image=Button(text="capture",command=captureImage).grid(row=0,column=1)
text_image=Button(text="fetch Text",command=fetchImgText).grid(row=0,column=2)
root.mainloop()
