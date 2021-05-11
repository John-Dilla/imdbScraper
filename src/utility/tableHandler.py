import pandas as pd

import src.utility.fileHandler as io

def top5Movie(actorID: str):
    dataframe = io.getTable("filmography", actorID)
    top5 = dataframe[['Name', 'Year', 'Genre']]
    print(top5.head())

def ratingOverall(actorID: str):
    dataframe = io.getTable("filmography", actorID)
    top5 = dataframe[['Name', 'Year', 'Genre']]
    print(top5.head())

def ratingPerYear(actorID: str):
    dataframe = io.getTable("filmography", actorID)
    top5 = dataframe[['Name', 'Year', 'Genre']]
    print(top5.head())