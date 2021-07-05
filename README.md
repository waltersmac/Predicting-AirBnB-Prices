# Predicting London AirBnB Prices

**Project Objective:** In this project I explored the processing and prediction the listings from ["Inside AirBnB"](http://insideairbnb.com/get-the-data.html) for London in 2020. I want to look into various business questions that I could answer for the owners of the properties which in turn would assist Airbnb in obtaining more revenue.

As AirBnB has become increasingly popular, I wanted to investigate the underlying data around the listings of the different properties within London and try to answer certain questions that could benefit both AirBnB and potential owners. I decided to look at the investigation from a certain point of view, I wanted to see if there was anything that could help the property owners in deciding whether to list their property and what could help in getting the best possible price, this would certainly help both the landlord and AirBnB. I wanted to select the most recent listings within 2020, even with the current situation facing London.

## 1. Business Understanding
Link for notebook is [here](https://github.com/waltersmac/Predicting-AirBnB-Prices/blob/master/notebooks/1.0-rw-data-exploration.ipynb) <br/>

I explored the data and tried to answer the following questions:
  * What types of verifications are hosts using?
  * Which types of amenities are hosts using? Would they give a good review score?
  * What could possibly an acceptable price?
  * Can the nightly price be predicted? Which features could be most important to the price?

## 2. Data Understanding
Link for notebook is [here](https://github.com/waltersmac/Predicting-AirBnB-Prices/blob/master/notebooks/1.0-rw-data-exploration.ipynb) <br/>
I explored the AirBnB listsing using the following tasks:
  * Variable Identification
  * Univariate Analysis
  * Bi-variate Analysis
  * Missing values treatment
  * Outlier treatment
  * Variable transformation
  * Variable creation

## 3. Prepared Data
Link for notebook is [here](https://github.com/waltersmac/Predicting-AirBnB-Prices/blob/master/notebooks/1.0-rw-model-exploration.ipynb) <br/>
The following steps were taken to find the data needed for the prediction model:
  * Manual Feature Selection
  * Feature Engineering
  * Data Pipeline

## 3. Predictive Model Evaluation
Link for notebook is [here](https://github.com/waltersmac/Predicting-AirBnB-Prices/blob/master/notebooks/1.0-rw-model-exploration.ipynb) <br/>
The following steps were applied in order to obtain the best results using “Extreme Gradient Boosting” Regressor (XGBoost) algorithm:
  * Base Model Evaluation
  * Cross-Validation
  * GridSearchCV Evaluation
  * Plotting and find top 10 Feature Importance scores

## 4. Conclusion
## **What types of verifications are hosts using?**
Looking at the security verifications I want to see what the different types were and how many were associated with the listings. The data seems to show that phone calls, emails and "government id" were in the top 3. About 70% of the listings had a "government id" as one of the verifications and in my mind that would be suitable, especially if you're letting someone into your property that you do not know.

<kbd> <img src="https://raw.githubusercontent.com/waltersmac/Predicting-AirBnB-Prices/master/reports/figures/Verification_type_price_histogram_plots.png" alt="drawing"/> </kbd>

## **Which types of amenities are hosts using? Would they give a good review score?**
Now with amenities these are the items that you would hope would make a guest enjoy their stay and in turn give you an outstanding review. The table below shows the amenities by the number of listings with the calculated minimum, maximum and average review value. The top 20 amenities seem to show that luxuries certainly do help with the average review and having the option for allowing pets i.e. dogs also helps.

<kbd> <img src="https://raw.githubusercontent.com/waltersmac/Predicting-AirBnB-Prices/master/reports/figures/top_amenities.png" alt="drawing" height = 500 width="500"/> </kbd>

## **What could possibly be an acceptable price?**
My first thoughts with the price was to look at the data from a view of the London boroughs. Was there any areas within London that were the most expensive? or was there an even spread of the prices.

When initially viewing the London map, it shows that the majority of the prices that range from £111 to £223 are within the central/west, which would presume that the borough of Westminster would be one of the most expensive. The lower prices are evenly spread throughout London which would confirm that these properties would be more affordable.   

<kbd> <img src="https://raw.githubusercontent.com/waltersmac/Predicting-AirBnB-Prices/master/reports/figures/availability_365_prices_scatterplot.png" alt="drawing"/> </kbd>

The average price for the different boroughs shows that the City of London, Kensington and Chelsea, and also Westminster are the top 3 boroughs with the largest average price.

<kbd> <img src="https://raw.githubusercontent.com/waltersmac/Predicting-AirBnB-Prices/master/reports/figures/Neighbourhood_av_price_histogram_plots.png" alt="drawing"/> </kbd>


## **What could be the most important to the price?**
With my final investigation I wanted to see if I could predict the price of a listing for a night, what would be the minimal difference between the actual price and the prediction? What would be the features of importance that could have an impact and could this help the potential landlords?

I found that with my prediction model, I could predict prices with plus or minus £30 difference from the actual price. When I investigated the features of the results, I found that the property type and area certainly had an effect on the price, and this would confirm that my previous investigation of the average price for each borough was correct.

## **Review**
Looking at the results of the different questions that I wanted to ask, I found that the area of London that you could advertise would certainly have an effect on the price for the property. The property type and amenities would certainly have some kind of effect as well. I think to make a listing stand out from the crowd I would make sure to look into these features.


## 6. Project Organisation

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
