import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('st.write')

st.header('Display text')
st.write('Hello there ! :sunglasses:')

st.header('Display numbers')
st.write(1234)

st.header('Display Dataframe')
ser = pd.Series([1,2,3,4], index = ["a", "b", "c", "d"])
df = pd.DataFrame(data = ser, index = ["a", "b", "c", "d"])
st.write(df)

st.header('Accept multiple arguments')
st.write('Below is a dataframe', df, 'Above is a dataframe')

st.header('Display charts')
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size = 'c', color = 'c', tooltip = ['a','b','c']
)
st.write(c)