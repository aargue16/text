import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
#nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import csv

from nltk.chunk import conlltags2tree, tree2conlltags
from pprint import pprint

desc_array = []


with open('C:/Users/User/Desktop/test_data.csv', 'r') as csvfile:
    desc_reader = csv.reader(csvfile)

    for row in desc_reader:
        desc_array.append(row[0])


for j in desc_array[1:2]:
    
    words = nltk.word_tokenize(j)
    tagged = nltk.pos_tag(words)

##    iob_tagged = tree2conlltags(tagged)
##    pprint(iob_tagged)


    namedEnt = nltk.ne_chunk(tagged, binary=True)
    print(namedEnt)


##    for i in tagged:
##        if i[1] == "NNP":
##            print(i[0])


