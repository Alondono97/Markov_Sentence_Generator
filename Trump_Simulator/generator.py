import re 
import numpy as np 
import OccurencyCorpus

def make_sentence_list(text_string):
  ''''takes a string object, parses it by sentences and
  returns a list of lists. Each sublist consists of a sentence
  parsed by words of said sentence'''

  # get rid of any unwanted extra characters
  text_string = text_string.replace('\ufeff', '')
  text_string = text_string.replace('\n', ' ')
  
  # compile regex for parsing by sentences
  sent_regex = re.compile('[^.]*\.')
  
  # initialize iterator for creating a list of sentences
  #itereator lets you loop through the regex matches
  iterator = sent_regex.finditer(text_string)
  
  matched_text = []
  for match in iterator:
    #split the sentence by white space to 'tokenize' the words
    #store words as list called 'words'
    words = match.group().split()
    matched_text.append(words)
  
  return matched_text

def generate_occurrence_dict(file_name):
  # returns tuple:
  # first thing it returns is the occurences dictionary
  # second thing returned is a list of 'first words' with which to begin a sentence

  # open the text file and load into string object
  with open(file_name, 'r') as text_file:
    book_txt = text_file.read()

  sentence_list = make_sentence_list(book_txt)

  # the variable named words will be an OccurencyCorpus object which holds:
  # a dictionary of dictionaries keeping track of word occurence
  # a list of first words in each sentence
  occ = OccurencyCorpus.OccurencyCorpus() 
  words = {}
  first_words = []
  for sentence in sentence_list:
    first_words.append(sentence[0])
    for i in range(len(sentence)):
      # each 'i' represents a word  in the sentence
      curr_word = sentence[i]
    
      if i < len(sentence) - 1 :
        #if not the last word in the sentence
        next_word = sentence[i+1]
        if curr_word in words:
          #if the current word has been ecountered before
          #check to see if the next word has been encountered
          if next_word in words[curr_word]:
            #if next word has been encountered increase occurence
            words[curr_word][next_word] += 1
          else:
            #if next word has not been encountered, initialize occurence to 1
            words[curr_word][next_word] = 1        
        else:
          # if the curr_word has not yet been encountered, make a new instance and make its next_word occurrence == 1
          words[curr_word] = {}  
          words[curr_word][next_word] = 1 
      else:
        '''if it is the last word in the sentence
        map the word to a blank space of frequency 1
        (this is for words that end in a period, for future revisions
        parse out period earlier, change whitespace to a period and incease frequency every occurence)
        '''
        if curr_word in words:
          words[curr_word][' '] = 1
        else: 
          words[curr_word] = {}
          words[curr_word][' '] = 1 

  occ.occ_dict = words
  occ.first_words = first_words
  return occ 

def generate_freq_dict(occ_dict):
  #given a dictionary of words mapped to dictionaries of words mapped to number of occurences of words
  #converts occurences to frequency
  for word in occ_dict:
    values_list = occ_dict[word].values() #get the occurences into a list
    freq_total = sum(values_list) # sum up occurences 
    for inner_word in occ_dict[word]:
      occ_dict[word][inner_word] = occ_dict[word][inner_word]/freq_total #replace occurences with their fraction of the total to get freq
  return occ_dict

def markov_sentence_generate(freq_dict, first_words):
  #given frequency dict and a list of first words generate a pseudo sentence using markov chain

  sent_len = 0 #length of sentence 
  final_sentence = ''

  #initial word/state for the markov chain, generated randomly with equal probability
  current_state = np.random.choice(first_words)  
  final_sentence += current_state #add it to the sentence

  while True:

    if current_state != ' ':

      #list of frequency values corresponding to the next words(state) after the current word(state)
      #And list of states that map to the frequencies 
      f_list = list(freq_dict[current_state].values()) 
      s_list = list(freq_dict[current_state].keys()) 


      #generate next state randomly, but based on probabilities
      next_state = np.random.choice(s_list, replace=True, p= f_list) 

      # add to sentence
      final_sentence += ' ' + next_state 

      current_state = next_state # change states
    else:
      #when the sentence reaches its final word, end the while loop
      break

  print(final_sentence)


# ------------------------------------------------------------------------------------------------------------------
#OccurencyCorpus object containing an occurency dictionary and a first words list
parsed_text = generate_occurrence_dict('A_study_in_scarlet.txt') 
occurency_dict = parsed_text.occ_dict
sentence_first_words = parsed_text.first_words

frequency_dict = generate_freq_dict(occurency_dict)

markov_sentence_generate(frequency_dict, sentence_first_words)

#-------------------------------------------------------------------------------------------------------------------



