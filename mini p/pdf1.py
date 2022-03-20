import fitz
from gtts import gTTS

doc=fitz.open()
for page in doc:
    text1=page.getText("text1")
    
tts = gTTS(text=text1, lang='en')
tts.save("file1.mp3")
