# Nordschleife-Analysis
## Introduction

This project focuses on the analysis of the Nürburgring Nordschleife lap times.
The objective is to build a machine learning model that predicts Nordschleife lap times from vehicle specifications.
The goal is to uncover patterns that influence track performance and have some fun with cars.

## Learn about Data
The raw lap-time dataset was merged with a sports-car specification dataset.
The final dataset used in this analysis was generated using the data preparation pipeline implemented in `Data.py`.

At the end we have a merged dataset 'nls' which contains these columns:

| Variable | Description |
| ---------|-------------|
| Time     | Lap Time    |
| Vehicle  | Vehicle Name | 
| Driver   | Driver Name |
| Year     | Production Year |
| Engine Size (L) | Engine Size in Liters |
| HP       | Horsepower |
| Torque (Nm) | Torque in Nm |
| 0-100    | 0-100 km/h time |
| Price (EUR) | Price in Eur |

### Final dataset:
- 208 vehicles
- 9 variables
- Target variable: Lap Time

## The following preprocessing steps were performed:
- Standardized vehicle names for matching
- Converted torque, acceleration and price units
- Merged lap-time and vehicle-specification datasets
- Removed duplicate entries
- Filtered missing observations

## Used tools and packagges

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

## Repository Structure
``` text
Nordschleife_Analyse/
├──Code/                                # Data Preperation
│    └──Data.py                         
├──Data/                                # Datasets
│   └──laps.csv
│   └──nls.csv
│   └──Sport car price (1).csv
├──Notebook/                            # Exploratory Analysis and ML models
│   └──Nordschleife Analysis.ipynb
└──README.md

## Notebook

A polished analysis notebook is (soon) available on Kaggle:
[View Kaggle Notebook](...)


