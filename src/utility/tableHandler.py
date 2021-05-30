import pandas as pd
from pandas.core.frame import DataFrame

import src.utility.fileHandler as io

def top5Movie(actorID: str) -> DataFrame:
    """Retrieves the top 5 movie names of an actor or actress.
    Movies are selected by rating.

    Args:
        actorID (str): The IMDB-ID of an actor or actress.

    Returns:
        top5 (DataFrame): Returns a dataframe with the top 5 movies.
    """
    dataframe = io.getTable("filmography", actorID)
    top5 = dataframe[['Ranking', 'Name', 'Year', 'Genre']]
    return top5.head()

def ratingOverall(actorID: str) -> float:
    """Calculates the overall rating of an actor or actress.

    Args:
        actorID (str): The IMDB-ID of an actor or actress.

    Returns:
        overallRating (float): Returns the rating calculated over all movies.
    """
    dataframe = io.getTable("filmography", actorID).dropna(subset=['Rating'])
    overallRating = dataframe['Rating'].mean().round(2)
    return overallRating

def ratingPerYear(actorID: str) -> DataFrame:
    """Crates a rating table with an entry for each year. 
    The mean is calculated per grouped year.

    Args:
        actorID (str): The IMDB-ID of an actor or actress.

    Returns:
        perYearrating (DataFrame): A dataframe with a year column and a rating column.
    """
    dataframe = io.getTable("filmography", actorID).dropna(subset=['Rating'])
    perYearRating = dataframe.loc[:, ['Rating', 'Year']]
    perYearRating = perYearRating.groupby(['Year'], as_index=False).mean().round(2)
    perYearRating = perYearRating.sort_values('Year', ascending=False)
    return perYearRating