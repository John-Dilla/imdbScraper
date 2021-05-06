import os
import pandas as pd

rootPath = os.path.join(os.getcwd(), 'database')
pathStructure1 = os.path.join(rootPath, 'filmography')
pathStructure2 = os.path.join(rootPath, 'biography')

def createDatabase():
    rootPath = os.path.join(os.getcwd(), 'database')
    filmography = os.path.join(rootPath, 'filmography')
    biography = os.path.join(rootPath, 'biography')
    awards = os.path.join(rootPath, 'awards')
    genre = os.path.join(rootPath, 'genre')
    try:
        os.makedirs(filmography)
    except OSError:
        pass
    try:
        os.makedirs(biography)
    except OSError:
        pass
    try:
        os.makedirs(awards)
    except OSError:
        pass
    try:
        os.makedirs(genre)
    except OSError:
        pass

def writeToDirectory(folder: str, fileName: str, dataframe) -> None: 
    print("Saving File:", os.path.join(rootPath, folder, fileName)+".csv")
    p = os.path.join(rootPath, folder, fileName)+".csv"
    dataframe.to_csv(p, mode='w', sep=';')