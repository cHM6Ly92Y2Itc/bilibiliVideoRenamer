import os
import json
import shutil

os.chdir(input("输入工作路径："))
workPath = os.getcwd()

videoFolderName = tuple()
videoFolderName = os.listdir()

dirQuantityValue = len(videoFolderName)


def getHasJsonPath():
    currentPath = os.getcwd()
    dirname = tuple()
    dirname = os.listdir()
    absPath = os.path.join(currentPath, dirname[0])
    return absPath


def initialize():
    os.chdir(workPath)


def getTitle():
    with open(r'entry.json', 'r', encoding='utf-8', errors='ignore') as f:
        metadata = json.load(f)
        print(metadata['title'])
        return metadata['title']


def mkcontainfolder(folderName):
    createFolder = os.path.join(workPath, folderName)
    os.makedirs(createFolder)


def moveToFolder(objName, sourcePath):
    os.chdir(workPath)
    objectPath = os.path.join(workPath, objName)
    shutil.move(sourcePath, objectPath)


for i in range(0, dirQuantityValue):
    videoFolderAbsPath = os.path.join(workPath, videoFolderName[i])
    os.chdir(videoFolderAbsPath)
    hasJsonPath = getHasJsonPath()
    os.chdir(hasJsonPath)

    try:
        name = getTitle()
        mkcontainfolder(name)
        moveToFolder(name, videoFolderAbsPath)
    except:
        print('error')
        initialize()
        continue

    initialize()

input("按任意键退出")
