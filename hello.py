import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import csv
import re

term_array = []

with open('C:/Users/User/Desktop/text/csvs/terms.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        term_array.append(row[1])

unique_term_array = list(set(term_array))

##CHECK IF A TERM CONTAINS A SPACE

# for i in range(len(unique_term_array)):
for i in range(50):
    if re.search(r'\s', unique_term_array[i]):
        print(len(unique_term_array[i]))
        print(unique_term_array[i])
        new = unique_term_array[i].strip()
        print(len(new))
        print(unique_term_array[i])





'''
## CHECK ONE DESCTIPTION FOR TERMS IN UNIQUE TERM ARRAY
sample = "Backbreaker: Vengeance takes the intensity and AAA appeal of the original Backbreaker Football console game and combines it with the pick-up-and-play nature of the multi-million selling iPhone games to create a whole new one-of-a-kind sports experience for digital download on Xbox LIVE Arcade for Xbox 360. It takes as its inspiration the wildly popular ""Tackle Alley"" mini-game in Backbreaker Football to deliver an all-new arcade slant on football."

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

for sentence in tokenized_sentences:
    for word in sentence:
        for term in unique_term_array:
            if word == term:
                print(term)
'''
