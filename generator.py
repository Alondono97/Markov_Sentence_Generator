import re 
import numpy as np 

def make_sentence_list(text_string):
  ''''takes a string object, parses it by sentences and
  returns a list of lists. Each sublist consists of a sentence
  parsed by words of those sentences'''

  # get rid of any unwanted extra characters
  text_string = text_string.replace('\ufeff', '')
  text_string = text_string.replace('\n', ' ')
  
  # compile regex for parsing by sentences
  sent_regex = re.compile('[^.]*\.')
  
  # initialize iterator for creating a list of sentences
  iterator = sent_regex.finditer(text_string)
  
  matched_text = []
  for match in iterator:
    #split the sentence by white space to 'tokenize' the words
    words = match.group().split()
    matched_text.append(words)
  
  return matched_text

  

# open the text file and load into string object
with open('A_study_in_scarlet.txt', 'r') as holmes_file:
  book_txt = holmes_file.read()

sentence_list = make_sentence_list(book_txt)
# print(sentence_list[0:2])

words = {} #dictionary of dictionaries keeping track of word occurences
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
      '''
      if it is the last word in the sentence
      map the word to a blank space of frequency 1
      (this is for words that end in a period, for future revisions
      parse out period earlier, change whitespace to a period and incease frequency every occurence)
      '''
      if curr_word in words:
        words[curr_word][' '] = 1
      else: 
        words[curr_word] = {}
        words[curr_word][' '] = 1 

#Now we change the occurence number into frequencies by summing the occurences in each sub dictionary
#then dividing each occurence by the sum
for word in words:
  values_list = words[word].values() #get the occurences into a list
  freq_total = sum(values_list) # sum up occurences 
  for inner_word in words[word]:
    words[word][inner_word] = words[word][inner_word]/freq_total #replace occurences with their fraction of the total to get freq

#we are now ready to begin writing the markov chain

sent_len = 0 #length of sentence 
final_sentence = ''

# current_state = 'The' #initial word/state for the markov chain to begin at #generate randomly later

current_state = np.random.choice(first_words) #initial word/state for the markov chain, generated randomly with equal probability 
final_sentence += ' ' + current_state #add it to the sentence

while True:

  if current_state != ' ':
    f_list = list(words[current_state].values()) #list of frequency values corresponding to the next words(state) after the current word(state)
    s_list = list(words[current_state].keys()) #list of states that map to the frequencies 

    next_state = np.random.choice(s_list, replace=True, p= f_list) #generate next state randomly, but based on probabilities

    final_sentence += ' ' + next_state # add to sentence

    current_state = next_state # change states
  else:
    #when the sentence reaches its final word, end the while loop
    break

print(final_sentence)
  


