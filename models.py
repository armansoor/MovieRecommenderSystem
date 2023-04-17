import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, data_file):
        self.movies = pd.read_csv(data_file)
        self.tfidf = TfidfVectorizer(stop_words='english')
        
    def _get_cosine_sim(self, tfidf_matrix):
        return cosine_similarity(tfidf_matrix, tfidf_matrix)
        
    def _get_recommendations(self, title, cosine_sim):
        idx = self.movies[self.movies['title'] == title].index[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return self.movies['title'].iloc[movie_indices]
        
    def get_movie_recommendations(self, title):
        self.movies['overview'] = self.movies['overview'].fillna('')
        tfidf_matrix = self.tfidf.fit_transform(self.movies['overview'])
        cosine_sim = self._get_cosine_sim(tfidf_matrix)
        recommendations = self._get_recommendations(title, cosine_sim)
        return recommendations
