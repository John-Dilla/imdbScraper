import os
import pandas as pd
import urllib.request

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

    # Exception can happen when executed for the very first time. 
    # If so, no database is found.
    try:
        dataframe.to_csv(p, mode='w', sep=';')
    except:
        createDatabase()
        dataframe.to_csv(p, mode='w', sep=';')

def writeProfilepicture(fileName: str, imageURL: str) -> None:
    picturePath = os.path.join(rootPath, "biography", fileName)+".jpg"
    urllib.request.urlretrieve(imageURL, picturePath)


def getTable(folder: str, fileName: str):
    filePath = os.path.join(rootPath, folder, fileName)+".csv"
    dataframe = pd.read_csv(filePath, sep=';')
    if 'Year' in dataframe.columns:
        dataframe['Year'] = dataframe['Year'].astype('Int64')
    if 'Rating' in dataframe.columns:
        dataframe['Rating'] = dataframe['Rating'].astype('float')
    if 'Ranking' in dataframe.columns:
        dataframe['Ranking'] = dataframe['Ranking'].astype('Int64')
    return dataframe