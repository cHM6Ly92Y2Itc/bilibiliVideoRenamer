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
        return illegalCharacterRemove(metadata['title'])


# 去除entry.json末尾多余花括号
def correctJson():
    try:
        os.rename("entry.json", "entry_backup.json")
    except FileExistsError:
        os.rename("entry_backup.json", "entry_backup2.json")
        os.rename("entry.json", "entry_backup.json")

    with open(r'entry_backup.json', 'r', encoding='utf-8', errors='ignore') as f:
        f_str = f.read()
        docs = list(f_str)
        lenth = len(docs)
        docs[lenth - 1] = ""
        docs = list(map(str, docs))
        rewriteDocs = ''.join(docs)
    with open(r'entry.json', 'w+', encoding='utf-8', errors='ignore') as nf:
        nf.write(rewriteDocs)


def mkcontainfolder(folderName):
    createFolder = os.path.join(workPath, folderName)
    os.makedirs(createFolder)


def moveToFolder(objName, sourcePath):
    os.chdir(workPath)
    objectPath = os.path.join(workPath, objName)
    shutil.move(sourcePath, objectPath)


# 过滤文件夹名不允许的特殊字符
def illegalCharacterRemove(string):
    tempList = list(string)
    newList = filter(isIllegalCharacter, tempList)
    newlist = list(map(str, newList))
    newTitle = ''.join(newlist)
    return newTitle


# 判断特殊字符
def isIllegalCharacter(n):
    if (n == "\\" or n == "/" or n == ":" or n == "*" or n == "?" or n == "\"" or n == "<" or n == ">" or n == "|"):
        return False
    else:
        return True


for i in range(0, dirQuantityValue):
    videoFolderAbsPath = os.path.join(workPath, videoFolderName[i])
    os.chdir(videoFolderAbsPath)
    hasJsonPath = getHasJsonPath()
    os.chdir(hasJsonPath)

    try:
        name = getTitle()
        mkcontainfolder(name)
        moveToFolder(name, videoFolderAbsPath)
    except json.JSONDecodeError:
        try:
            correctJson()
            name = getTitle()
            mkcontainfolder(name)
            moveToFolder(name, videoFolderAbsPath)
        except json.JSONDecodeError:
            correctJson()
            name = getTitle()
            mkcontainfolder(name)
            moveToFolder(name, videoFolderAbsPath)

    except:
        print("Unknown Error")

initialize()

input("按任意键退出")
