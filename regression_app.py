#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import pickle
import streamlit as smt
from PIL import Image
from sklearn import datasets
  
# loading in the model to predict on the data
pickle_in = open('model1.pkl', 'rb')
model1 = pickle.load(pickle_in)
#model=pd.read_csv("C:\Users\BRAVE BARAKA\Breast cancer prediction\data.csv")
def welcome():
    return 'welcome all'
  
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(Avg_Area_Income, Avg_Area_House_Age,Avg_Number_of_Rooms,
       Avg_Area_Number_of_Bedrooms, Area_Population):  
   
    prediction=model.predict([[Avg_Area_Income, Avg_Area_House_Age,Avg_Number_of_Rooms,
       Avg_Area_Number_of_Bedrooms, Area_Population]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    smt.title("House Price Prediction Model")
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:blue ;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit House Price ML App by BRAVE BARAKA</h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    smt.markdown(html_temp, unsafe_allow_html = True)
       
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    Avg_Area_Income = smt.number_input ("Avg. Area Income") 
    Avg_Area_House_Age = smt.number_input ("Avg. Area House Age")
    Avg_Number_of_Rooms = smt.number_input ("Avg. Area Number of Rooms")
    Avg_Area_Number_of_Bedrooms = smt.number_input ("Avg. Area Number of Bedrooms")
    Area_Population = smt.number_input ("Area Population")
    X = pd.DataFrame([[Avg_Area_Income, Avg_Area_House_Age,Avg_Number_of_Rooms,
       Avg_Area_Number_of_Bedrooms, Area_Population]], 
                     columns = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population'])
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if smt.button("Predict"):
        prediction = model1.predict(X)[0]
        #smt.success('The output is {}'.format(result))
     # Output prediction
        #X = X.replace(["M", "B"], [1, 0])
        smt.text(f"This instance is a Ksh.{prediction}")
        print(X)
     
if __name__=='__main__':
    main()

