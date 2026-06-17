import pandas as pd
import re
from rapidfuzz import process, fuzz

## Load the lap times data
laps = pd.read_csv('Data/laps.csv', sep = ';')
## Load the car specs data
cars = pd.read_csv('Data/Sport car price (1).csv')

## Cleaning the data
## Deleting the 'Unnamed: 0', 'Length[a]' and 'Notes' column
laps = laps.drop(columns = ['Unnamed: 0', 'Length[a]', 'Notes'], errors = 'ignore')

## Renaming the columns for better readability
cars = cars.rename(columns = {'Horsepower': 'HP',
                            '0-60 MPH Time (seconds)': '0-100',
                            'Price (in USD)': 'Price_eur',
                            'Torque (lb-ft)': 'Torque_nm'})


## Removing the commas from the 'Price (EUR)' column and converting it to float
cars['Price_eur'] = (
    cars['Price_eur'].str.replace(',', '', regex = False).astype(float)
)

## Removing the commas from the 'Torque (Nm)' column and converting it to float
cars['Torque_nm'] = pd.to_numeric(cars['Torque_nm'], errors = 'coerce'
)

## Converting "HP", "0-100", "Engine Size (L)" columns to numeric, coercing errors to NaN
cars['HP'] = pd.to_numeric(cars['HP'], errors = 'coerce')
cars['0-100'] = pd.to_numeric(cars['0-100'], errors = 'coerce')
cars['Engine Size (L)'] = pd.to_numeric(cars['Engine Size (L)'], errors = 'coerce')

## Converting lb-ft to Nm and USD to EUR
cars['Torque_nm'] = cars['Torque_nm'] * 1.35582

cars['Price_eur'] = cars['Price_eur'] * 0.85


## Creating a new column 'Vehicle' by combining the 'Car Make' and 'Car Model' columns
cars['Vehicle'] = cars['Car Make'] + ' ' + cars['Car Model']

## Deleting the 'Car Make' and 'Car Model' columns
cars = cars.drop(columns = ['Car Make', 'Car Model'])

## Cleaning the 'Vehicle' column in both dataframes for better merging
def clean_vehicle_name(x):
    x = str(x).lower() ## Convert to lowercase
    x = re.sub(r"\(.*?\)", "", x) ## Remove text within parentheses
    x = re.sub(r"\b\d{4}\b", "", x) ## Remove 4-digit numbers (years)
    x = re.sub(r"\b\d+\s?ps\b", "", x) ## Remove horsepower specifications
    x = x.replace("coupé", "coupe") ## Replace 'coupé' with 'coupe'
    x = re.sub(r"[^a-z0-9 ]", " ", x) ## Remove special characters
    x = re.sub(r"\s+", " ", x).strip() ## Remove extra whitespace
    return x

## Applying the cleaning function to the 'Vehicle' column in both dataframes
laps["Vehicle_clean"] = laps["Vehicle"].apply(clean_vehicle_name)
cars["Vehicle_clean"] = cars["Vehicle"].apply(clean_vehicle_name)

## Removing duplicates from both dataframes based on the 'Vehicle_clean' column
cars = cars.drop_duplicates(subset = "Vehicle_clean", keep= "first")


car_names = cars["Vehicle_clean"].unique()
## Function to perform fuzzy matching and return the best match if the score is above a certain threshold
def fuzzy_match(name):
    result = process.extractOne(
        name,
        car_names,
        scorer = fuzz.token_sort_ratio
    )

    if result and result[1] >= 80:
        return result[0]
    return None

## Applying the fuzzy matching function to the 'Vehicle_clean' column in the laps dataframe
laps["Vehicle_match"] = laps["Vehicle_clean"].apply(fuzzy_match)

## Merging the two dataframes on the 'Vehicle_clean' column
nls = laps.merge(
    cars,
    left_on = "Vehicle_match",
    right_on = "Vehicle_clean",
    how = "inner"
)

## Renaming the 'Vehicle_x' column to 'Vehicle'
nls = nls.rename(columns={"Vehicle_x": "Vehicle"})

## Deleting the unnecessary columns
nls = nls.drop(columns=[
    "Vehicle_y",
    "Vehicle_clean_x",
    "Vehicle_clean_y",
    "Vehicle_match"
])