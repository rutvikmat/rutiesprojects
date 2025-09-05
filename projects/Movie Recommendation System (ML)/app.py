from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Load movie data and compute similarity matrix
df = pd.read_csv('movies.csv')
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title']).drop_duplicates()


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]  # Get top 3 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    selected_movie = None
    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommendations = get_recommendations(selected_movie)

    movie_titles = df['title'].tolist()
    return render_template('index.html', movies=movie_titles, recommendations=recommendations, selected=selected_movie)


if __name__ == '__main__':
    app.run(debug=True)