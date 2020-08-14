import os

def createifnotexist(folder):
    if  not os.path.exists(folder):
        os.makedirs(folder)

def moveFiles(folderName, files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")
    

if __name__ == "__main__":
    
    files = os.listdir()
    files.remove("main.py")
    print(files)
    createifnotexist("Images")
    createifnotexist("Docs")
    createifnotexist("Media")
    createifnotexist("Others")
    imgExts = [".png", ".jpg","jpeg"]
    images = [file for file  in files if os.path.splitext(file)[1].lower() in imgExts]

    doc = [".txt", ".docx",".doc",".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in doc]

    mediaa = [".mp4",".mp3"]
    media = [file for file in files if os.path.splitext(file)[1].lower() in mediaa]
    others = []
    for file in files:
        otherexts = os.path.splitext(file)[1].lower()
        if (otherexts not in mediaa) and (otherexts not in doc) and (otherexts not in imgExts) and os.path.isfile(file):
            others.append(file)
    moveFiles("Images",images)
    moveFiles("Docs",docs)
    moveFiles("Media",media)
    moveFiles("Others",others)