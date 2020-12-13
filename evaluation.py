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
    
    
def run_eval(parameter_list, X, y):
    
    # get the models to evaluate
    feat_models = get_models(parameter_list)
    
    #print("Evaluating the feature models")
    eval_feat_models = evaluate_results(feat_models, X, y)
    
    return eval_feat_models


def save_file(filename, eval_models):

    open_file = open(filename, "wb")
    pickle.dump(eval_models, open_file)
    open_file.close()
    
    
def main():
    
    df = process_data()
    
    X = df.drop('price', axis = 1)
    y = df['price']
    
    # Evaluate the feature models
    num_features = [10, 20, 30]

    # Run eval for feature models
    eval_feat_models = run_eval(num_features, X, y)
    
    # Store results for feature models
    save_file("eval_feat_models.pkl", eval_feat_models)

    
    
    # evaluate the n_trees models and store results
    # n_trees = [10, 20, 30]
    
    # eval_tree_models = run_eval(n_trees, X, y)
    
    # save_file("eval_trees_models.pkl", eval_tree_models)
    
    
    
    
    # evaluate the depth models and store results
    # depths = [i for i in range(1,8)] + [None]
 
    #
    # eval_depth_models = run_eval(depths, X, y)
    
    #
    # save_file("eval_depth_models.pkl", eval_depth_models)