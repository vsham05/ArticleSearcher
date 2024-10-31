import gensim
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def sentence_vector(sentence, model):
    words = sentence.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    return np.mean(word_vectors, axis=0)


def finds(text):
    MODEL = gensim.models.Word2Vec.load("word2vecTESTVER.model")
    df = pd.read_csv('data.csv')
    df = df.dropna()
    df['title'] = df['title'].apply(lambda x: x.capitalize())
    titles, links, texts = df['title'].values, df['link'].values, df['FullText'].values

    p = []

    for sentence in texts:
        vec1 = sentence_vector(sentence, MODEL)
        vec2 = sentence_vector(text.lower(), MODEL)
        try:
            p.append([sentence, cosine_similarity([vec1], [vec2])])
        except:
            p.append([sentence, 0.0])

    
    props = sorted(p, key=lambda x: -x[1])[0:25]
   
    res = []
    for e in props:
        if e[-1] > 0.43:
            index = texts.tolist().index(e[0])
            res.append([titles[index], links[index]])


    return res


def dataset_creator(categories):
    res = []
    categ = {'Математика': 'math.csv',
             'Информационные технологии и электроника': 'elec.csv',
             'Компьютерные науки': 'cs.csv',
             'Экономика': 'economy.csv'}
    for c in categories:
        res.append(pd.read_csv(categ[c]))
    df = pd.concat(res)
    df.to_csv('data.csv', index=False)
        
    