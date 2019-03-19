import generator as gen 
import json

class SimPerson:
    
    def __init__(self, name, corpus, freq_dict={}, first_words=[]):
        self.name = name #name of simulated person
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
        return person_sentence

    def export_freq_dict(self):
        '''export frequency dictionary as json file'''

        out_filename = self.name + '_freq.json'
        with open(out_filename, 'w') as out_file:
            json.dump(self.freq_dict,out_file)

    
    def import_freq_dict(self, filename):
        #import frequency dictionary from json
        try:
            with open(filename) as json_file:
                self.freq_dict = json.load(json_file)
        except IOError:
            print('Could not open file:', filename)

    def export_first_words(self):
        #export first words to text file
        out_filename = self.name + '_first_words.txt'
        with open(out_filename, 'w') as out_file:
            for word in self.first_words:
                out_file.write(word + ' ')

    def import_first_words(self, filename):
        #import first words from text file
        try:
            with open(filename, 'r') as words_file:
                first_words_string = words_file.readline()
                self.first_words = first_words_string.split()
        except IOError:
            print('Could not open file:', filename)



