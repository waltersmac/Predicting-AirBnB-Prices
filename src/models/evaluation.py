import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from numpy import mean
from numpy import std

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

from data_pipeline import process_data


# get a list of models to evaluate
def get_models(num_list, hyperparameter):

    models = dict()

    if hyperparameter == 'max_features':
        for i in num_list:
            models[str(i)] = RandomForestRegressor(max_features=i)
    elif hyperparameter == 'n_estimators':
        for i in num_list:
            models[str(i)] = RandomForestRegressor(n_estimators=i)
    elif hyperparameter == 'max_depth':
            for i in num_list:
                models[str(i)] = RandomForestRegressor(max_depth=i)

    return models


# evaluate a given model using cross-validation
def evaluate_model(model, X_train, X_test, y_train, y_test):
    # evaluate the model and collect the results
    scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=10, n_jobs=-1)
    model_rmse_scores = np.sqrt(-scores)
    return model_rmse_scores


def evaluate_results(models, X, y):
    # evaluate the models and store results
    results, names = list(), list()
    for name, model in models.items():
        # evaluate the model
        rmse_scores = evaluate_model(model, X, y)
        # store the results
        results.append(rmse_scores)
        names.append(name)
        # summarize the performance along the way
        #print('>%s %.3f (%.3f)' % (name, mean(rmse_scores), std(rmse_scores)))



    results, results2 = list(), list()
    for name, model in models.items():
        # evaluate the model
        rmse_scores = evaluate_model(model, X, y)
        # store the results
        results.append(rmse_scores)
        names.append(name)
        # summarize the performance along the way
        #print('>%s %.3f (%.3f)' % (name, mean(rmse_scores), std(rmse_scores)))


    for depth in max_depth_size:

        model = RandomForestClassifier(depth, oob_score=True, n_jobs=-1, random_state=44)

        #model.fit(X, y)
        model.fit(X_train, y_train)

        pred = model.predict(X_train)
        pred2 = model.predict(X_test)

        roc1 = roc_auc_score(y_train, pred)
        roc2 = roc_auc_score(y_test, pred2)

        results.append(roc1)
        results2.append(roc2)


    return results, names


def run_eval(parameter_list, hyperparameter, X_train, X_test, y_train, y_test):

    # get the models to evaluate
    feat_models = get_models(parameter_list, hyperparameter)

    #print("Evaluating the feature models")
    eval_feat_models = evaluate_results(feat_models, X_train, X_test, y_train, y_test)

    return eval_feat_models


def save_file(filename, results):
    # Create the results file inside the directory
    with open(filename, 'wb') as f:
        pickle.dump(results, f)


def rf_eval():

    # Process and load data
    df = process_data()

    # data varibles
    X = df.drop('price', axis = 1)
    y = df['price']

    #split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)


    # Store results for feature models
    # Create the directory if not exists
    if not os.path.exists('Evaluation-results'):
        os.makedirs('Evaluation-results')


    # Evaluate the feature models
    # num_features = ["auto", None, "sqrt", "log2", 0.7, 0.2]

    # Run eval for feature models
    # eval_feat_models = run_eval(num_features, 'max_features', X, y)

    # Create the results file inside the directory
    # save_file('Evaluation-results/eval_feat_models.pickle', eval_feat_models)


    # evaluate the n_trees models and store results
    # n_trees = [100, 200, 300, 400, 500]

    # eval_tree_models = run_eval(n_trees, 'n_estimators', X, y)

    # Create the results file inside the directory
    # save_file('Evaluation-results/eval_tree_models.pickle', eval_tree_models)


    # evaluate the depth models and store results
    depths = [1,2,3,4,5,10,20,50,100] + [None]

    eval_depth_models = run_eval(depths, 'max_depth', X_train, X_test, y_train, y_test)

    # Create the results file inside the directory
    save_file('Evaluation-results/eval_depth_models.pickle', eval_depth_models)



if __name__ == "__main__":
    rf_eval()
