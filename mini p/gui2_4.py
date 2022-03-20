# importing tkinter module
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import fitz
from gtts import gTTS
import pyttsx3
from pygame import mixer
import tkinter.scrolledtext as st
import tkinter as tk
import pytesseract as tess
from PIL import Image
import os
import shutil
from pdf2image import convert_from_path
from pdf2image.exceptions import (PDFInfoNotInstalledError, PDFPageCountError,PDFSyntaxError)
import time
import cv2

# creating tkinter window
root = tk.Tk()
root.title("Audiobook")
root.geometry("637x800")

#root.configure(bg="#166EA1")
speaker=pyttsx3.init()
rate=speaker.getProperty('rate')
speaker.setProperty('rate',150)
voices=speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
tess.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text_area = st.ScrolledText(root,width = 60,height = 15,font = ("Times New Roman",15))
text_area.grid(row=6,column = 0, pady = 10, padx = 10,columnspan=3)
text_area.focus()

accent_option=["India","USA","UK","Australia","Canada","South Africa"]
clicked=StringVar()
clicked.set(accent_option[0])
pdf=""

pdf_type=["Scanned Document","Scanned Handwritten","No. Plates"]
clicked1=StringVar()
clicked1.set(pdf_type[0])  
#get the pdf file location in pdf
def selectPdf():
    global pdf
    root.filename=filedialog.askopenfilename(initialdir="/",title="Select a file", filetypes=(("pdf file","*.pdf"),("All files","*.*")))
    pdf=root.filename
    if pdf=="":
        messagebox.showinfo("Not Selected","Nothing Selected")
    else:
        messagebox.showinfo("Selected","selected from here"+pdf)

#to play files already in the system
def playCreated():
    root.filename=filedialog.askopenfilename(initialdir="/",title="Select a file", filetypes=(("mp3 file","*.mp3"),("All files","*.*")))
    global audio
    audio=root.filename
    if audio=="":
        messagebox.showinfo("Not Selected","Nothing Selected")
    else:
        messagebox.showinfo("Selected","selected from here"+audio)
#fetch the text from the pdf
def fetchText():
    try:
        doc=fitz.open(pdf)
        global text2
        text2=""
        for page in doc:
            text1=page.getText("text")
            text2=text2+text1
    except:
        messagebox.showinfo("Error","First Select a file")
    
    #speaker.say("Text Fetched Successfully")
    #speaker.runAndWait()
    #speaker.stop()    
    
    text_area.delete("1.0",END)
    text_area.insert(tk.INSERT, text2)    
#fetch text that is manually entered or changed
def fetchThis():
    global text2,pdf
    text3=text_area.get("1.0",END)
    text2=""
    text2=text3
    pdf=""    
    
    messagebox.showinfo("Fetched","Different file is fetched")
#convert the fetched text by gTTS
def convertAudio():
    global audio,text2,pdf  
    acc=clicked.get()
    #language=clicked1.get()
    #if language=="English":
        #lang1='en'
    if acc=="India":
        accent1="co.in"
    elif acc=="USA":
        accent1="com"
    elif acc=="UK":
        accent1="co.uk"
    elif acc=="Australia":
        accent1="com.au"
    elif acc=="Canada":
        accent1="ca"
    elif acc=="South Africa":
        accent1="co.za"
    #else :
        #lang1='hi'
        #accent1='co.in'
    try:
        res = len(text2.split())
        text2=text2.replace('∫','Integration of,')
        lbl=Label(root,text="Number of words= "+str(res),fg="blue").grid(row=4,column=2)
        root.filesave=filedialog.asksaveasfilename(initialdir="/",defaultextension=".mp3",initialfile="fileaudio.mp3", title="Save Report", filetypes=(("mp3 file","*.mp3"),("All files","*.*")))
        audio=root.filesave
        #text2=text2.replace('sin','sine')
        begin=time.time()
        tts=gTTS(text=text2,lang='en',tld=accent1)
        tts.save(str(audio))
        end=time.time()
        ttime=str(end-begin)
        ttime=ttime[0:5]
        #speaker.say("Conversion of Audio done Successfully")
        #speaker.runAndWait()
        messagebox.showinfo("Done","Done Conversion and saved file at "+str(audio)+"\nTotal time taken = "+ttime+" seconds")
        #speaker.stop()
    except:
        messagebox.showinfo("Error","No text Provided")
            
    #log=open("C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\logs\\logstext.txt","a+")
    #if str(pdf)!="":    
        #log.write("Selected file from:- "+str(pdf)+"\n")
    #else :
        #log.write("Selected file from:- Inside the program\n")
    #log.write("Total no. of words = "+str(res)+"\n")
    #log.write("Audio file saved at:- "+str(audio)+"\n")
    #log.write("Total time taken= "+str(ttime)+"seconds\n\n")
#play the saved audio using pygame mixer
def playAudio(): 
    try:
        global j
        j=1.0   
        mixer.init()
        mixer.music.load(str(audio))    
        mixer.music.play()
    except:
        messagebox.showinfo("Error","Select a audio file(.mp3)")
#resume the audiobook
def resumeAudio():
    try:
        mixer.music.unpause()
    except:
        messagebox.showinfo("Error","No audio file to resume")
#pause the audiobook
def pauseAudio():
    try:
        mixer.music.pause()
    except:
        messagebox.showinfo("Error","No audio file to pause")
