import math
import sys


class Classification:
    def __init__(self, corpus, models):
        self.models = models
        self.corpus = corpus
        self.classes = models.keys()

    def classify(self, unigram_factor, bigram_factor):
        max_priority = -100000000
        selected_model = ""
        for model in self.classes:
            priority = self.backoff(self.models[model], unigram_factor, bigram_factor)
            if priority > max_priority:
                max_priority = priority
                selected_model = model
        return selected_model

    def backoff(self, model, unigram_factor, bigram_factor):
        unigram_priorities = model[0]
        bigram_priorities = model[1]
        all_words = self.corpus.split()
        all_bi_words = list(map(' '.join, zip(all_words[:-1], all_words[1:])))
        model_priority_log = 0
        for i in range(len(all_bi_words)):
            bigram_priority = 0
            unigram_priority = 0
            if all_bi_words[i] in bigram_priorities.keys():
                bigram_priority = bigram_priorities[all_bi_words[i]]
            if all_words[i+1] in unigram_priorities.keys():
                unigram_priority = unigram_priorities[all_words[i+1]]
            priority = bigram_factor * bigram_priority + unigram_factor * unigram_priority
            # I never ever wanna have priority 0 so if this happens I'm
            # will plus the smallest number possible with it
            if priority == 0:
                priority = sys.float_info.min
            priority_log = math.log2(priority)
            model_priority_log += priority_log
        return model_priority_log

