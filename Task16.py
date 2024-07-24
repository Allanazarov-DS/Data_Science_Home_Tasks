import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, RobustScaler, MinMaxScaler
import altair as alt

st.write("""
## Restaurant Data Visualization
""")

# Load data
df = sns.load_dataset('flights')

st.sidebar.header('Choose Scaling Method')
scaling_method = st.sidebar.radio('Choose a scaling method', ['None', 'Standardization', 'Robust Scaling', 'MinMax Scaling'])

if scaling_method != 'None':
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    if scaling_method == 'Standardization':
        scaler = StandardScaler()
    elif scaling_method == 'Robust Scaling':
        scaler = RobustScaler()
    elif scaling_method == 'MinMax Scaling':
        scaler = MinMaxScaler()
    
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

st.write(df.head())

visualization = st.selectbox("Choose the visualization type:", ['Histogram', 'Scatterplot', 'Boxplot', 'Heatmap', 'Linechart', 'Areachart', 'Map'], index=3)

if visualization == 'Histogram':
    column = st.selectbox("Select column for histogram:", df.columns)
    st.write(f'Histogram of {column}')
    st.bar_chart(df[column])

elif visualization == 'Scatterplot':
    x_col = st.selectbox("Select X-axis column for scatterplot:", df.columns)
    y_col = st.selectbox("Select Y-axis column for scatterplot:", df.columns)
    st.write(f'Scatterplot of {x_col} vs {y_col}')
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    ax.set_title(f'Scatterplot of {x_col} vs {y_col}')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

elif visualization == 'Boxplot':
    x_col = st.selectbox("Select X-axis column for boxplot:", df.columns)
    y_col = st.selectbox("Select Y-axis column for boxplot:", df.columns)
    st.write(f'Boxplot of {y_col} by {x_col}')
    fig, ax = plt.subplots()
    sns.boxplot(x=df[x_col], y=df[y_col], ax=ax)
    ax.set_title(f'Boxplot of {y_col} by {x_col}')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    st.pyplot(fig)

elif visualization == 'Heatmap':
    st.write('Correlation Heatmap')
    corr = df.select_dtypes('number').corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

elif visualization == "Linechart":
    y_col = st.selectbox("Select Y-axis column for line chart:", df.columns)
    df_line_chart = df.set_index(df.columns[0])  
    st.write(f'Line Chart of {y_col}')
    st.line_chart(df_line_chart[y_col])

elif visualization == "Areachart":
    y_col = st.selectbox("Select Y-axis column for area chart:", df.columns)
    df_area_chart = df.set_index(df.columns[0])  
    st.write(f'Area Chart of {y_col}')
    st.area_chart(df_area_chart[y_col])

elif visualization == "Map":
    st.write('Map')
    df_map = df[[df.columns[0], df.columns[1]]]
    df_map.columns = ['lat', 'lon']
    st.map(df_map)
