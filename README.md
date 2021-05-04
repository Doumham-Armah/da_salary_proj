# Data Analyst Salary Prediction: Project Overview

* Created a tool that estimates data analyst salaries (MAE ~ $ 16K) to help them negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing web app using Streamlit 
## Acquiring The Data

Coded my own web scraper to scrape over 1000 job postings from glassdoor.com. With each job, we got the following:
*	Job title
*	Salary Estimate
*	Rating
*	Company 
*	Location
*	Company Size
*	Company Founded Date
*	Type of Ownership 
*	Industry
*	Sector
*	Revenue

## Model Building 

First, I transformed the categorical variables into dummy variables. Then, I also split the data into train and test sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error.

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Hyperparameter Autotuning 
I used GridsearchCV to tune the hyperparameters on the random forest model.
The Random Forest model outperformed the other models on the test and validation sets:
*	**Random Forest** : MAE = 16k USD
*	**Linear Regression**: MAE = 18.2K USD
*	**Ridge Regression**: MAE = 24K USD

## Productionization 
In this step, I built a StreamLit application and hosted it on my own machine. The web app lets the user input all the features by typing and choosing from drop down menues and returns an estimated salary. 


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.