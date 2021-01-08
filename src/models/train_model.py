import os
import pickle
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline

from src.data.data_pipeline import process_data


def load_data(df):
    # Process and load data

    # Extract features and labels
    features = df.drop('price', axis = 1)
    labels = df['price']

    # Convert to numpy arrays
    features = np.array(features)
    labels = np.array(labels)

    return features, labels


def build_model():
    # Scaler and model pipeline
    pipeline = Pipeline([
        ('rfr', RandomForestRegressor())
    ])

    # define parameters for GridSearchCV
    params = {
        'rfr__n_estimators': [1000],
        'rfr__max_depth': [1,2,3,4,5,10,20,50,100] + [None],
        'rfr__max_features': ['auto', None, 'sqrt', 'log2', 0.7, 0.2]
    }

    # create gridsearch object and return as final model pipeline
    model_pipeline = GridSearchCV(pipeline, param_grid=params, scoring='neg_mean_squared_error', cv=10, n_jobs=-1, random_state=42)

    return model_pipeline


def train(features, labels, model):
    # train test split
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state=42)

    # fit model
    model.fit(features_train, labels_train)

    return model


def export_model(model, filename):
    # Export model as a pickle file
    with open(filename, 'wb') as f:
        pickle.dump(model, f)


def run_pipeline(df_csv, output_location):
    # Process and load data
    features, labels = load_data(df_csv) # run ETL pipeline
    model = build_model()  # build model pipeline
    model = train(features, labels, model)  # train model pipeline
    export_model(model, output_location + 'final_model.pickle')  # save model
