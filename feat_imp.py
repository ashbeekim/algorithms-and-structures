#liner
#from sklearn.linear_model import LinearRegression
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
model = LinearRegression()
# fit the model
model.fit(X, y)
# get importance
imp = model.coef_
# summarize feature importance
for i,v in enumerate(imp):
    print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(imp))], imp)
plt.show()

#logistic
#from sklearn.linear_model import LogisticRegression
# define dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=1)
# define the model
model = LogisticRegression()
# fit the model
model.fit(X, y)
# get importance
imp = model.coef_[0]
# summarize feature importance
for i,v in enumerate(imp):
    print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(imp))], imp)
plt.show()

#DecisionTree
#from sklearn.tree import DecisionTreeRegressor
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
model = DecisionTreeRegressor()
# fit the model
model.fit(X, y)
# get importance
imp = model.feature_importances_
# summarize feature importance
for i,v in enumerate(imp):
    print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(imp))], imp)
plt.show()

#RandomForest
#from sklearn.ensemble import RandomForestRegressor
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
model = RandomForestRegressor()
# fit the model
model.fit(X, y)
# get importance
imp = model.feature_importances_
# summarize feature importance
for i,v in enumerate(imp):
    print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(imp))], imp)
plt.show()

#XGBoost
#from xgboost import XGBRegressor
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
model = XGBRegressor()
# fit the model
model.fit(X, y)
# get importance
imp = model.feature_importances_
# summarize feature importance
for i,v in enumerate(imp):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(imp))], imp)
plt.show()

#Permutation
#from sklearn.neighbors import KNeighborsRegressor
#from sklearn.inspection import permutation_importance
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
model = KNeighborsRegressor()
# fit the model
model.fit(X, y)
# perform permutation importance
results = permutation_importance(model, X, y, scoring='neg_mean_squared_error')
# get importance
imp = results.importances_mean
# summarize feature importance
for i,v in enumerate(imp):
	print('Feature: %0d, Score: %.5f' % (i,v))
# plot feature importance
plt.bar([x for x in range(len(imp))], imp)
plt.show()

#Feature Selection
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
 
# feature selection
def select_features(X_train, y_train, X_test, n_est=42):
    # configure to select a subset of features
    feat_s = SelectFromModel(RandomForestClassifier(n_estimators=n_est), max_features=5)
    # learn relationship from training data
    feat_s.fit(X_train, y_train)
    # transform train input data
    X_trn_fs = feat_s.transform(X_train)
    # transform test input data
    X_tst_fs = feat_s.transform(X_test)
    return X_trn_fs, X_tst_fs, feat_s

# define the dataset
X, y = make_classification(n_samples=1000, n_features=10, n_informative=5, n_redundant=5, random_state=1)
# split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=1)
# feature selection
X_trn_fs, X_tst_fs, feat_s = select_features(X_train, y_train, X_test)
# fit the model
model = LogisticRegression(solver='liblinear')
model.fit(X_trn_fs, y_train)
# evaluate the model
yhat = model.predict(X_test_fs)
# evaluate predictions
accuracy = accuracy_score(y_test, yhat)
print('Accuracy: %.2f' % (accuracy*100))

# [cf link_feature importance] https://machinelearningmastery.com/calculate-feature-importance-with-python/

# # lightgbm.plot_importance
# # https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.plot_importance.html
    
# # https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html

# #Permutation Feature Importance
# # https://scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html

# #xgboost
# # https://machinelearningmastery.com/feature-importance-and-feature-selection-with-xgboost-in-python/

# feature_names = [f'feature {i}' for i in range(X.shape[1])]
# forest = RandomForestClassifier(random_state=0)
# forest.fit(X_train, y_train)
