import os
import pandas as pd

rootPath = os.path.join(os.getcwd(), 'database')

def createDatabase():
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

def getTable(folder: str, fileName: str):
    filePath = os.path.join(rootPath, folder, fileName)+".csv"
    dataframe = pd.read_csv(filePath, error_bad_lines=False)
    return dataframe