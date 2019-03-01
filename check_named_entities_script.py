import csv
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

##read each row of the csv into an array
results = []
with open("C:/Users/User/Desktop/check_named_entities_mickey.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)

##isolate only the descriptions and put them into an array
sample=[]
for i in range(len(results)):
    sample.append(results[i][22])

##isolate only the game_id and put them into an array
ids=[]
for i in range(len(results)):
    ids.append(results[i][1])


##remove all the quotation marks
for i in range(len(sample)):
    sample[i] = sample[i].replace('"', '')

for j in range(len(sample)):

    description = sample[j]
    ##print(description)


    ##Extract the named entitites from the first entry only
    sentences = nltk.sent_tokenize(sample[j])
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)

    def extract_entity_names(t):
        entity_names = []

        if hasattr(t, 'label') and t.label:
            if t.label() == 'NE':
                entity_names.append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))

        return entity_names

    entity_names = []
    for tree in chunked_sentences:
        ##Print results per sentence
        ##print(extract_entity_names(tree))

        entity_names.append(extract_entity_names(tree))


    ##Put the entity names and the description together in an array
    data_row = ["NA","NA","NA","NA","NA","NA","NA","NA","NA","NA",
                "NA","NA","NA","NA","NA","NA","NA","NA","NA","NA",
                "NA","NA"]

    for i in range(len(entity_names[0])):
        data_row[i+1] = entity_names[0][i]

    ##Add the game_id to first column and the description to the last
    data_row[0]=ids[j]
    data_row[21]=description

    with open('C:/Users/User/Desktop/algo_mickey.csv', 'a') as f:
        writer = csv.writer(f,lineterminator = '\n')
        writer.writerow(data_row)


