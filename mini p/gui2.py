# importing tkinter module
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import fitz
import pyttsx3

# creating tkinter window
root = Tk()
def selectPdf():
    global pdf
    root.filename=filedialog.askopenfilename(initialdir="/",title="Select a file", filetypes=(("pdf file","*.pdf"),("All files","*.*")))
    pdf=root.filename
    messagebox.showinfo("Selected","selected from here"+pdf)
    
def convertAudio():
    doc=fitz.open(pdf)
    global text2
    text2=""
    for page in doc:
        text1=page.getText("text")
        text2=text2+text1
    lbl=Label(root,text=text2,fg="blue").grid(row=4,column=0)
def playAudio():
    speaker=pyttsx3.init()
    rate=speaker.getProperty('rate')
    speaker.setProperty('rate',150)
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    speaker.say(text2)
    speaker.runAndWait()
    speaker.stop()    
    

button_pdf=Button(root,text="Select Pdf",command=selectPdf,padx=23,pady=20,bg="light blue",activebackground="blue")
button_pdf.grid(row=0,column=0)
convert_audio=Button(root,text="Convert",command=convertAudio,padx=29,pady=20,bg="pink",activebackground="red")
convert_audio.grid(row=1,column=0,columnspan=1)
play_audio=Button(root,text="Play",command=playAudio,padx=38,pady=20,bg="light green",activebackground="green")
play_audio.grid(row=2,column=0,columnspan=1)
#exit_button=Button(root,text="Exit",command=root.destroy,padx=38,pady=20,bg="purple",activebackground="red")
#exit_button.grid(row=3,column=0,columnspan=1)
# infinite loop
root.mainloop()
#resume_audio=Button(root,text="Resume",command=resumeAudio,padx=19,pady=20,bg="light green",activebackground="green")
#resume_audio.grid(row=4,column=0)
#pause_audio=Button(root,text="Pause",command=pauseAudio,padx=19,pady=20,bg="pink",activebackground="red")
#pause_audio.grid(row=4,column=1)


#def extractImage():
    #pages=convert_from_path(pdf)
    
    #i = 1
    #root.filesave1=filedialog.asksaveasfilename(initialdir="/",defaultextension=".jpg",initialfile="image", title="Save Image", filetypes=(("jpg file","*.jpg"),("All files","*.*")))
    #pdfs=root.filesave1
    #for page in pages:
        #image_name = str(pdfs) + str(i) + ".jpg"  
        #page.save(image_name, "JPEG")
        #i = i+1