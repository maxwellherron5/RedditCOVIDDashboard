"""

Author: Maxwell Herron
"""

from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import numpy as np

app = Flask(__name__)

# Listing of subreddits scanned
subreddits = ("worldnews", "news", "funny", "gaming", "pics", "science",
                  "videos", "AskReddit", "aww", "askscience", "Tinder",
                  "BlackPeopleTwitter", "politics", "dankmemes", "memes",
                  "PoliticalHumor", "WhitePeopleTwitter", "ABoringDystopia",
                  "Conservative", "nottheonion", "LateStageCapitalism")

# Primary dataframe extracted from CoronaScan results
results_df = pd.read_csv("../CoronaScan/results.csv", names=[i for i in subreddits])
# Stripping column name literals from dataframe
results_df = results_df.iloc[1:]

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/get_piechart_data')
def get_piechart_data():
    """
    Takes the sum of mentions for each subreddit. It then gets the percentage of
    the total mentions, and returns a dictionary containing subreddit/percent pairs.
    @return The dictionary containing all percentages of mentions associated
    with their respective Subreddit
    """
    # Initialize empty dictionary
    column_sums = {}
    for i in subreddits:
        # Maps each column value to an int value, converts to a list, takes sum
        column_sums[i] = sum(list(map(int, results_df[i])))
    column_percentages = get_percentage(column_sums)
    return column_percentages


def get_percentage(piechart_values):
    """
    Takes the input dictionary of all sums and returns the percentage of each sum
    @param The sum of each column in the dataframe
    @return The percentage of the sum of the column with respect to the total
    """
    total = sum(piechart_values.values())
    column_percentages = {}
    for key, value in piechart_values.items():
        column_percentages[key] = (value / total) * 100
    return column_percentages


if __name__ == '__main__':
    app.run(debug=True)
