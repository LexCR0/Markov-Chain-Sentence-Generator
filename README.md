## Project Description

This program generates random sentences in the style of a text that is provided. 

I utilized the Natural Language Toolkit to split up a body of text into a sequence of tokens. This sequence of tokens is then used to train a simple Markov chain model. The trained model generates sentences by predicting subsequent words given the current word until a period is produced. I utilized [*Jane Eyre*](https://www.gutenberg.org/files/1260/1260-h/1260-h.htm) by Charlotte Bronte to test my program.

## Examples

-

## Dependencies

- [Natural Language Toolkit](https://www.nltk.org/) - Used to work with human language data
