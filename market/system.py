# -*- coding: utf-8 -*-


def mela(X_test1):

    import numpy as np
    import pandas as pd
    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    from sklearn.compose import ColumnTransformer
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestRegressor
    import os

 #   import matplotlib.pyplot as plt

    activities = ['Hording', 'Newspaper', 'TVadd', 'Socialmedia']
    profit_pred = {}

    for actv in activities:
        actvd = actv+'.csv'
        dataset = pd.read_csv(os.path.dirname(
            os.path.realpath(__file__)) + "\\" + actvd)
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, [-1]].values

    # Encoding
        labelencoder_X = LabelEncoder()
        X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
        onehotencoder = ColumnTransformer(
            # The column numbers to be transformed (here is [0] but can be [0, 1, 3])
            [('one_hot_encoder', OneHotEncoder(), [1])],
            # Leave the rest of the columns untouched
            remainder='passthrough'
        )
        X = np.array(onehotencoder.fit_transform(X))
        X = X[:, 1:]

    # Splitting Test and train data
      #  X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.05,random_state=0)

        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X)
        X_test = sc_X.transform(X_test1)
        sc_y = StandardScaler()
        y_train = sc_y.fit_transform(y)

    # FittingRandomForestRegressor to the dataset

        regressor = RandomForestRegressor(n_estimators=200, random_state=0)
        regressor.fit(X_train, y_train.ravel())

    # Predicting a new result
        y_pred = regressor.predict(X_test)

        y_pred = sc_y.inverse_transform(y_pred)

        profit_pred.update({actv: int(y_pred)})

    Keymax = max(profit_pred, key=profit_pred.get)
    maxprofit = profit_pred[Keymax]

    return profit_pred, maxprofit
