import os
import pandas as pd

rootPath = os.path.join(os.getcwd(), 'database')
pathStructure1 = os.path.join(rootPath, 'filmography')
pathStructure2 = os.path.join(rootPath, 'biography')

def createDatabase():
    rootPath = os.path.join(os.getcwd(), 'database')
    pathStructure1 = os.path.join(rootPath, 'filmography')
    pathStructure2 = os.path.join(rootPath, 'biography')
    pathStructure3 = os.path.join(rootPath, 'awards')
    try:
        os.makedirs(pathStructure1)
    except OSError:
        pass
    try:
        os.makedirs(pathStructure2)
    except OSError:
        pass
    try:
        os.makedirs(pathStructure3)
    except OSError:
        pass

def writeToDirectory(folder: str, fileName: str, dataframe) -> None: 
    print("Saving File:", os.path.join(rootPath, folder, fileName)+".csv")
    p = os.path.join(rootPath, folder, fileName)+".csv"
    dataframe.to_csv(p, mode='w', sep=';')