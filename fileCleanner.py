import os
from plyer import notification

def notify():
    Images = len([name for name in os.listdir("Images")])
    Docs = len([name for name in os.listdir("Docs")])
    Medias = len([name for name in os.listdir("Medias")])
    Programs = len([name for name in os.listdir("Programs")])
    Others = len([name for name in os.listdir("Others")])
    notification.notify(
        title=f"Total {Images+Docs+Medias+Programs+Others} were cleaned",
        message=f"Total files in Images are {Images}\nTotal files in Docs are {Docs}\nTotal files in Medias are {Medias}\nTotal files in Programs are {Programs}\nTotal files in Others are {Others}",
        timeout=10
    )
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def makeFolders(folderName,folders):
    for folder in folders:
        os.replace(folder,f"{folderName}/{folder}")
if __name__ == "__main__":
    files = os.listdir()
    files.remove('fileCleanner.py')
    createIfNotExist("Images")
    createIfNotExist("Docs")
    createIfNotExist("Medias")
    createIfNotExist("programs")
    createIfNotExist("others")
    imgExts = ['.png','.jpg','.jpeg','.webp','.ico']
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    docExts = ['.txt', '.docx', '.doc','.pdf']
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    mediaExts = ['.mp4', '.mp3', '.flv']
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    programExts = ['.py', '.c', '.cpp','.java','.html','.css','.js','.php','.sql']
    programs = [file for file in files if os.path.splitext(file)[1].lower() in programExts]
    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExts) and (ext not in docExts) and (ext not in mediaExts) and (ext not in programExts) and  os.path.isfile(file):
            others.append(file)
    makeFolders("Images",images)
    makeFolders("Docs",docs)
    makeFolders("Medias",medias)
    makeFolders("Programs",programs)
    makeFolders("Others",others)
    notify()
