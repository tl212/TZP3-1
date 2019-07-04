from flask import Flask, render_template, request
import pandas as pd
from flask import *
import numpy as np
import os
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Reader, Dataset, SVD, evaluate
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        movie_name = request.form['title']
        user = request.form['userId']
        data = pd.read_csv('movies_bow.csv')
        print(os.getcwd())
        indices = pd.Series(data.index, index=data['Title'])
        idx = indices[movie_name]
        count = CountVectorizer()
        count_matrix = count.fit_transform(data['bag_of_words'])
        cosine_sim = cosine_similarity(count_matrix, count_matrix)
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:26]
        movie_indices = [i[0] for i in sim_scores]
        movies_map = data.copy()
        movies_map.reset_index(inplace=True)
        movies_map = movies_map.rename(columns={'index': 'id'})
        movies = movies_map.iloc[movie_indices][['Title', 'id']]
        new_ratings = pd.read_csv('new_ratings.csv')
        reader = Reader()
        Dataset.load_from_df(new_ratings[['userId', 'movieId', 'rating']], reader)
        svd = joblib.load('svd.pkl')
        movies['est'] = movies['id'].apply(lambda x: svd.predict(user, movies_map.loc[x]['movieId']).est)
        movies = movies.sort_values('est', ascending=False)
        top10_df = pd.DataFrame(movies['Title'][:11])
        results = top10_df.to_dict('records')
        columnNames = top10_df.columns.values
                
        return render_template('recommendation.html', records = results, colnames = columnNames)


if __name__ == '__main__':
    app.run(debug=True)