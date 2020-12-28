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

    def dict_to_list(self):
        self = self.str.replace('{', '', regex=True).replace('}', '', regex=True).replace('\"', '', regex=True)
        self = self.str.split(',')

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





# Removing N/A
def fill_na_data(df_listings):

    # filling float or int columns with the mean value of the column
    num_vars = df_listings.select_dtypes(include=['float', 'int']).columns
    for col in num_vars:
        df_listings[col].fillna((df_listings[col].mean()), inplace=True)


    # filling the categorial columns with text
    df_listings['host_response_time'].fillna('No Response', inplace=True)
    df_listings['host_is_superhost'].fillna('f', inplace=True)
    df_listings['host_has_profile_pic'].fillna('f', inplace=True)
    df_listings['bed_type'].fillna('Unknown', inplace=True)

    return df_listings




# Dropping the columns that are not needed
def drop_columns(df_listings):

    # Dropping Columns that aren't needed
    regex_list = ['url','id','scraped','first_review','last_review']
    for i in regex_list:
        df_listings = df_listings[df_listings.columns.drop(list(df_listings.filter(regex=i)))]

    df_listings = df_listings.drop(columns=['name','summary','space','description','neighborhood_overview','notes',
                                            'transit','access','interaction','house_rules','host_name','host_about',
                                            'latitude','longitude','host_since','host_neighbourhood','street',
                                            'neighbourhood','market','host_location','city','state','zipcode',
                                            'smart_location','country_code','country','amenities', 'host_verifications'])

    # remove columns with 70% or high with missing data
    col_nulls = set(df_listings.columns[df_listings.isnull().mean()>0.70])
    df_listings = df_listings.drop(list(col_nulls), axis=1)

    return df_listings



def process_data(file_csv):

    # Read in data from CSV
    df_listings = pd.read_csv(file_csv, dtype={'listing_url': 'object',
                                                     'price': 'object',
                                                     'weekly_price': 'object',
                                                     'monthly_price': 'object',
                                                     'security_deposit': 'object',
                                                     'cleaning_fee': 'object',
                                                     'extra_people': 'object',
                                                     'license': 'object',
                                                     'jurisdiction_names': 'object',})

    # Formating the data
    float_list = ['price','security_deposit','cleaning_fee','extra_people']
    for x in float_list:
        df_listings[x] = format_data.data_float(df_listings[x])

    float_list = ['host_response_rate','host_acceptance_rate']
    for x in float_list:
        df_listings[x] = format_data.data_percentage(df_listings[x])

    df_listings['amenities'] = format_data.dict_to_list(df_listings['amenities'])


    # Removing outliers
    outliers = find_outliers(df_listings).index
    df_listings = df_listings.drop(df_listings.index[outliers]).reset_index(drop = True)


    # Preparing the data
    # Creating the 'amenities - count' column
    df_listings['amenities - count'] = [len(i) for i in df_listings['amenities']]


    # Dropping the columns that aren't needed
    df_listings = drop_columns(df_listings)


    # Removing N/A
    df_listings = fill_na_data(df_listings)


    # Removing rows that do not have a price
    df = df_listings.dropna(subset=["price"])


    # Dummy the categorical variables
    cat_vars = df.select_dtypes(include=['object']).copy().columns
    for var in  cat_vars:
        # for each cat add dummy var, drop original column
        df = pd.concat([df.drop(var, axis=1), pd.get_dummies(df[var],
                                                             prefix=var, prefix_sep='_', drop_first=True)], axis=1)


    return df
