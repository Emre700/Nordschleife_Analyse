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
                            'Price (in USD)': 'Price (EUR)',
                            'Torque (lb-ft)': 'Torque (Nm)'})


## Removing the commas from the 'Price (EUR)' column and converting it to float
cars['Price (EUR)'] = (
    cars['Price (EUR)'].str.replace(',', '', regex = False).astype(float)
)

## Using a loop to convert important columns to numeric, coercing errors to NaN
numeric_columns = ['HP', '0-100', 'Engine Size (L)', 'Torque (Nm)']

for col in numeric_columns:
    cars[col] = pd.to_numeric(cars[col], errors = 'coerce')


## Converting lb-ft to Nm and USD to EUR
cars['Torque (Nm)'] = cars['Torque (Nm)'] * 1.35582

cars['Price (EUR)'] = cars['Price (EUR)'] * 0.85


## Creating a new column 'Vehicle' by combining the 'Car Make' and 'Car Model' columns
cars['Vehicle'] = cars['Car Make'] + ' ' + cars['Car Model']

## Deleting the, now unnecessary, 'Car Make' and 'Car Model' columns
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
## This will create a new column 'Vehicle_clean' in both dataframes with the cleaned vehicle names
laps["Vehicle_clean"] = laps["Vehicle"].apply(clean_vehicle_name)
cars["Vehicle_clean"] = cars["Vehicle"].apply(clean_vehicle_name)

## Removing duplicates from both dataframes based on the new 'Vehicle_clean' column
cars = cars.drop_duplicates(subset = "Vehicle_clean", keep= "first")

## Function to perform fuzzy matching and return the best match if the score is above a certain threshold
car_names = cars["Vehicle_clean"].unique()

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
nls = nls.drop(columns = [
    "Vehicle_y",
    "Vehicle_clean_x",
    "Vehicle_clean_y",
    "Vehicle_match"
])

