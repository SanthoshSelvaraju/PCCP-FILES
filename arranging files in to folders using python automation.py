import os
import shutil


def Automatefolder():
    pathOfFolder="C:\\Users\\santhosh\\Documents\\test"
    files=[f for f in os.listdir(pathOfFolder)]
    for file in files:
        fileType=file.split('.')
        if len(fileType) >=2:
            folderName=pathOfFolder+'\\'+fileType[1]+'_Folder'
            if os.path.isdir(folderName):
                shutil.move(pathOfFolder+'\\'+file,folderName+'\\'+file)
                continue
            else:
                os.mkdir(folderName)
                shutil.move(pathOfFolder + '\\' + file, folderName + '\\' + file)


if __name__=="__main__":
    Automatefolder()
