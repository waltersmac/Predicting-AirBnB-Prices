import os
import sys
import pickle
import numpy as np
import pandas as pd


import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


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

    xgb1 = xgb.XGBRegressor()

    # define parameters for GridSearchCV
    parameters = {'nthread':[4],
                  'objective':['reg:squarederror'],
                  'learning_rate': [.03, 0.05, .07],
                  'max_depth': [7, 8, 9],
                  'min_child_weight': [4],
                  'silent': [1],
                  'subsample': [0.7],
                  'colsample_bytree': [0.7],
                  'n_estimators': [500]}

    # create gridsearch object and return as final model pipeline
    xgb_grid = GridSearchCV(xgb1,
                        parameters,
                        cv = 5,
                        n_jobs = 5,
                        verbose=True)


    return xgb_grid


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
