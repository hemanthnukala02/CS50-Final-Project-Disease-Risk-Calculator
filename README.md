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
Next, after cleaning the data, I had to train 4 models to help predict each disease. For this, I chose to use the Random Forest algorithm, which is a decison-tree type of machine learning algorithm, to do so. This is because it is able to handle large datasets, such as the one im using, efficiently and is suitable for handling mixed data types such as the free responses answers for height and weight and the multiple choice answers for the other categories. After this, I had to encode the datapoints for the categories whose responses were in the multiple choice format as this most models like the Random Forest model can only work with data in the numerical form. Hence, I used the encoding method, `pd.get_dummies` from the pandas library. Next, I proceeded to train and test 4 models, one for each disease, with an 80/20 split due to the relatively large size of my dataset. 

### The HTML
So, as for the website, I made 2 HTML files, index.html and results.html. The index page serves as the page where the user can fill in their information for the 7 necessary categories. The calculator then uses the user's input and through some Python code, which I will explain in the next section, outputs the results that were calculated. 

In the index page, information for the 7 categories consisted of a mix between free response questions for the height and weight categories and multiple choice questions for the rest of the categories. Of the multiple choice questions, the categories with just 2 options like the gender category use an input tag of type radio to produce the required 2 buttons. This helps make it easier for the users to select their desired option. However, for the categories such as age group, as there were many options to choose from, a dropdown format would be more efficient and aesthetic. Hence, for those categories I used the select and option tags to do so.

I also added an info icon for the exercise category to allow for users to clear any doubts on what exercise may refer to. To execute this, I used a small amount of Javascript to be able to listen to when the user clicks the info icon and then trigger a pop-up that contains the information on what the exercise category refers to. The pop-up will remain onscreen for a sufficient amount of time for the user to read the information before disappearing.

For the results page, I had chose to keep it simple and straighforward and just loop through a dictionary called predictions I had created using the Python code. This helps print out the disease risk being calculated by my models in order according to their respective diseases in a consistent format. 

As for the style.css, I also kept it pretty simple and set a class of site-header for my h1 header and container for the content portion in both HTML files. With the site-header class, I made the background blue to stand out against the light grey background of my body. I also made the container an even lighter colour grey to further stand out the important content portion against the rest of the website.

### The Python
For the Python code, I used a routes.py file to be able to take the user input from the index template and pass it to the 4 trained models for prediction. In this file, I also conducted error checking to make sure all 7 fields were filled when being submitted so that it does not cause any errors on the risk prediction side of things.

I also created a model.py file to download my trained models using the `load` function from the joblib library. Afterwards, I defined a function, `predict_disease_risk`, that I will use in my routes.py to pass the user input through and produce the risk predictions and from there output it to the results template. In this function, I first used `pd.DataFrame` from the pandas library to arrange the user data in a suitable data frame to be used. Then, I encoded the user data using the same `pd.get_dummies` function just as how I did so for my training and testing data during the training of my models. Next, I used the `predict_proba` function from the sklearn library to use the models to predict the probability of the user getting the respective diseases and from there converting it to a percentage format and then being saved as a dictionary in `disease_risk`.

## The End




