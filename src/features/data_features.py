import os
import sys
import pickle
import numpy as np
import pandas as pd


# function for removing unwanted columns
def drop_columns(df):

    # Dropping Columns that aren't needed
    regex_list = ['url','scrape','first_review','last_review','cancellation_policy','requires']
    for i in regex_list:
        df = df[df.columns.drop(list(df.filter(regex=i)))]

    df = df.drop(columns=['id','name','description','neighborhood_overview','latitude',
                          'longitude','neighbourhood','calendar_updated','host_id', 'host_name',
                          'host_since', 'host_location', 'host_about','host_response_time',
                          'host_response_rate', 'host_acceptance_rate',
                          'host_neighbourhood', 'host_listings_count',
                          'host_has_profile_pic', 'host_identity_verified',
                          'minimum_minimum_nights', 'maximum_nights_avg_ntm',
                          'maximum_minimum_nights', 'minimum_maximum_nights',
                          'maximum_maximum_nights', 'minimum_nights_avg_ntm'])

    # remove columns with 70% or high with missing data
    col_nulls = set(df.columns[df.isnull().mean()>0.70])
    df = df.drop(list(col_nulls), axis=1)

    return df


# Function for creating 1D series
def to_1D(series):
    return pd.Series([x for _list in series for x in _list])


# Function for creating one-hot encoding
def onehot_df(df, variable, unique_items):

    item_lists = df[variable]

    # Loop through all the labels
    for i, label in enumerate(unique_items):

        # Creating new column for each label
        df[variable+'_'+label] = item_lists.apply(lambda x: 1 if label in x else 0)

    # Removing old column
    del df[variable]

    # Return the results as a dataframe
    return df


def process_data(file_pickle):

    # Read in the file to dataframe
    df_listings = pd.read_pickle(file_pickle)

    # Removing unwanted columns from the dataframe
    df_listings = drop_columns(df_listings)

    df_listings.rename(columns={'bathrooms_text': 'bathrooms_shared'}, inplace=True)

    # Amenities expansion to label encoding
    df_listings["amenities"] = df_listings["amenities"].apply(eval)

    # host_verifications expansion to label encoding
    df_listings["host_verifications"] = df_listings["host_verifications"].apply(eval)

    # Creating new columns
    df_listings['amenities_len'] = df_listings['amenities'].str.len()
    df_listings['verifications_len'] = df_listings['host_verifications'].str.len()

    del df_listings['host_verifications']

    # Creating new property type column
    df_listings["property_type"] = df_listings["property_type"].str.split().str[-1]

    # creating 1D series for amenities
    df_amenities_top_10 = pd.DataFrame(to_1D(df_listings["amenities"]).value_counts().head(50)).index

    # creating 1D series for property_type
    df_new_property_top_10 = pd.DataFrame(df_listings["property_type"].value_counts().head(20)).index

    # Implementing one-hot encoding for the amenities
    onehot_df(df_listings,"amenities", df_amenities_top_10)

    # Implementing one-hot encoding for the property types
    onehot_df(df_listings,"property_type", list(df_new_property_top_10))

    # Removing any rows with NaN values
    df_listings = df_listings.dropna()

    # Removing rows that do not have a price
    df_listings = df_listings[df_listings['price'] != 0]

    return df_listings
