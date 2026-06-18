# Nordschleife-Analysis
## Introduction
The Nürburgring Nordschleife is regarded as the benchmark for vehicle performance.
With its unique combination of high-speed straights, technical corners, elevation changes, and demanding track conditions,
it provides one of the most comprehensive tests for both drivers and cars.

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

## The following preprocessing steps were performed:
- Cleaned vehicle names
- Converted units
- Merged datasets
- Removed duplicates
- Handled missing values

## Used tools and packagges

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

## Repository Structure
Code/
Data/
Notebook/

## Notebook

A polished analysis notebook is available on Kaggle:
[View Kaggle Notebook](...)


