class Model:
    def __init__(self, corpus):
        self.each_word_number_of_occurrences_dict = {}
        self.each_bi_word_number_of_occurrences_dict = {}
        file_name = corpus + ".txt"
        f = open(file_name, "r")
        self.corpus = f.read()
        f.close()

        self.unigram_model_file_name = "unigram_model_of_" + file_name
        f = open(self.unigram_model_file_name, "w+")
        f.close()

        self.bigram_model_file_name = "bigram_model_of_" + file_name
        f = open(self.bigram_model_file_name, "w+")
        f.close()

    def model(self):
        all_words = self.corpus.split()
        known_words = set(all_words)
        for word in known_words:
            self.each_word_number_of_occurrences_dict[word] = 0
        unigram_model_dictionary = self.unigram_model(known_words, all_words)
        all_bi_words = list(map(' '.join, zip(all_words[:-1], all_words[1:])))
        known_bi_words = set(all_bi_words)
        for bi_word in known_bi_words:
            self.each_bi_word_number_of_occurrences_dict[bi_word] = 0
        bigram_model_dictionary = self.bigram_model(known_bi_words, all_bi_words, all_words)
        return [unigram_model_dictionary, bigram_model_dictionary]

    def unigram_model(self, known_words, all_words):
        # we can write the probabilitis to a file for better study
        # but we know writng to a file is an I/O operation and takes
        # a long time so for better performance I comment the lines
        # which are related to writing the result to file
        number_of_words = len(all_words)
        each_word_probability_dict = {}
        for word in all_words:
            self.each_word_number_of_occurrences_dict[word] = self.each_word_number_of_occurrences_dict[word] + 1
        # f = open(self.unigram_model_file_name, "a+")
        for word in known_words:
            probability = self.each_word_number_of_occurrences_dict[word] / number_of_words
            each_word_probability_dict[word] = probability
            #f.write(word + " " + str(probability) + "\n")
        #f.close()
        return each_word_probability_dict

    def bigram_model(self, known_bi_words, all_bi_words, all_words):
        # as explained in unigram_model function I comment the the lines
        # which are related to writing to a file
        #f = open(self.bigram_model_file_name, "a+")
        each_bi_word_probability_dict = {}
        for bi_word in all_bi_words:
            self.each_bi_word_number_of_occurrences_dict[bi_word] = self.each_bi_word_number_of_occurrences_dict[bi_word] + 1
        for bi_word in known_bi_words:
            # we know that function list.count in python simply iterates over all the elements
            # of the list and it's time complexity is O(n) and we also know that searching in a
            # dictionary is O(1) because dictionaries are hash tables and n is a big number
            # as a result it has considerable effect on performance if we make a dictionary of the
            # words and their number of occurrences when finding them out in unigram_model function
            # and just use them in here
            first_word = bi_word.split()[0]
            number_of_occurrences_of_first_word = self.each_word_number_of_occurrences_dict[first_word]
            number_of_occurrences_of_bi_word = self.each_bi_word_number_of_occurrences_dict[bi_word]
            probability = number_of_occurrences_of_bi_word / number_of_occurrences_of_first_word
            each_bi_word_probability_dict[bi_word] = probability
            #f.write(bi_word + " " + str(probability) + "\n")
        #f.close()
        return each_bi_word_probability_dict