import re 


def make_sentence_list(text_string):
  ''''takes a string object, parses it by sentences and
  returns a list of those sentences'''

  # get rid of any unwanted extra characters
  text_string = text_string.replace('\ufeff', '')
  text_string = text_string.replace('\n', '')
  
  # compile regex for parsing by sentences
  sent_regex = re.compile('[^.]*\.')
  
  # initialize iterator for creating a list of sentences
  iterator = sent_regex.finditer(text_string)
  matched_text = []
  for match in iterator:
    matched_text.append(match.group())
  
  return matched_text

  

# open the text file and load into string object
with open('A_study_in_scarlet.txt', 'r') as holmes_file:
  book_txt = holmes_file.read()

sentence_list = make_sentence_list(book_txt)

print(sentence_list[0:10])
