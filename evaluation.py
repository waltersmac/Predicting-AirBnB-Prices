import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

from numpy import mean
from numpy import std

from data_pipeline import process_data


# get a list of models to evaluate
def get_models(num_features):
    models = dict()
    for i in num_features:
        models[str(i)] = RandomForestRegressor(max_features=i)
    return models
 
    
# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
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
        
    return results, names
    
    
def main():
    
    df = process_data()
    
    X = df.drop('price', axis = 1)
    y = df['price']
    
    
    # evaluate the feature models and store results
    num_features = [reound(X.shape[0]/3)]

    # get the models to evaluate
    feat_models = get_models(num_features)
    
    #print("Evaluating the feature models")
    eval_feat_models = evaluate_results(feat_models, X, y)

    file_eval_feat_models = "eval_feat_models.pkl"
    open_file = open(file_eval_feat_models, "wb")

    pickle.dump(eval_feat_models, open_file)

    open_file.close()

    # evaluate the n_trees models and store results
    #n_trees = [10, 20, 30, 40, 50]
 
    # get the models to evaluate
    #n_trees_models = get_models(n_trees)
    
    #print("evaluate the n_trees models")
    #evaluate_results(n_trees_models, X, y)
    
    
    
    # evaluate the depth models and store results
    #depths = [i for i in range(1,8)] + [None]
 
    # get the models to evaluate
    #depths_models = get_models(depths)
    
    #print("evaluate the depth models")
    #evaluate_results(depths_models, X, y)