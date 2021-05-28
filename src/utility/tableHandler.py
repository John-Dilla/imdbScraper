import pandas as pd

import src.utility.fileHandler as io

def top5Movie(actorID: str):
    dataframe = io.getTable("filmography", actorID)
    top5 = dataframe[['Ranking', 'Name', 'Year', 'Genre']]
    return top5.head()

def ratingOverall(actorID: str):
    """Calculates the overall rating of an actor or actress

    Args:
        actorID (str): the IMDB-ID of an actor or actress

    Returns:
        overallRating (float): Returns the rating calculated over all movies
    """
    dataframe = io.getTable("filmography", actorID).dropna(subset=['Rating'])
    overallRating = dataframe['Rating'].mean().round(2)
    return overallRating

def ratingPerYear(actorID: str):
    dataframe = io.getTable("filmography", actorID).dropna(subset=['Rating'])
    perYearRating = dataframe.loc[:, ['Rating', 'Year']]
    perYearRating = perYearRating.groupby(['Year'], as_index=False).mean().round(2)
    perYearRating = perYearRating.sort_values('Year', ascending=False)
    return perYearRating