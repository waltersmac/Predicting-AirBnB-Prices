import os
import numpy as np
import pandas as pd


# Formating the data
class format_data:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def data_float(self):
        self = self.str.replace('$', '', regex=True).replace(',', '', regex=True).astype(float)

        return self

    def data_percentage(self):
        self = (self.str.replace('%', '', regex=True).astype('float')) / 100

        return self

    def text_to_int(self):
        self = self.str.split(' ').str[0].replace('Half-bath', '0.5', regex=True).replace('Shared', '0.5', regex=True) \
                                         .replace('Private', '1', regex=True).astype('float')

        return self



def find_outliers(df_listings):
    # Calculate Q1 (25th percentile of the data) for the given feature
    Q1 = np.percentile(df_listings["price"], 25)

    #Calculate Q3 (75th percentile of the data) for the given feature
    Q3 = np.percentile(df_listings["price"],75)

    # Use the interquartile range to calculate an outlier step (1.5 times the interquartile range)
    step = (Q3 - Q1) * 1.5

    # Display the outliers
    #print("Data points considered outliers for the feature '{}':".format("price"))
    filtered_data = df_listings[~((df_listings["price"] >= Q1 - step) &
                                  (df_listings["price"] <= Q3 + step))].sort_values(by=["price"])

    #filtered_data["price"].hist()
    #outliers = filtered_data[filtered_data["price"] >= 1000.00]

    return filtered_data



def process_data(file_csv):

    # Read in data from CSV
    df_listings = pd.read_csv(file_csv, low_memory=False)

    # Formating the data
    # Applying format to the price column
    float_list = ['price']
    for x in float_list:
        df_listings[x] = format_data.data_float(df_listings[x])

    # Applying format to the host_response_rate and host_acceptance_rate column
    percentage_list = ['host_response_rate','host_acceptance_rate']
    for x in percentage_list:
        df_listings[x] = format_data.data_percentage(df_listings[x])

    # Applying format to the bathrooms_text column
    text_list = ['bathrooms_text']
    for x in text_list:
        df_listings[x] = format_data.text_to_int(df_listings[x])


    # Removing outliers
    outliers = find_outliers(df_listings).index
    df_listings = df_listings.drop(df_listings.index[outliers]).reset_index(drop = True)


    return df_listings
