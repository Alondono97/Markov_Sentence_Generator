# Markov_Sentence_Generator
Sentence generator using a markov chain with probabilities garnered from word frequency in a given text. For now I will be using A Study In Scarlet by Sir Arthur Conan Doyle pulled from Gutenburg.org.

## How to use:
* Fork the repo and run `python3 generator.py`
* If you cd into the Trump_Simulator directory, it will work the same way
* If you want to use a different .txt file, currently you'll have to go into the generator.py file and change the line 

`parsed_text = generate_occurrence_dict(<corpus.txt>)` 

to whatever your .txt file is called. (I plan to make the code more modular so you can simply use command line arguments, but I havent implemented it yet)

## To do:
* Clean up code (it's kind of a mess right now and I need to make it more readable/standardized/modular)
* Improve parsing for twitter corpuses


If you find any mistakes please point them out to me with sugestions of how to fix them! I'm sure to make a good amount and am trying to learn and improve!

