import generator as gen 
import json

class SimPerson:
    
    def __init__(self, corpus, freq_dict={}, first_words=[]):
        self.corpus = corpus #text file with body of text 
        self.freq_dict = freq_dict
        self.first_words = first_words
    
    def generate_freq_dict(self):
        parsed_text = gen.generate_occurrence_dict(self.corpus) 
        occurency_dict = parsed_text.occ_dict
        sentence_first_words = parsed_text.first_words

        frequency_dict = gen.generate_freq_dict(occurency_dict)

        self.freq_dict = frequency_dict
        self.first_words = sentence_first_words

    def generate_sentence(self):
        person_sentence = gen.markov_sentence_generate(self.freq_dict, self.first_words)
        print(person_sentence)

    def export_freq_dict(self, out_filename):
        '''export frequency dictionary as json file'''
        with open(out_filename, 'w') as out_file:
            json.dump(self.freq_dict,out_file)

    
    def import_freq_dict(self):
        #import frequency dictionary from json
        

    def export_first_words(self):
        #export first words to text file

    def import_first_words(self):
        #import first words from text file

