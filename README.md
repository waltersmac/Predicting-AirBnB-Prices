# Predicting London AirBnB Prices

<kbd> <img src="reports/figures/London.jpg" alt="drawing"/> </kbd>

**Project Objective:** In this project I explored the processing and prediction the listings from ["Inside AirBnB"](http://insideairbnb.com/get-the-data.html) for London in 2020. I want to look into various business questions that I could answer for the owners of the properties which in turn would assist Airbnb in obtaining more revenue.

## 1. Business Understanding
Link for notebook is [here](https://github.com/waltersmac/Predicting-AirBnB-Prices/blob/master/notebooks/1.0-rw-data-exploration.ipynb) <br/><br/>
Explored the listings and tried to answer the following:
  * What types of verifications are hosts using?
  * Which types of amenities are hosts using? Would they give a good review score?
  * What could possibly an acceptable price?
  * What could be the most important to the price?

## 2. Data Understanding
I explored the AirBnB listsing using the following tasks:
  * Variable Identification
  * Univariate Analysis
  * Bi-variate Analysis
  * Missing values treatment
  * Outlier treatment
  * Variable transformation
  * Variable creation

## 3. Prepared Data
The following steps were taken to find the data needed for the prediction model:
  * Manual Feature Selection
  * Feature Engineering

## 3. Predictive Model Evaluation
Link for notebook is [here](https://github.com/waltersmac/Predicting-AirBnB-Prices/blob/master/notebooks/1.0-rw-model-exploration.ipynb) <br/><br/>
The following steps were applied in order to obtain the best results using “Extreme Gradient Boosting” Regressor (XGBoost) algorithm:
  * Base Model Evaluation
  * Cross-Validation
  * GridSearchCV Evaluation
  * Plotting and find top 10 Feature Importance scores

## 4. Data Science Blog
Link to the webpage [here ](https://waltersmac.github.io/Predicting-AirBnB-Prices/) <br>
  * Communicated my findings from the business questions
  * Created a page within Github and using the "Dinky theme" built in theme


## 5. Project Organisation

    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── index.md           <- The file that the GitHub page reads from.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── reports
    │   └── figures        <- visualizations that have been created.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
          └── visualize.py


## Resources Used for This Project
  * Udacity Data Science Nanodegree: [here](https://www.udacity.com/course/data-scientist-nanodegree--nd025) <br>
  * Sklearn [here](https://scikit-learn.org/stable/)
  * XGBoost Algorithm [here](https://xgboost.readthedocs.io/en/latest/#)
  * <p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
