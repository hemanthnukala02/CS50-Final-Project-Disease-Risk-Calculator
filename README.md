# CS50 Final Project: Disease Risk Calculator
A calculator that predicts the user's risk of 4 diseases.

#### Video Demo: <https://youtu.be/CMihKRgkvk4>
#### Description:

## Overview of the Project
This is a calculator that, as the name suggests, calculates the percentage risk of the user getting a certain disease. This calculator will predict the user’s risk of getting 4 non-communicable diseases, namely Arthritis, Cancer, Diabetes and Heart Disease. It does this based off of the user's information on 7 different categories; Age, Sex, Height, Weight, Exercise, Smoking History and Frequency of Alcohol Consumption.

### Background
The 7 categories above influence a person’s risk of developing these non-communicable diseases as the first four factors, age, sex, height and weight, give an indication of a person’s inherent predisposition to getting these diseases while the other 3 factors, exercise, smoking history and frequency of alcohol consumption, indicate lifestyle choices that play a big part in determining a person’s risk of getting the above 4 diseases. 

### Potential shortcomings
However, as a disclaimer, these 7 factors only give a rough estimate of a person’s risk of disease as there definitely are other genetic, environmental and behavioural factors that play a part. Examples of such factors can be family history of certain diseases like Heart Disease or amount of daily exposure to carcinogenic chemicals like those common at construction or mining sites.

## How I made this calculator

### The data
I obtained the dataset from Kaggle, made by the Kaggle username, "ALPHIREE". The dataset contained 19 columns consisting of both the independent and dependent variables affecting disease risk. However, as there certain rows with no units provided such as Fruit Consumption, I removed those columns in order not to create unnecessary skewing of data due to misinformed data. 

There were also some columns such as General Health which prompted for how the user felt the state of his general health was. While this generally does correlate well as better overall health does correlate with a lower risk of having the 4 diseases above, estimating the state of one's general health is very vague as there is no distinct line to draw between 'Very Good' and 'Good' health. Hence, I removed these rows as well. 

Lastly, there were columns with datapoints that can cause a data model to skew certain ways. For example, the column for Diabetes had an option for pregnancy-induced diabetes which would skew the data slightly as it is not possible to predict if a female user with an age that deems them capable of carrying a foetus is actually pregnant and thus, being higher higher likely to have pregnancy-induced diabetes. Moreover, generalising all pregnancy-induced diabetes cases as diabetes would just wrongly increase the percentage risk of that age group of female users having Diabetes. Hence, I removed all datapoints providing such responses that were of special cases. 

### The models
Next, after cleaning the data, I had to train 4 models to help predict each disease. For this, I chose to use the Random Forest algorithm, which is a decison-tree type of machine learning algorithm, to do so. This is because it is able to handle large datasets, such as the one im using, efficiently and is suitable for handling mixed data types such as the free responses answers for height and weight and the multiple choice answers for the other categories. After this, I had to encode the datapoints for the categories whose responses were in the multiple choice format as this most models like the Random Forest model can only work with data in the numerical form. Hence, I used the encoding method, pd.get_dummies from the pandas library. Next, I proceeded to train and test 4 models, one for each disease, with an 80/20 split due to the relatively large size of my dataset. 




