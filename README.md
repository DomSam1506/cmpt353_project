# Game Data Analysis Project

# Overview
This project was for my SFU CMPT 353 course and explores factors influencing video game popularity, defined primarily by average user ratings ("love"). Using a dataset of thousands of games from RAWG.io, the analysis includes exploratory data analysis, statistical testing, and predictive modeling.

## Repository Structure

**data**\
| File | Description |
|------|-------------|
| `games_data.csv` | Raw data extracted from RAWG API |
| `games_data_cleaned.csv` | Cleaned and processed dataset |

**notebooks**\
| File | Description |
|------|-------------|
| `clean.ipynb` | Data cleaning and feature enginnering |
| `exploration.ipynb` | Exploratory data analysis and visualizations |
| `tests.ipynb` | Statistical hypothesis testing |
| `models.ipynb` | Machine learning models for regression and classification |
| `games_collection.ipynb` | Data extraction and collection from RAWG API |

| File | Description |
|------|-------------|
| `CMPT 353 REPORT.pdf` | Final analysis report |
| `plots.py` | Visualization helper functions |
| `requirements.txt` | List of required libraries |

## Setup and Requirements

* An official RAWG API key (free using email) or using the data provided
* Python 3.11+: Speciifc libraries listed in `requirements.txt`


## Usage Guide:
All important files are made notebooks for convenience of users and can be run easy without use of arguments. Many notebooks assume plots.py is included in the orignal folder for importing visulization functions

Markdown files and comments are included within the notebooks to guide user on analysis.

### **Data Extraction:**

Run games_collection.ipynb to fetch raw data from the RAWG API if you want to test different datasets. This produces games_data.csv

Note: You must get a free API key from RAWG as the API key used in the project is hidden for privacy reasons.

### **Data Cleaning:**

Run clean.ipynb to clean and process the raw dataset. This will produce games_data_cleaned.csv

### **Exploratory Analysis & Testing:**

Run exploration.ipynb and stats.ipynb to perform EDA and hypothesis testing on the cleaned dataset. Users are free to experiment with different datasets once API key is obtained

### **Machine Learning Modeling:**

Run model.ipynb to train and evaluate the regression and classification models.


## NOTES:
Analysis on Metacritic Ratings found in notebooks was only supplementary and not focus of the project.

All important visualizations are contained within the notebooks and final report in an interpretable order for the reader.

Thank you for visiting my project, this took a lot of time and effort and I appreciate you checking it out!

Author: Dominion Ubong Samuel, dus@sfu.ca


