# Nordschleife-Analysis
## Introduction
The Nürburgring Nordschleife is regarded as the benchmark for vehicle performance.
With its unique combination of high-speed straights, technical corners, elevation changes, and demanding track conditions,
it provides one of the most comprehensive tests for both drivers and cars.

This project focuses on the analysis of the Nürburgring Nordschleife lap times.
The objective is to build a machine learning model that predicts Nordschleife lap times from vehicle specifications.
The goal is to uncover patterns that influence track performance and have some fun with cars.

## The following preprocessing steps were performed:
- Removed irrelevant columns
- Converted torque from lb-ft to Nm
- Converted prices from USD to EUR
- Standardized vehicle names
- Merged both datasets

## Learn about Data
### Nürburgring Lap Times Dataset
Cointains:
- Lap Time
- Vehicle Name
- Driver Name
- Date
  
### Sports Cars Dataset
Contains:
- Vehicle Name
- Production Year
- Engine Size in L
- Horsepower
- Torque in Nm
- 0-100 Time (Note: actually the 0-60 mph time, just the name is changed)
- Price in EUR

At the end we have a merged dataset 'NLS' which contains all information.

## Used tools and packagges

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

## Notebook

A polished analysis notebook is available on Kaggle:
[View Kaggle Notebook](...)


