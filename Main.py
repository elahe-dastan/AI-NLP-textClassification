from Evaluate import Evaluate
from Train import Train

train_corpus = Train("HAM-Train")
train_corpus.group_titles()
models = train_corpus.model_per_class()
evaluation = Evaluate("HAM-Test", models)
evaluation.initialize_table()
evaluation.update_table()
print(evaluation.get_precision("اقتصادرررررررررر"))
print(evaluation.get_recall("سیاسیرررررررررر"))
