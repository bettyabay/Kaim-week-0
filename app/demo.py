import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
 

# Load the dataset
data = pd.read_csv("C:/Users/USER/Desktop/KAIM/data0/benin-malanville.csv")

# Preview the data
st.dataframe(data.head())


# Set a title for the app
st.title("Data Insights Dashboard")

# Sidebar for user inputs
st.sidebar.header("User Input")
option = st.sidebar.selectbox("Select a feature", ["Overview", "Visualization", "Statistics"])

# Display results based on user input
if option == "Overview":
    st.subheader("Dataset Overview")
    st.write(data.describe())
elif option == "Visualization":
    st.subheader("Visualize Data")
elif option == "Statistics":
    st.subheader("Detailed Statistics")




st.sidebar.header("Bar Chart Options")
column = st.sidebar.selectbox("Select Column", data.columns)

# Generate bar chart
st.subheader(f"Bar Chart for {column}")
fig, ax = plt.subplots()
data[column].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)


st.line_chart(data[column])



x_col = st.sidebar.selectbox("X-Axis", data.columns)
y_col = st.sidebar.selectbox("Y-Axis", data.columns)

fig = px.scatter(data, x=x_col, y=y_col)
st.plotly_chart(fig)

