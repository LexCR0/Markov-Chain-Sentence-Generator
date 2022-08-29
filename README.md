## Project Description

This program generates random sentences in the style of a text that is provided. 

I utilized the Natural Language Toolkit to split up a body of text into a sequence of tokens. This sequence of tokens is then used to train a simple Markov chain model. The trained model generates sentences by predicting subsequent words given the current word until a period is produced. I utilized [*Jane Eyre*](https://www.gutenberg.org/files/1260/1260-h/1260-h.htm) by Charlotte Bronte to test my program. While the sentences generated lack proper syntax, they manage to retain the feeling Charlotte Bronte evokes in her writing.
<br/><br/>


## Instructions

First, run Train.py to train the Markov chain model. This will save a pickle file. Next, run the Generator.py to generate sentences.
<br/><br/>



## Hand-picked examples generating using *Jane Eyre*:

- "A book from my black train of terror confused answers."

- "My pulses throb of his uncovered head in a great pain: you to six miles."

- "The might see the calmer and embracing and considered only of an hour of what is hurt by the beginning: narrow staircase: six as a note was my hand, now so very sheets were expected, fervid eloquence, however, i demanded the stones which would not sufficiently, whistling through life and i thought; he relapsed into?"

- "She possessed of my heart."

- "o, mine, that object in a crimson cloth, told him or vice which we should either to catch the fact was very bright eyes glitter!"

- "At the bed of her actions, this plan to merit record on the course, what are all would make a silver bonnet and music."

- "Solitude are times in stately house was to fulfil every now at this very bloodless lip from you make?"

- "And the freezing spell of moonlight last; i have thought them, there, which aims; it; call her brazen coolness of her; for leaving nothing soft, which shall be offered my heart say."

- "You will spare him, and sat at thornfield, john was the antipodes of diana and veiled figure whose voice was a week; and it was very probable."

- "I intimated my crib last kiss on to supply the hill-top above and i longed, and it was a light he had been spoken!"

- "Finding that it: do not ponder business to persuade her improvement, i am your room but one with volcanic vehemence."

- "I mean what if a gay tones of fate purposely to serve elsewhere than the look."

- "You already gone for some years since his uncovered head is visible to night: i had never lived quietly."

- "I could not for all is stone-blind, the woods and have struck me; bluntly."
<br/><br/>




## Dependencies

- [Natural Language Toolkit](https://www.nltk.org/) - Used to tokenize text
