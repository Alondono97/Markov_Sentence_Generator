import re 


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

words = {}

for sentence in sentence_list:
  for i in range(len(sentence)):
    # each 'i' represents a word  in the sentence
    if i < len(sentence):
      ''' there is an error here. the first loop goes into an empty dict so it cannot be index.
      fortwith, the sub dictionary will be empty as well. need a conditional to address this.'''
      value = words[i].get(words[i+1])
      if value == None:
        # if the word has not yet been encountered, make its occurrence 1
        words[i][words[i+1]] = 1
      else:
        # increase occurence of word  
        words[i][words[i+1]] += 1


