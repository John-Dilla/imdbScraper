from os.path import dirname, join
import os

import pandas as pd
import urllib.request

from pandas.core.frame import DataFrame

# The basic root path of the local database
rootPath = join(os.getcwd(), 'database')

def createDatabase() -> None:
    """The utility method for creating the local database.
    """

    filmography = join(rootPath, 'filmography')
    biography = join(rootPath, 'biography')
    awards = join(rootPath, 'awards')

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

def writeToDirectory(folder: str, fileName: str, dataframe) -> None: 
    """The utility method for saving files to the directory in the local database.

    Args:
        folder (str): The concrete folder in the database.
        fileName (str): The concrete name of the specific file.
        dataframe ([type]): The actual dataframe.
    """

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
    """The utility method for saving the profile pictures of the actors.

    Args:
        fileName (str): The name of the file.
        imageURL (str): The URL from which the picture is retrieved.
    """

    picturePath = join(rootPath, "biography", fileName)+".jpg"
    urllib.request.urlretrieve(imageURL, picturePath)
    print("Saving File:", picturePath)


def getTable(folder: str, fileName: str) -> DataFrame:
    """The utility method for retrieving a specific table.

    Args:
        folder (str): The folder in which the designated file is stored.
        fileName (str): The name of the file.

    Returns:
        dataframe (DataFrame)]: The file converted to a pandas dataframe.
    """

    filePath = join(rootPath, folder, fileName)+".csv"
    dataframe = pd.read_csv(filePath, sep=';')
    if 'Year' in dataframe.columns:
        dataframe['Year'] = dataframe['Year'].astype('Int64')
    if 'Rating' in dataframe.columns:
        dataframe['Rating'] = dataframe['Rating'].astype('float')
    if 'Ranking' in dataframe.columns:
        dataframe['Ranking'] = dataframe['Ranking'].astype('Int64')
    return dataframe

def getUIPath(absolutePath: str, uiFile: str) -> str:
    """The utility method to construct the path to a UI file. 

    Args:
        absolutePath (str): The absolute path to the file.
        uiFile (str): The name of the UI file.

    Returns:
        pathUI (str): Returns the OS dependent path to the file.
    """
    ui_path = dirname(absolutePath)
    pathUI = join(ui_path, "ui", uiFile)
    return pathUI

def getPicture(id) -> str:
    """The utility method to construct the path to a jpg file. 

    Args:
        id (str): The IMDB-ID of an actor or actress.

    Returns:
        str: Returns the OS dependent path to the file.
    """
    pathUI = join(rootPath, "biography", id) + ".jpg"
    return pathUI