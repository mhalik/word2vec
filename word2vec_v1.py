# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:32:55 2020

@author: smarthalik
"""

# Import the pandas package, then use the "read_csv" function to read
# the labeled training data
import pandas as pd       
train = pd.read_csv("word2vec\labeledTrainData.tsv", header=0, \
                    delimiter="\t", quoting=3)

from bs4 import BeautifulSoup

example1 = BeautifulSoup(train["review"][0], features="html.parser")

#print(train["review"][0])
#print(example1.get_text())

import re
# Use regular expressions to do a find-and-replace
letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                      example1.get_text() )  # The text to search
#print(letters_only)

lower_case = letters_only.lower()        # Convert to lower case
words = lower_case.split()               # Split into words

#print(words)
#import nltk
#nltk.download()  # Download text data sets, including stop words

from nltk.corpus import stopwords # Import the stop word list
#print(stopwords.words("english")) 

# Remove stop words from "words"
words = [w for w in words if not w in stopwords.words("english")]
#print(words)

def review_to_words( raw_review ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review,features="html.parser").get_text() 
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))   
    
clean_review = review_to_words( train["review"][0] )
#print(clean_review)


#%%
# Get the number of reviews based on the dataframe column size
num_reviews = train["review"].size

# Initialize an empty list to hold the clean reviews
clean_train_reviews = []

# Loop over each review; create an index i that goes from 0 to the length
# of the movie review list 
for i in range( 0, num_reviews ):
    # Call our function for each one, and add the result to the list of
    # clean reviews
    clean_train_reviews.append( review_to_words( train["review"][i] ) )

