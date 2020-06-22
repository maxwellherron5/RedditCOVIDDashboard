from flask import Flask, jsonify, render_template
import csv
import pandas as pd
import numpy as np

"""

Author: Maxwell Herron
"""

app = Flask(__name__)

results_df = pd.read_csv("../CoronaScan/results.csv")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/get_barchart_data')
def get_barchart_data():
    row_values = results_df.to_numpy()

    
if __name__ == '__main__':
    app.run(debug=True)
    