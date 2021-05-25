from os.path import dirname, join
import os

import pandas as pd
import urllib.request

rootPath = join(os.getcwd(), 'database')

def createDatabase():
    filmography = join(rootPath, 'filmography')
    biography = join(rootPath, 'biography')
    awards = join(rootPath, 'awards')
    genres = join(rootPath, 'genres')

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
        os.makedirs(genres)
    except OSError:
        pass

def writeToDirectory(folder: str, fileName: str, dataframe) -> None: 
    print("Saving File:", join(rootPath, folder, fileName)+".csv")
    p = join(rootPath, folder, fileName)+".csv"

    # Exception can happen when executed for the very first time. 
    # If so, no database is found.
    try:
        dataframe.to_csv(p, mode='w', sep=';')
    except:
        createDatabase()
        dataframe.to_csv(p, mode='w', sep=';')

def writeProfilepicture(fileName: str, imageURL: str) -> None:
    picturePath = join(rootPath, "biography", fileName)+".jpg"
    urllib.request.urlretrieve(imageURL, picturePath)
    print("Saving File:", picturePath)


def getTable(folder: str, fileName: str):
    filePath = join(rootPath, folder, fileName)+".csv"
    dataframe = pd.read_csv(filePath, sep=';')
    if 'Year' in dataframe.columns:
        dataframe['Year'] = dataframe['Year'].astype('Int64')
    if 'Rating' in dataframe.columns:
        dataframe['Rating'] = dataframe['Rating'].astype('float')
    if 'Ranking' in dataframe.columns:
        dataframe['Ranking'] = dataframe['Ranking'].astype('Int64')
    return dataframe

def getUIPath(absolutePath, uiFile: str):
    ui_path = dirname(absolutePath)
    pathUI = join(ui_path, "ui", uiFile)
    return pathUI

def getPicture(id):
    pathUI = join(rootPath, "biography", id) + ".jpg"
    return pathUI