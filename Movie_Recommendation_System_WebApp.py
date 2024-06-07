# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:29:57 2024

@author: prachet
"""

import pandas as pd
import difflib

import numpy as np
import pickle
import streamlit as st

df = pd.read_csv("C:/Users/prachet/OneDrive - Vidyalankar Institute of Technology/Desktop/Coding/Machine Learning/ML-Project-18-Movie Recommendation System using Machine Learning/movies.csv")

list_of_all_titles = df['title'].tolist()

#loading. the saved model
with open('C:/Users/prachet/OneDrive - Vidyalankar Institute of Technology/Desktop/Coding/Machine Learning/ML-Project-18-Movie Recommendation System using Machine Learning/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

#creating a function for prediction

def movie_recommendation_system(input_data):
    
    find_close_match = difflib.get_close_matches(input_data,list_of_all_titles)
    
    close_match = find_close_match[0]
    
    index_of_the_movie = df[df.title == close_match]['index'].values[0]
    
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    
    sorted_similar_movies = sorted(similarity_score, key = lambda x: x[1], reverse = True)
    
    i = 1
    
    x = []
    
    for movie in sorted_similar_movies:
      index = movie[0]
      title_from_index = df[df.index==index]['title'].values[0]
      if (i<=16):
        y = title_from_index
        i=i+1
        x.append(y)
    
    return x
  
    
  
def main():
    
    #giving a title
    st.title('Movie Recommendation Web App')
    
    #getting input data from user
    
    movie_name = st.text_input('Enter your fav movie name:')
    
    # code for prediction
    movies = ''
    
    #creating a button for Prediction
    if st.button('Recommend Movies'):
        movies = movie_recommendation_system(movie_name)
    
    for i in range(1,len(movies)):
        st.success(movies[i])
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    

