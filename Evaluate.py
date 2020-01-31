from Classification import Classification


class Evaluate:
    def __init__(self, test_corpus, models, unigram_factor, bigram_factor):
        self.test_file_name = test_corpus + ".txt"
        self.models = models
        self.classes = models.keys()
        self.table = {}
        self.unigram_factor = unigram_factor
        self.bigram_factor = bigram_factor

    def initialize_table(self):
        for actual in self.classes:
            predicted_dict = {}
            for predicted in self.classes:
                predicted_dict[predicted] = 0
            self.table[actual] = predicted_dict

    def update_table(self):
        f = open(self.test_file_name, mode="r", encoding='utf-8-sig')
        test_corpuses = f.read().split('\n')
        f.close()
        for test_corpus in test_corpuses:
            title, data = test_corpus.split("@@@@@@@@@@ ")
            classification = Classification(data, self.models)
            selected_model = classification.classify(self.unigram_factor, self.bigram_factor)
            self.table[title][selected_model] += 1

    def get_precision(self, input_class):
        true_positive = self.table[input_class][input_class]
        all_predicted = 0
        for class_name in self.models.keys():
            all_predicted += self.table[class_name][input_class]
        precision = true_positive / all_predicted
        return precision

    def get_recall(self, input_class):
        true_positive = self.table[input_class][input_class]
        all_positive = 0
        for class_name in self.models.keys():
            all_positive += self.table[input_class][class_name]
        recall = true_positive / all_positive
        return recall

    def get_f_measure(self, precision, recall):
        return 2 * precision * recall / (precision + recall)