def increaseVol():
    try:
        global j
        j=j+0.1
        mixer.music.set_volume(j)
    except:
        messagebox.showinfo("Error","No audio file")
def decreaseVol():
    try:
        global j
        j=j-0.1
        mixer.music.set_volume(j)
    except:
        messagebox.showinfo("Error","No audio file")
#take a snippent of each page of pdf and save in desired location as png
def captureImage():
    try:
        global pdf,path,images
        images = convert_from_path(pdf,500,poppler_path=r'C:\\Program Files\\poppler-0.68.0\\bin')
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
        
    except:
        messagebox.showinfo("Error","First Select a file")
#machine learning ie ocr to extract text from each image by opening it and using image_to_string method to get the text
def fetchImgText():
    #try:
        global path,images,text2
        i=0
        text2=""
        for i, image in enumerate(images):
            fname="image_" + str(i) + ".png"
            fname1=path+fname
            print(fname1)
            img=Image.open(str(fname1))
            #image = cv2.imread(str(fname1))
            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #cv2.imshow('Gray image', gray)
            #cv2.waitKey()
            #cv2.destroyWindow()
            text=tess.image_to_string(img)
            text2=text2+text
        print(text2)
        text_area.delete("1.0",END)
        text_area.insert(tk.INSERT, text2)
        res = len(text2.split())
        print("Number of words ="+str(res))
        lbl=Label(root,text="Number of words= "+str(res),fg="blue").grid(row=4,column=2)
        shutil.rmtree(path)
    #except:
        #messagebox.showinfo("Error","No image file found\n First capture the image from the respective pdf")
def instruction():
    messagebox.showinfo("Instruction to Follow","Note\n1.Select the pdf file\n2.If it is a scanned pdf then use step(3-4)or else use step(5)\n3.Capture the Images of Pdf and Save at Desired Location.\n4.Click Fetch Text from Image-->>step(6)\n5.Click Fetch Text. \n6.Convert to Audio.\n7.Click the Play Button to Play the Audio File")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!row=0!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#select pdf
select_pdf=Button(root,text="Select Pdf",command=selectPdf,padx=40,pady=20,bg="light blue",activebackground="blue")
select_pdf.grid(row=0,column=0)
#play already created audio
play_created=Button(root,text="Play already\nCreated file",command=playCreated,padx=40,pady=12,bg="light blue",activebackground="blue")
play_created.grid(row=0,column=1)
#extract image
capture_image=Button(root,text="Capture Image",command=captureImage,padx=40,pady=20,bg="light blue",activebackground="blue")
capture_image.grid(row=0,column=2)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!row=1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#convert to audio
convert_audio=Button(root,text="Convert Audio",command=convertAudio,padx=27,pady=20,bg="pink",activebackground="red")
convert_audio.grid(row=1,column=1)
#fetch text
fetch_text=Button(root,text="Fetch Text",command=fetchText,padx=37,pady=20,bg="pink",activebackground="red")
fetch_text.grid(row=1,column=0)
#fetch text from image
fetch_image_text=Button(root,text="Fetch text from Image",command=fetchImgText,padx=12,pady=20,bg="pink",activebackground="red")
fetch_image_text.grid(row=1,column=2)
#define the images for resume and pause
resume_img=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\resume.png")
pause_img=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\pause.png")
increase_vol=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\volumeup.png")
decrease_vol=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\volumedown.png")


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!row=2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Start playing the audio
play_audio=Button(root,text="Play",command=playAudio,padx=82,pady=20,bg="cyan",activebackground="blue")
play_audio.grid(row=2,column=0)
#resume the audio
resume_audio=Button(root,command=resumeAudio,padx=19,pady=20,image=resume_img,bg="light green",activebackground="green")
resume_audio.grid(row=2,column=1)
#pause the audio
pause_audio=Button(root,command=pauseAudio,padx=19,pady=20,image=pause_img,bg="yellow",activebackground="light Yellow")
pause_audio.grid(row=2,column=2)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!row=3!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#volume up
volume_up=Button(root,command=increaseVol,padx=19,pady=20,image=increase_vol,bg="blue",activebackground="Yellow")
volume_up.grid(row=3,column=0)
#volume down
volume_down=Button(root,command=decreaseVol,padx=19,pady=20,image=decrease_vol,bg="blue",activebackground="Yellow")
volume_down.grid(row=3,column=2)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!row=5!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Exit button
exit_button=Button(root,text="Exit",command=root.destroy,padx=83,pady=20,bg="purple",activebackground="red")
exit_button.grid(row=7,column=1)
#put some text manually
fetch_this=Button(root,text="Fetch This",command=fetchThis,padx=83,pady=20,bg="green",activebackground="light green")
fetch_this.grid(row=7,column=0)
#instructions
instruction=Button(root,text="Instruction",command=instruction,padx=40,pady=20,bg="green",activebackground="light green")
instruction.grid(row=7,column=2)
#accent
accent=Label(root,text="Choose Accent",bg="yellow",bd=8).grid(row=4,column=0)
drop1=OptionMenu(root, clicked, *accent_option).grid(row=4,column=1)
#language
lang=Label(root,text="Choose PDF type",bg="yellow",bd=8).grid(row=5,column=0)
drop1=OptionMenu(root, clicked1, *pdf_type).grid(row=5,column=1)
#lang=Label(root,text="Choose Language").grid(row=7,column=0)
# infinite loop

root.mainloop()
