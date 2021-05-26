#train, test, samplesub

X_trn = data.copy().drop(['PassengerId','Survived'], axis=1)
X_tst = df.copy().drop('PassengerId', axis=1)
y_trn = data.copy().Survived
y_tst = target.copy().Survived

model = XGBClassifier()

model.fit(X_trn,y_trn)

#prediction
y_pred = model.predict(X_tst)
y_prob = model.predict_proba(X_tst)
# y_score = model.decision_function(X_tst)  #SVM
mse = mean_squared_error(y_pred, y_tst)

#scoring
score = model.score(X_trn, y_trn)
accry = accuracy_score(y_tst,y_pred)
  # Accuracy makes no sense here because you're trying to predict on continuous values. Only use accuracy for categorical variables.
precs = metrics.precision_score(y_tst,y_pred)
recal = metrics.recall_score(y_tst,y_pred)
# precs, recal, _ = precision_recall_curve(y_tst, y_score)
f1scr = metrics.f1_score(y_tst,y_pred)
r2scr = metrics.r2_score(y_tst,y_pred)

rocauc = metrics.roc_auc_score(y_tst,y_pred)
auc = metrics.roc_auc_score(y_tst, y_prob[:,1])
# fpr, tpr, thresholds = metrics.roc_curve(y_tst, y_pred, pos_label=2)
fpr, tpr, thresholds = roc_curve(y_tst, y_prob[:,1])
# roc_auc_plot = metrics.auc(fpr,tpr)
auc_plot = metrics.roc_auc_score(y_tst, y_prob[:,1])

clf_report = metrics.classification_report(y_tst,y_pred)
matrix = metrics.confusion_matrix(y_tst,y_pred)
expvarscore = explained_variance_score(y_tst,y_pred)

print(f'score : {round(score,3)}')
print(f'accuracy : {round(accry,3)}')
print(f'precision : {round(precs,3)}')
print(f'recall : {round(recal,3)}')
print(f'f1 score : {round(f1scr,3)}')
print(f'r2 score : {round(r2scr,3)}')
print(f'roc auc score : {round(rocauc,3)}')
print(f'auc score : {round(auc,3)}')
print(f'classification report : \n {clf_report}')
print(f'matrix : {matrix}')
print(f'explained variand score : {round(expvarscore,3)}')

# model importance
fscore = model.get_booster().get_fscore()
print(fscore)
plot_importance(model)
