import pandas as pd
import re

## Load the lap times data
laps = pd.read_csv('Data/laps.csv', sep = ';')
## Load the car specs data
cars = pd.read_csv('Data/Sport car price (1).csv')

## Cleaning the data
## Deleting the 'Unnamed: 0', 'Length[a]' and 'Notes' column
laps = laps.drop('Unnamed: 0', axis = 1)
laps = laps.drop('Length[a]', axis = 1)
laps = laps.drop('Notes', axis = 1)

## Renaming the columns for better readability
cars = cars.rename(columns = {'Horsepower': 'HP',
                            '0-60 MPH Time (seconds)': '0-100',
                            'Price (in USD)': 'Price (EUR)',
                            'Torque (lb-ft)': 'Torque (Nm)'})


## Removing the commas from the 'Price (EUR)' column and converting it to float
cars['Price (EUR)'] = (
    cars['Price (EUR)'].str.replace(',', '', regex = True).astype(float)
)

## Removing the commas from the 'Torque (Nm)' column and converting it to float
cars['Torque (Nm)'] = pd.to_numeric(cars['Torque (Nm)'], errors = 'coerce'
)

## Converting lb-ft to Nm and USD to EUR
cars['Torque (Nm)'] = cars['Torque (Nm)'] * 1.35582

cars['Price (EUR)'] = cars['Price (EUR)'] * 0.85


## Creating a new column 'Vehicle' by combining the 'Car Make' and 'Car Model' columns
cars['Vehicle'] = cars['Car Make'] + ' ' + cars['Car Model']

## Deleting the 'Car Make' and 'Car Model' columns
cars = cars.drop('Car Make', axis = 1)
cars = cars.drop('Car Model', axis = 1)


## Cleaning the 'Vehicle' column in both dataframes for better merging
def clean_vehicle_name(x):
    x = str(x).lower()
    x = re.sub(r"\(.*?\)", "", x)
    x = re.sub(r"\b\d{4}\b", "", x)
    x = re.sub(r"\b\d+\s?ps\b", "", x)
    x = x.replace("coupé", "coupe")
    x = re.sub(r"[^a-z0-9 ]", " ", x)
    x = re.sub(r"\s+", " ", x).strip()
    return x

## Applying the cleaning function to the 'Vehicle' column in both dataframes
laps["Vehicle_clean"] = laps["Vehicle"].apply(clean_vehicle_name)
cars["Vehicle_clean"] = cars["Vehicle"].apply(clean_vehicle_name)

## Removing duplicates from both dataframes based on the 'Vehicle_clean' column
laps = laps.drop_duplicates(subset = "Vehicle_clean", keep = "first")
cars = cars.drop_duplicates(subset = "Vehicle_clean", keep= "first")

## Merging the two dataframes on the 'Vehicle_clean' column
nls = laps.merge(
    cars,
    on = "Vehicle_clean",
    how = "inner",
    suffixes = ("_lap", "_car")
)