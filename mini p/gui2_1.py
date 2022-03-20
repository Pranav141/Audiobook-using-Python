# importing tkinter module
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import fitz
from gtts import gTTS
import pyttsx3
from pygame import mixer
from pdf2image import convert_from_path
import tkinter.scrolledtext as st
import tkinter as tk


# creating tkinter window
root = tk.Tk()
root.title("Audiobook")
speaker=pyttsx3.init()
rate=speaker.getProperty('rate')
speaker.setProperty('rate',150)
voices=speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)
text_area = st.ScrolledText(root,width = 60,height = 8,font = ("Times New Roman",15))
text_area.grid(row=7,column = 0, pady = 10, padx = 10,columnspan=2)

#text_area.configure(state ='disabled')

text_area.focus()  
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
    doc=fitz.open(pdf)
    global text2
    text2=""
    for page in doc:
        text1=page.getText("text")
        text2=text2+text1
    speaker.say("Text Fetched Successfully")
    speaker.runAndWait()
    speaker.stop()
    text_area.delete("1.0",END)
    text_area.insert(tk.INSERT, text2)
    res = len(text2.split())
    print("Number of words ="+str(res))
    #lbl=Label(root,text=text2,fg="blue").grid(row=6,column=0)
#fetch text that is manually entered or changed
def fetchThis():
    global text2
    text3=text_area.get("1.0",END)
    text2=""
    text2=text3
    messagebox.showinfo("Fetched","Different file is fetched")
#convert the fetched text by gTTS
def convertAudio():
    root.filesave=filedialog.asksaveasfilename(initialdir="/",defaultextension=".mp3",initialfile="audio.mp3", title="Save Report", filetypes=(("mp3 file","*.mp3"),("All files","*.*")))
    global audio    
    audio=root.filesave
    tts=gTTS(text=text2,lang='en')
    tts.save(str(audio))
    speaker.say("Conversion of Audio done Successfully")
    speaker.runAndWait()
    messagebox.showinfo("Done","Done Conversion and saved file at "+str(audio))
    speaker.stop()
#play the saved audio using pygame mixer
def playAudio(): 
    global j
    j=1.0   
    mixer.init()
    mixer.music.load(str(audio))    
    mixer.music.play()
#resume the audiobook
def resumeAudio():
    mixer.music.unpause()
#pause the audiobook
def pauseAudio():
    mixer.music.pause()
def increaseVol():
    global j
    j=j+0.1
    mixer.music.set_volume(j)
def decreaseVol():
    global j
    j=j-0.1
    mixer.music.set_volume(j)


button_pdf=Button(root,text="Select Pdf",command=selectPdf,padx=40,pady=20,bg="light blue",activebackground="blue")
button_pdf.grid(row=0,column=0)
play_created=Button(root,text="Play already Created file",command=playCreated,pady=20,bg="light blue",activebackground="blue")
play_created.grid(row=0,column=1)

convert_audio=Button(root,text="Convert Audio",command=convertAudio,padx=27,pady=20,bg="pink",activebackground="red")
convert_audio.grid(row=1,column=1)
fetch_text=Button(root,text="Fetch Text",command=fetchText,padx=37,pady=20,bg="pink",activebackground="red")
fetch_text.grid(row=1,column=0)

#define the images for resume and pause
resume_img=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\resume.png")
pause_img=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\pause.png")
increase_vol=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\volumeup.png")
decrease_vol=PhotoImage(file="C:\\Users\\Pranav\\Desktop\\.py file\\mini p\\2x\\volumedown.png")

play_audio=Button(root,text="Play",command=playAudio,padx=82,pady=20,bg="cyan",activebackground="blue")
play_audio.grid(row=3,column=0,columnspan=2)

resume_audio=Button(root,command=resumeAudio,padx=19,pady=20,image=resume_img,bg="light green",activebackground="green")
resume_audio.grid(row=4,column=0)
pause_audio=Button(root,command=pauseAudio,padx=19,pady=20,image=pause_img,bg="yellow",activebackground="light Yellow")
pause_audio.grid(row=4,column=1)

volume_up=Button(root,command=increaseVol,padx=19,pady=20,image=increase_vol,bg="blue",activebackground="Yellow")
volume_up.grid(row=5,column=0)
volume_down=Button(root,command=decreaseVol,padx=19,pady=20,image=decrease_vol,bg="blue",activebackground="Yellow")
volume_down.grid(row=5,column=1)

#extract_image=Button(root,command=extractImage,padx=19,pady=20,text="fetch Image",bg="magenta",activebackground="Yellow")
#extract_image.grid(row=6,column=1)

exit_button=Button(root,text="Exit",command=root.destroy,padx=83,pady=20,bg="purple",activebackground="red")
exit_button.grid(row=6,column=0,columnspan=2)

fetch_this=Button(root,text="Fetch This",command=fetchThis,padx=83,pady=20,bg="green",activebackground="light green")
fetch_this.grid(row=8,column=0,columnspan=2)
# infinite loop

root.mainloop()
