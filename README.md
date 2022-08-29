## Project Description

This program generates random sentences in the style of a text that is provided. 

I utilized the Natural Language Toolkit to split up a body of text into a sequence of tokens. This sequence of tokens is then used to train a simple Markov chain model. The trained model generates sentences by predicting subsequent words, given the current word, until a period is produced. I utilized [*Jane Eyre*](https://www.gutenberg.org/files/1260/1260-h/1260-h.htm) by Charlotte Bronte and [*The Tell-Tale Heart*](https://www.gutenberg.org/files/1260/1260-h/1260-h.htm) by Edgar Allan Poe to test my program. While the sentences generated may be meaningless, they are often times grammatically correct and manage to retain the characteristic feeling Charlotte Bronte and Edgar Allan Poe evoke in their writing.
<br/><br/>



## Instructions

First, run Train.py to train the Markov chain model. This will save a pickle file containing the model. Next, run Generator.py to generate sentences.
<br/><br/>



## Hand-picked examples generated using *Jane Eyre*:

- "A book from my black train of terror confused answers."

- "My pulses throb of his uncovered head in a great pain: you to six miles."

- "The might see the calmer and embracing and considered only of an hour of what is hurt by the beginning: narrow staircase: six as a note was my hand, now so very sheets were expected, fervid eloquence, however, i demanded the stones which would not sufficiently, whistling through life and i thought; he relapsed into?"

- "She possessed of my heart."

- "o, mine, that object in a crimson cloth, told him or vice which we should either to catch the fact was very bright eyes glitter!"

- "Solitude are times in stately house was to fulfil every now at this very bloodless lip from you make?"

- "And the freezing spell of moonlight last; i have thought them, there, which aims; it; call her brazen coolness of her; for leaving nothing soft, which shall be offered my heart say."

- "You will spare him, and sat at thornfield, john was the antipodes of diana and veiled figure whose voice was a week; and it was very probable."

- "Finding that it: do not ponder business to persuade her improvement, i am your room but one with volcanic vehemence."

- "I could not for all is stone-blind, the woods and have struck me; bluntly."
<br/><br/>


## Hand-picked examples generated using *The Tell-Tale Heart*:

- "Above all closed, placed my head ached, no more tolerable than this?"

- "For madness is only a low, did not be gone."

- "The world slept, when i heard all was dead."

- "A hideous heart and night, but could i fancied a new anxiety seized me day broke, precisely upon the shriek had my brain; but over him, and pulled the hour had been lodged at ease."

- "The beating of a muffled sound, that distracted me."

- "He had i said, like the old man, in vain; suspicion of my sagacity."

- "All between the concealment of the old man, i felt myself of the very marrow in the point."

- "I grew furious as i dismembered the beating grew very profound old man felt myself, no doubt i could bear those hypocritical smiles no blood-spot whatever."

- "And kept quite still dark as a watch makes when my own in the heart increased."

- "So that sound that night i must scream or person: for he had stalked with its dreadful echo, undisturbed."




<br/><br/>

## Dependencies

- [Natural Language Toolkit](https://www.nltk.org/) - Used to tokenize text
