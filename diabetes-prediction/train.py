import pandas as pd

df = pd.read_csv('diabetes.csv')
# print(df.shape)
# print(df.head())
# print(df.Outcome.value_counts())
# print(df.info())
input_columns = [column for column in df.columns if column != "Outcome"]
# print(input_columns)
output_colmun = "Outcome"
print(output_colmun)

X = df.loc[:, input_columns].values
y = df.loc[:, output_colmun]
# print(X.shape, Y.shape)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=555, stratify=y)

# print(np.sum(y_train))
# print(np.sum(y_test))

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression(class_weight='balanced', max_iter=1000).fit(X_train, y_train)
# print(logreg.score(X_test, y_test))

predictions = logreg.predict(X_test)

# print(classification_report(y_test, predictions, target_names=["Non Outcome", "Outcome"]))

import pickle

pickle_out = open("logreg.pkl", "wb")
pickle.dump(logreg, pickle_out)
pickle_out.close()

