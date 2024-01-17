import pickle

import streamlit as st
st.title('car credentials will gift you its price')

fuel_type = st.number_input('1 for cng 2 for diesel 3 for petrol')
kms_driven = st.number_input('number of kilometers driven')
ownership = st.number_input('1 for first 2 for second hand 3 for third hand')
transmission = st.number_input('1 for manual 2 for automatic')
manufacture_year = st.number_input('Manufacturing year')
mileage = st.number_input('Enter mileage')
engine = st.number_input('engine in cc')
model = pickle.load(open('model.pkl','rb'))
if st.button('Predict'):
    pred = model.predict([[fuel_type,kms_driven,ownership,transmission,manufacture_year,mileage,engine]])
    st.header(pred)