import os
import json
import shutil

os.chdir(input("输入工作路径："))
workPath = os.getcwd()

firstSubPath = tuple()
firstSubPath = os.listdir()

dirQuantityvalue = len(firstSubPath)


def getSubAbsPath():
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


def moveToFolder(objname, sourcePath):
    os.chdir(workPath)
    objectPath = os.path.join(workPath, objname)
    shutil.move(sourcePath, objectPath)


for i in range(0, dirQuantityvalue):
    firstabsPath = os.path.join(workPath, firstSubPath[i])
    os.chdir(firstabsPath)
    hasJsonPath = getSubAbsPath()
    os.chdir(hasJsonPath)

    try:
        name = getTitle()
        mkcontainfolder(name)
        moveToFolder(name, firstabsPath)
    except:
        print('error')
        initialize()
        continue

    initialize()

input("按任意键退出")
