from tkinter import filedialog
from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os
import shutil
import time

if __name__ == "__main__":

    root = Tk()
    
    root.geometry("450x470")
    root.config(bg="white")
    root.title("File Manager")
    root.resizable(0,0)

    def createIfNotExist(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)


    def browse_button():
        file = filedialog.askdirectory()
        if file == "":  
            file = None
        else:
            fileEntry.delete(0,END)
            fileEntry.insert(0,file)
        
        filePath = fileEntry.get()            
        files = os.listdir(filePath)
        imgExts = [".png", ".jpg", ".jpeg"]
        zipExts = [".rar", ".zip"]
        docExts = [".txt", ".docx", ".doc", ".pdf", ".pptx"]
        mediaExts = [".mp4", ".mp3", ".flv", ".mkv", ".3gp", ".wav"]
        softExts = [".exe", ".apk"]
    

        images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
        zips = [file for file in files if os.path.splitext(file)[1].lower() in zipExts]
        docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
        medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
        softwares = [file for file in files if os.path.splitext(file)[1].lower() in softExts]
    

        extras = []
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if (ext not in imgExts) and (ext not in zipExts) and (ext not in docExts) and (ext not in mediaExts) and (ext not in softExts) and os.path.isfile(file):
                extras.append(file)


        def moveFiles():
        
            # creating the folders
            if images:
                createIfNotExist(f'{filePath}/Images')
            if zips:
                createIfNotExist(f'{filePath}/Zip')
            if docs:
                createIfNotExist(f'{filePath}/Docs')
            if medias:
                createIfNotExist(f'{filePath}/Media')
            if softwares:
                createIfNotExist(f'{filePath}/Software')
            if extras:
                createIfNotExist(f'{filePath}/Extras')
                    
            # moving files to respective folders
            for image in images:
                shutil.move(f"{filePath}/{image}", f"{filePath}/Images/{image}")

            for zip in zips:
                shutil.move(f"{filePath}/{zip}", f"{filePath}/Zip/{zip}")

            for doc in docs:
                shutil.move(f"{filePath}/{doc}", f"{filePath}/Docs/{doc}")

            for media in medias:
                shutil.move(f"{filePath}/{media}", f"{filePath}/Media/{media}")

            for software in softwares:
                shutil.move(f"{filePath}/{software}", f"{filePath}/Software/{software}")

            for extra in extras:
                shutil.move(f"{filePath}/{extra}", f"{filePath}/Extras/{extra}")

            progress = Progressbar(root,orient="horizontal",length=300, mode="determinate")
            progress.place(x=70, y=300)

            for i in range(1,100,1):
                progress['value'] = i
                root.update_idletasks()
                time.sleep(0.02)
            progress['value'] = 100
            progress.destroy()


            doneLabel = Label(root, image=tickPhoto, bg="white")
            doneLabel.place(x=180,y=320)

            resultLabel = Label(root,text="Done !!",font=('arial',16,'bold'), bg="white", fg="green")
            resultLabel.place(x=180,y=380) 
    
      
        arrangeButton = Button(root,text=" Arrange ",font=('arial',12,'bold'),width=20, bg="#4169E1",fg='#FFFFFF',command=moveFiles)
        arrangeButton.place(x=115,y=220)


    photo = Image.open(f"{os.path.split(os.path.realpath(__file__))[0]}/images/tick.png")
    tickPhoto = ImageTk.PhotoImage(photo)

    image = Image.open(f"{os.path.split(os.path.realpath(__file__))[0]}/images/icon.png")
    iconPhoto = ImageTk.PhotoImage(image)
    appName = Label(root,justify=LEFT, compound = LEFT, padx = 10,text="File Manager",image=iconPhoto,font=('cooper black',20,'bold'),
                    bg="white",fg='maroon')
    appName.place(x=95,y=15)

    labelFile = Label(root,text="Arrange your cluttered files to their proper folders.",font=('sans-serif',12,'bold'), bg="white")
    labelFile.place(x=30,y=70)

        
    fileEntry = Entry(root,font=('calibri',12),width=30)
    fileEntry.place(x=35, y=150)

    openFileButton = Button(root,text=" Browse ",font=('arial',12,'bold'),width=10,
                        bg="#008080",fg='white',command=browse_button)
    openFileButton.place(x=300,y=150)
   

    root.mainloop()
