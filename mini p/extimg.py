from tkinter import *
import pytesseract
import PIL
import fitz
from tkinter import filedialog
root=Tk()
def selectPdf():
    global pdf
    root.fileopen=filedialog.askopenfilename(initialdir="/",filetypes=(("pdf file","*.pdf"),("all files","*.*")))
    pdf=root.fileopen
        
def captureImage():
    global pdf
    i=1
    root.filesave=filedialog.asksaveasfilename(initialdir="/",defaultextension=".png", title="Save Report", filetypes=(("png file","*.png"),("All files","*.*")))
    doc=fitz.open(pdf)
    zoom_x=3.0
    zoom_y=3.0
    mat=fitz.Matrix(zoom_x,zoom_y)
    for page in doc:
        pix=page.getPixmap(matrix=mat)
        output=root.filesave
        pix.writePNG(output)
        i=i+1

select_pdf=Button(text="Select",command=selectPdf).grid(row=0,column=0)
capture_image=Button(text="capture",command=captureImage).grid(row=0,column=1)
root.mainloop()