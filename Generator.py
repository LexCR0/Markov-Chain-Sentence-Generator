import random
import pickle 

# Generation Algorithim 
with open('word_pairs.pkl', 'rb') as f:
    word_pairs = pickle.load(f)

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

