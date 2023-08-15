import streamlit as st
import  pickle as pkl
import numpy as np
st.title("Car Price Predictor")
pipe=pkl.load(open('pipe.pkl','rb'))
df=pkl.load(open('df.pkl','rb'))

# company
com=st.selectbox('company name',df['company'].unique())

#model
mod=st.selectbox('car model',df['model'].unique())

# year
year=st.selectbox('manufacturing year',[2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000])

#kilometer driven
kms_driven=float(st.number_input('Kilometer Driven'))

#fuel type
fuel=st.selectbox('fuel',['Petrol','Diesel'])

if st.button('Predict price'):
    if(fuel=='Petrol'):
        fuel=0
    else:
        fuel=1
    query=np.array([com,year,kms_driven,fuel,mod])
    query=query.reshape(1,5)
    st.title("This Car price is: " + str(int(np.exp(pipe.predict(query)[0]))) + " \u20B9 ")
