from Evaluate import Evaluate
from Train import Train

train_corpus = Train("HAM-Train")
train_corpus.group_titles()
models = train_corpus.model_per_class()
evaluation = Evaluate("HAM-Test", models, 0.2, 0.3)
evaluation.initialize_table()
evaluation.update_table()
# all_precisions = []
# all_precisions.append(evaluation.get_precision("اقتصادرررررررررر"))
# all_precisions.append(evaluation.get_precision("اجتماعیرررررررررر"))
# all_precisions.append(evaluation.get_precision("ادب و هنررررررررررر"))
# all_precisions.append(evaluation.get_precision("سیاسیرررررررررر"))
# all_precisions.append(evaluation.get_precision("ورزشرررررررررر"))
# sum = 0
# for v in all_precisions:
#     sum += v
# print(sum/len(all_precisions))
#
# all_recals = []
# all_recals.append(evaluation.get_recall("اقتصادرررررررررر"))
# all_recals.append(evaluation.get_recall("اجتماعیرررررررررر"))
# all_recals.append(evaluation.get_recall("ادب و هنررررررررررر"))
# all_recals.append(evaluation.get_recall("سیاسیرررررررررر"))
# all_recals.append(evaluation.get_recall("ورزشرررررررررر"))
# sum = 0;
# for v in all_recals:
#     sum += v
# print(sum/len(all_recals))
preceision = evaluation.get_precision("اقتصاد")
recall = evaluation.get_recall("اقتصاد")
print("Precision of eghtesad")
print(preceision)
print("Recall of eghtesad")
print(recall)
print("f-mesaure of eghtesad")
print(evaluation.get_f_measure(preceision, recall))
print()

preceision = evaluation.get_precision("اجتماعی")
recall = evaluation.get_recall("اجتماعی")
print("Precision of ejtemaie")
print(preceision)
print("Recall of ejtemaie")
print(recall)
print("f-mesaure of ejtemaie")
print(evaluation.get_f_measure(preceision, recall))
print()

preceision = evaluation.get_precision("ادب و هنر")
recall = evaluation.get_recall("ادب و هنر")
print("Precision of adab va honar")
print(preceision)
print("Recall of adab va honar")
print(recall)
print("f-mesaure of adab va honar")
print(evaluation.get_f_measure(preceision, recall))
print()

preceision = evaluation.get_precision("سیاسی")
recall = evaluation.get_recall("سیاسی")
print("Precision of siasi")
print(preceision)
print("Recall of siasi")
print(recall)
print("f-mesaure of siasi")
print(evaluation.get_f_measure(preceision, recall))
print()

preceision = evaluation.get_precision("ورزش")
recall = evaluation.get_recall("ورزش")
print("Precision of varzeshi")
print(preceision)
print("Recall of varzeshi")
print(recall)
print("f-mesaure of varzeshi")
print(evaluation.get_f_measure(preceision, recall))
