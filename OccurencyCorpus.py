
class OccurencyCorpus:

    def __init__(self):
        self.occ_dict = {} #dictionary of dictionaries of words->words->number of occurences
        self.first_words = [] #list consisting of first word in each sentence

    def get_frequencies(self):
        return self.occ_dict

    def get_first_words(self):
        return self.first_words
