import pandas as pd

import src.utility.fileHandler as io

def top5Movie(actorID: str):
    dataframe = io.getTable("filmography", actorID)
    print(dataframe)
    top5 = dataframe[['Name', 'MovieYear', 'Genre']]
    print(top5)
    top5 = dataframe.head()
    print(top5)