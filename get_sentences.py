import csv
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

with open('test_data.txt', 'r') as f:
    sample = f.readlines()

sentence_sample = []

sentence_sample.append(sample[0].replace('\n', ''))

count = 0

for i in (range(2,len(sample))):
##    print(i)
##    print(sample[i])
##    print(sentence_sample[count])
##    print("\n")

    if sample[i] != sentence_sample[count]:
        sentence_sample.append(sample[i].replace('\n', ''))
        count+=1
        if count >150:
            break

##print(len(sentence_sample))
##print(sentence_sample)

with open('small_unique_description_sample.txt', 'w') as f:
    for item in sentence_sample:
        f.write("%s\n" % item)




##
##
##    for j in range(i,len(sample)):
##        if sample[j] != sample[j-1]:
##            sentence_sample.append(sample[j].replace('\n', ''))
##            count +=1
##            if count > 149:
##                break
##
##
##print(len(sentence_sample))
##



#sentences = nltk.sent_tokenize(sample)
##tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
##tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
##chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
##
##def extract_entity_names(t):
##    entity_names = []
##
##    if hasattr(t, 'label') and t.label:
##        if t.label() == 'NE':
##            entity_names.append(' '.join([child[0] for child in t]))
##        else:
##            for child in t:
##                entity_names.extend(extract_entity_names(child))
##
##    return entity_names
##
##entity_names = []
##for tree in chunked_sentences:
##    # Print results per sentence
##    # print extract_entity_names(tree)
##
##    entity_names.extend(extract_entity_names(tree))
##
#### Print all entity names
##  print entity_names
##
#### Print unique entity names
##
##with open('named_entities.txt', 'w') as f:
##    for item in entity_names:
##        f.write("%s\n" % item)
