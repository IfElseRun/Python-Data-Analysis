# NYC Restaurant Inspection Data Analysis


## Problem Statement, Motivation and Purpose

Choosing a favorite restaurant in New York City is a joyful task with myriad possibilities depending on the occasion, mood and even the time of year. Being among the most diversed cities in the world with around 800 native languages, you can find any type of restaurant with varieties of cuisines.

DIfferent mobile and web application as Yelp, Google Business Reviews and Grubhub are often a starting research point for many as it allows them to get an idea of other restaurant goers' experience at each restaurant.

In order to operate every restaurant is graded and has to pass special program inspection conducted by NYC every year which is also one important aspect that many restaurant goers will consider prior to eating at a restaurant. However, not that many applications that offer restaurant search offer more details on restaurant health over time.

The motivation of this research is to analyze NYC inspection data, better understand overall restaurants health and analyze one of the potential user journeys. 

## Tools & Methods

The tools that were used for the data analysis project are: 
-- MySQL Workbench Database Managamenet Software for schema cration, MySQL execution and raw data manipulation
-- Jupyter Notebook using Anaconda for Python execution and data visualization

## Data Set 

The dataset contains every sustained or not yet adjudicated violation citation from every full or special program inspection conducted up to three years prior to the most recent inspection for restaurants and college cafeterias in an active status on the RECORD DATE (date of the data pull)

### Data Set Source

[NYC OPEN DATA](https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j)


 **Column Name**       	| **Column Description**                                                          	|
|-----------------------	|---------------------------------------------------------------------------------	|
|                       	|                                                                                 	|
| CAMIS                 	| Unique identifier for the establishment (restaurant)                            	|
| DBA                   	| Establishment (restaurant) name                                                 	|
| BORO                  	| Borough of establishment (restaurant) location                                  	|
| BUILDING              	| Building number for establishment (restaurant) location                         	|
| STREET                	| Street name for establishment (restaurant) location                             	|
| ZIPCODE               	| Zip code of establishment (restaurant) location                                 	|
| PHONE                 	| Phone number                                                                    	|
| CUISINE DESCRIPTION   	| Establishment (restaurant) cuisine                                              	|
| INSPECTION DATE       	|                                                                                 	|
| ACTION                	| Action associated with each establishment (restaurant) inspection               	|
| VIOLATION CODE        	| Violation code associated with an establishment (restaurant) inspection         	|
| VIOLATION DESCRIPTION 	| Violation description associated with an establishment  (restaurant) inspection 	|
| CRITICAL FLAG         	| Indicator of critical violation                                                 	|
| SCORE                 	| Total score for a particular inspection                                         	|
| GRADE                 	| Grade associated with the inspection                                            	|
| GRADE DATE            	| Date when grade was issued to the establishment (restaurant)                    	|
| RECORD DATE           	| Date record was added to dataset                                                	|
| INSPECTION TYPE       	| A combination of the inspection program and the type of inspection performed    	|