import os
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline

from data_pipeline import process_data


def load_data():
    # Process and load data
    df = process_data()

    # data varibles
    X = df.drop('price', axis = 1)
    y = df['price']

    return X, y


def build_model():
    # Scaler and model pipeline
    pipeline = Pipeline([
        ('rfr', RandomForestRegressor())
    ])

    # define parameters for GridSearchCV
    params = {
        'rfr__n_estimators': [100, 200, 300, 400, 500],
        'rfr__max_depth': [1,2,3,4,5,10,20,50,100] + [None],
        'rfr__max_features': ['auto', None, 'sqrt', 'log2', 0.7, 0.2]
    }

    # create gridsearch object and return as final model pipeline
    model_pipeline = GridSearchCV(pipeline, param_grid=params, scoring='neg_mean_squared_error', cv=3, n_jobs=-1)

    return model_pipeline


def train(X, y, model):
    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    # fit model
    model.fit(X_train, y_train)

    return model


def export_model(model, filename):
    # Export model as a pickle file
    with open(filename, 'wb') as f:
        pickle.dump(model, f)


def run_pipeline():
    # Process and load data
    X, y = load_data() # run ETL pipeline
    model = build_model()  # build model pipeline
    model = train(X, y, model)  # train model pipeline
    export_model(model, 'final_model.pickle')  # save model


if __name__ == '__main__':
    run_pipeline()  # run data pipeline
