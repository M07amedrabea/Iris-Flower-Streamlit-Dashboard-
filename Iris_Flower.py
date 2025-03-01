import pandas as pd
from sklearn import datasets

import streamlit as st

from sklearn.ensemble import RandomForestClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target

model = RandomForestClassifier()

model.fit(X,y)

# Streamlit Structure

st.write("Simple Classifier For **Iris Flower** App !")

st.sidebar.header('Input Parameters')
#st.sidebar.slider()

def User_inputs():

    first = st.sidebar.slider('sepal length (cm)',4.3,7.9,5.4)
    second = st.sidebar.slider('sepal width (cm)',2.5,4.4,3.4)
    third = st.sidebar.slider('petal length (cm)',1.0,6.9,1.3)
    forth = st.sidebar.slider('petal width (cm)',0.1,2.5,0.2)

    data = {
        'sepal length (cm)':first,
        'sepal width (cm)':second,
        'petal length (cm)':third,
        'petal width (cm)':forth,
    }

    features = pd.DataFrame(data ,index=[0])

    return features

df = User_inputs()

st.subheader('User Inputs Parameters')

st.write(df)

st.subheader('Target Names')

st.write(iris.target_names)

prediction = model.predict(df)

prediction_Probability = model.predict_proba(df)

st.subheader('Prediction')
st.write(iris.target_names[prediction])


st.subheader('Probability of Prediction')
st.write(prediction_Probability)

