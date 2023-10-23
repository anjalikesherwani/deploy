import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

col1, col2, col3 = st.columns(3)


a = {
    'name':['abc','xyz'],
    'age':[23,45],
    'city':['nyc','sf']
}

df = pd.read_csv('data.csv')

st.title("Data Analysis")
#st.write(df)
#st.write(a)


df1 = df.drop(['ID','Year','Category','Product','UnitPrice','TotalPrice'],axis = 'columns')
#st.write(df1)




if st.sidebar.button('load dataset'):
    st.write(df)

if st.sidebar.button('load description'):
    st.write(df.describe())


if st.sidebar.button('load chart'):
    df2 = df.head(20)


    fig = plt.figure(figsize=(10,8))
    plt.plot(df2['Year'],df2['TotalPrice'])
    plt.xlabel('Year')
    plt.ylabel('Total Price')
    st.pyplot(fig)

    fig = plt.figure(figsize=(10,8))
    plt.bar(df2['Category'],df2['Qty'])
    plt.xlabel('Category')
    plt.ylabel('Qty')
    st.pyplot(fig)


#col1.metric("Name",'a','b')
#col2.metric("Age",'20','24')
#col3.metric("City",'patna','ald')



col1.metric("Year",'2022','2021')
col2.metric("India",'$4301','$4100')


