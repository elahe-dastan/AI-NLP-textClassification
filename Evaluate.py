import re
from Classification import Classification


class Evaluate:
    def __init__(self, test_corpus, models):
        self.test_file_name = test_corpus + ".txt"
        self.models = models
        self.table = {}

    def initialize_table(self):
        for actual in self.models:
            predicted_dict = {}
            for predicted in self.models:
                predicted_dict[predicted] = 0
            self.table[actual] = predicted_dict

    def update_table(self):
        f = open(self.test_file_name, "r")
        new_title = 0
        previous_title = ""
        corpus = ""
        for line in f:
            title = re.findall(r'\b(\w+رررررررررر)\b', line)
            # there will be a bug with title adab va honar
            # fix the bug in an ugly way just for now
            if title[0] == 'هنررررررررررر':
                title[0] = 'ادب و هنررررررررررر'
            if len(title) == 1:
                new_title += 1

            if new_title == 1:
                previous_title = title[0]
                corpus += line

            if new_title == 2:
                classification = Classification(corpus, self.models)
                selected_model = classification.classify()
                self.table[previous_title][selected_model] += 1
                corpus = line
                new_title = 1
                previous_title = title[0]
        f.close()

    def get_precision(self, input_class):
        true_positive = self.table[input_class][input_class]
        all_predicted = 0
        for class_name in self.models:
            all_predicted += self.table[class_name][input_class]
        precision = true_positive / all_predicted
        return precision

    def get_recall(self, input_class):
        true_positive = self.table[input_class][input_class]
        all_positive = 0
        for class_name in self.models:
            all_positive += self.table[input_class][class_name]
        recall = true_positive / all_positive
        return recall