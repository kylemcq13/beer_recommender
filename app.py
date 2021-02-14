import flask
import difflib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

app = flask.Flask(__name__, template_folder='templates')

df = pd.read_csv(r'F:\beer_recommender\beer_recs.csv', error_bad_lines=False)

#using lemmatized_text, create the corpus
corpus = df['adjectives/nouns']

#FEATURE EXTRACTION
tfidf_model = TfidfVectorizer(max_features=500,
                             max_df=0.25,
                             min_df=0.01)

tfidf_matrix = tfidf_model.fit_transform(corpus).todense()

#calculate the cosine similarity of the matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

#Construct a reverse mapping of indices and beer names, and drop duplicate names, if any
indices = pd.Series(df.index, index=df['Name']).drop_duplicates()

# Function that takes in beer name as input and gives recommendations 
def content_recommender(title, cosine_sim=cosine_sim, df=df, indices=indices):
    # Obtain the index of the beer that matches the name
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    beer_indices = [i[0] for i in sim_scores]

    
    return df[['style', 'brewery_name', 'beer_name']].iloc[beer_indices]

# Set up the main route
@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        m_name = flask.request.form['beer_name']  #beer_name should be defined in index.html
        m_name = m_name.title()
        if m_name not in all_titles:
            return(flask.render_template('negative.html',name=m_name))
        else:
            result_final = content_recommender(m_name)
            names = []
            style = []
            breweries = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                style.append(result_final.iloc[i][1])
                breweries.append(result_final.iloc[i][1])


            return flask.render_template('positive.html',beer_names=names,beer_style=style,brewery=breweries,
                                         search_name=m_name)  #all variables here should be defined in the postive.html page

if __name__ == '__main__':
    app.run()
