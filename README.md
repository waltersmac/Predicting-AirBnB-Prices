# Predicting London AirBnB Prices

<kbd> <img src="reports/figures/London.jpg" alt="drawing"/> </kbd>

**Project Objective:** In this project I explored the processing and prediction the listings from ["Inside AirBnB"](http://insideairbnb.com/get-the-data.html) for London in 2020. I want to look into various business questions that I could answer for the owners of the properties which in turn would assist Airbnb in obtaining more revenue.

## 1. Exploratory Data Analysis
Refer to the following data exploration notebook [here](https://github.com/waltersmac/AirBnB-London-2020/blob/master/notebooks/1.0-rw-data-exploration.ipynb)
  * Variable Identification
  * Univariate Analysis
  * Bi-variate Analysis
  * Missing values treatment
  * Outlier treatment
  * Variable transformation
  * Variable creation

## 2. Business Questions
Refer to the following business questions notebook [here](https://github.com/waltersmac/AirBnB-London-2020/blob/master/notebooks/1.0-rw-business-questions.ipynb) <br>
Explored the listings and tried to answer the following:
  * What types of verifications are hosts using?
  * Which types of amenities are hosts using? Would they give a good review score?
  * What could possibly an acceptable price?
  * What could be the most important to the price?

## 3. Predictive Model Evaluation
Refer to the following Model Evaluation notebook [here](https://github.com/waltersmac/AirBnB-London-2020/blob/master/notebooks/1.0-rw-model-exploration.ipynbM) <br>
The following steps were applied in order to obtain the best results using “Extreme Gradient Boosting” Regressor (XGBoost) algorithm:
  * Manual Feature Selection
  * Feature Engineering
  * Base Model Evaluation
  * Cross-Validation
  * GridSearchCV
  * Feature Importance

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
