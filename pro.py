import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
from math import sqrt
from sklearn.metrics import mean_squared_error


st.set_page_config(page_title="Demand forecasting for manufacturing")


def main():
    st.title("Demand Forecasting")
    st.write("You are welcomed to the prediction world where in the prediction of Beer Manufacturing data that we had as a project.\nThe goal was to predict order quantity of beers from 2020-05-01 to 2020-05-15 using verious Forecasting Mehtods.\n The data is provided you can check how close forecasts are to the actual values")
    tech = ["Holt's Winter","ARIMA","SARIMA","FBprophet","SimpleExponentialSmoothing","Holt's Linear Trend",]

    data = pd.read_csv("prediction3 (1).csv")
    data.drop("Unnamed: 0", axis=1, inplace=True)
    data.set_index("Checkout_Date", inplace=True)
    data.pop('indexing')
    st.dataframe(data)
    st.write("## Techniques Used")
    for t in tech:
        st.write(t)

    #plotting
    ls = data.columns.tolist()
    options = st.multiselect("Choose Forecasting Methods",ls,default="Order_Quantity")
    user = data[options]
    fig = plt.figure()
    st.line_chart(user)

    #Evaluation Metric
    st.subheader("Evaluation Metrics")
    score = 0
    agree = st.button("show RMSE score")
    if agree:
        for i in user.columns:
            if i!="Order_Quantity":
                score = sqrt(mean_squared_error(user[i].values, data["Order_Quantity"].values))
                txt = f"Mean Squared Error for {st.write(i)}: {st.success(round(score,2))}"
                # st.write(txt)

    st.subheader("Comparison of values")
    comp = st.button("Show")
    if comp:
        st.table(user)

    st.info("Conlusions from the predictoions")
    txt2 = "1. on the weekends our sale are very high as comapared to the weekdays "
    txt3 = "2. The time series consists noice, it means there are exceptions in our series which could be due to varying reasons."
    txt4 = "3. Inorder to incorporate the Algorithms the stationarity was checked and the result was that the data was stationary"
    txt5 = "4. Based on the root mean Sqaured error we have the best model as Fbprophet.?n Though there is scope of imporvement using optimizes"
    for j in [txt2,txt3,txt4,txt5]:
        st.write(j)

    st.write("## Thank you for Visiting \nProject by Ishika Shivhare")
if __name__ == '__main__':
  main()