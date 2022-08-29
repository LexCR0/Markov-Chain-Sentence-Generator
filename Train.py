import nltk 
import random
import os, sys
import pickle 

# This is the absolute path to the source text.
file_path = os.path.join(sys.path[0], "JaneEyre_text.txt")
with open(file_path, encoding="utf-8") as f:
    text = f.read()

text = text.replace("\n\n"," ")
text = text.replace("\n"," ")
text = text.replace('(', '')
text = text.replace(')', '')
text = text.replace('“', '')
text = text.replace('”', '')
text = text.replace('‘', '')
text = text.replace('’', '')

word_list = nltk.word_tokenize(text)
word_list = [word.lower() for word in word_list]
word_pairs = {}

for i in range(len(word_list)-1):
    current_word = word_list[i]
    next_word = word_list[i+1]
    # check - do we already have a key for this word?
    if current_word in word_pairs.keys():
        word_pairs[current_word].append(next_word)
    else: 
        word_pairs[current_word] = [next_word]

with open('word_pairs.pkl', 'wb') as f:
    pickle.dump(word_pairs, f)


