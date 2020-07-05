from tkinter import *
import os

if __name__ == "__main__":

    root = Tk()
    
    root.geometry("450x300")
    root.config(bg="light blue")
    root.title("File Manager")
    root.resizable(0,0)

    def createIfNotExist(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
        
    
    def moveFiles():
        
        # creating the folders
        if images:
            createIfNotExist('Images')
        if zips:
            createIfNotExist('Zip')
        if docs:
            createIfNotExist('Docs')
        if medias:
            createIfNotExist('Media')
        if softwares:
            createIfNotExist('Software')
        if extras:
            createIfNotExist('Extras')
                
        # moving files to respective folders
        for image in images:
            os.replace(image, f"Images/{image}")    

        for zip in zips:
            os.replace(zip, f"Zip/{zip}")

        for doc in docs:
            os.replace(doc, f"Docs/{doc}")

        for media in medias:
            os.replace(media, f"Media/{media}")

        for software in softwares:
            os.replace(software, f"Software/{software}")

        for extra in extras:
            os.replace(extra, f"Extras/{extra}")
        
        resultLabel = Label(root,text="Done !!",font=('arial',12,'bold'), bg="light blue", fg="green")
        resultLabel.place(x=190,y=200)           
            
        
             
    files = os.listdir()
    files.remove("fileManager.py")
     

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


    appName = Label(root,text="File Manager",font=('arial',20,'bold'),
                    bg="light blue",fg='maroon')
    appName.place(x=135,y=15)

    labelFile = Label(root,text="Arrange your cluttered files to their proper folders.",font=('arial',12,'bold'), bg="light blue")
    labelFile.place(x=30,y=70)

   
    arrangeButton = Button(root,text=" Arrange ",font=('arial',12,'bold'),width=20,
                        bg="sky blue",fg='blue',command=moveFiles)
    arrangeButton.place(x=115,y=120)




    root.mainloop()
