from diabetesoop.data.load import Data
from diabetesoop.processing.prep import DropNaNs, FillNaNs
from diabetesoop.processing.transformer import Dummifier, Binarizer
from diabetesoop.modeling.model import Model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

X_FEATURES = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis', 'M/F']
Y_FEATURE = 'diabetes_mellitus'

data = Data()
X_y_train, X_y_test = data.from_csv('data/sample_diabetes_mellitus_data.csv', Y_FEATURE)

print('X_y_train>>', X_y_train)
print('X_y_test>>', X_y_test)

X_y_train = DropNaNs(X_y_train, ['age', 'gender', 'ethnicity']).drop()
X_y_test = DropNaNs(X_y_test, ['age', 'gender', 'ethnicity']).drop()

print('X_y_train>>', X_y_train)
print('X_y_test>>', X_y_test)

print('X_y_train nans before filling>>>\n', X_y_train.isna().sum().T[['height', 'weight']])
print('X_y_test nans before filling>>>\n', X_y_test.isna().sum().T[['height', 'weight']])

X_y_train = FillNaNs(X_y_train, ['height', 'weight']).fill()
X_y_test = FillNaNs(X_y_test, ['height', 'weight']).fill()

print('X_y_train nans after filling>>>\n', X_y_train.isna().sum().T[['height', 'weight']])
print('X_y_test nans after filling>>>\n', X_y_test.isna().sum().T[['height', 'weight']])

# dummify ethnicity
X_y_train = Dummifier(X_y_train, ['ethnicity']).generate()
X_y_test = Dummifier(X_y_test, ['ethnicity']).generate()

print('X_y_train>>', X_y_train.info())
print('X_y_test>>', X_y_test.info())

# binarize gender
X_y_train = Binarizer(X_y_train, 'gender', 'M/F').generate()
X_y_test = Binarizer(X_y_test, 'gender', 'M/F').generate()

print('X_y_train>>', X_y_train.info())
print('X_y_test>>', X_y_test.info())

# model_ = Model(feature_columns=X_FEATURES, target_column=Y_FEATURE, model=LogisticRegression, hyperparamaterers={'penalty': 'ads', 'solver': 'saga'})
model_ = Model(feature_columns=X_FEATURES, target_column=Y_FEATURE, model=RandomForestClassifier, hyperparamaterers={'n_estimators': 1000, 'criterion': 'gini'})

model_.train(X_y_train)
preds = model_.predict(X_y_test)
print('preds>>', preds)