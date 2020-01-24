import sys


class Classification:
    def __init__(self, corpus, models):
        self.models = models
        self.corpus = corpus

    def classify(self):
        max_priority = -1
        selected_model = ""
        for model in self.models:
            priority = self.backoff(self.models[model])
            if priority > max_priority:
                max_priority = priority
                selected_model = model
        return selected_model

    def backoff(self, model):
        unigram_priorities = model[0]
        bigram_priorities = model[1]
        all_words = self.corpus.split()
        all_bi_words = list(map(' '.join, zip(all_words[:-1], all_words[1:])))
        landa2 = 0.3
        landa = 0.2
        model_priority = 1
        for i in range(len(all_bi_words)):
            bigram_priority = 0
            unigram_priority = 0
            if all_bi_words[i] in bigram_priorities:
                bigram_priority = bigram_priorities[all_bi_words[i]]
            if all_words[i] in unigram_priorities:
                unigram_priority = unigram_priorities[all_words[i]]
            priority = landa2 * bigram_priority + landa * unigram_priority
            # I never ever wanna have priority 0 so if this happens I'm
            # will plus the smallest number possible with it
            if priority == 0:
                priority = sys.float_info.min
            model_priority *= priority
        return model_priority

