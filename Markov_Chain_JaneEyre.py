import nltk 
import random
import os, sys

# This is the absolute path to the source text.
file_path = os.path.join(sys.path[0], "source_text.txt")
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

# print(sorted(list(set(text.lower()))))

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

# Generation Algorithim 
# Goal: Randomly generate sentences
# 1: Get starting word ---> list of words followed by '.'
start_word = random.choice(word_pairs["."])
# 2: Next word in random sentence ---> list of words paired with the start word
next_word = random.choice(word_pairs[start_word])
# 3: Loop this process to keep generating new words in our sentence...
current_word = start_word
sentence_list = [start_word]
while current_word not in [".", "?", "!"]:
    next_word = random.choice(word_pairs[current_word])
    sentence_list.append(next_word)
    current_word = next_word

# formatting
sentence_list[0] = sentence_list[0].title() 
sentence = " ".join(sentence_list)
sentence = sentence.replace(" ,", ",")
sentence = sentence.replace(" :", ":")
sentence = sentence.replace(" ;", ";")
sentence = sentence.replace(" !", "!")
sentence = sentence.replace(" .", ".")
sentence = sentence.replace(" ?", "?")
print(sentence)