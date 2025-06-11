import pandas as pd
import plotly.express as px


import streamlit as st
st.title ("# PERFORMANCE")
#create a data frame
df= pd.read_csv("student_habits_performance.csv")
#st.table(df)


#code for data inspection
st.markdown("### FIRST  5 DATA")
Pa = df .  head(5)
st.table(Pa)

#code for data inspection
st.markdown("### LAST 5 DATA")
we = df .tail(5)
st.table(we)

#code for data inspection
st.markdown("### DATA INFO")
my = df.info
st.write(my)

#code for data inspection
st.markdown ("### DATA DESCRIBE")
my = df. describe()
st.write(my)

#code for data inspection
st.markdown("### DATA SHAPE")
my = df.shape
st.table(my)


st.markdown("## UNIVARIATE VARIABLES")
#code to pick a column in a table - univariate
df =  pd.read_csv("student_habits_performance.csv")
netflix_hours = df["netflix_hours"].describe()
st.markdown ("### gender netflix_hours")
st.table(netflix_hours)


st.title("GRAPH REPRESENTATION")
netflix_hours =px.histogram(df["netflix_hours"], x = "netflix_hours", title = "gender")
st.plotly_chart(netflix_hours, use_container_width = True)

#display string type data using bar chart
st.title("Bar Graph Representation")
gender_count = df["gender"].value_counts()
gender_count.columns = ["gender", "counts"]
gender_count2 =px.bar(df["gender"], x = "gender", title = "gender")
st.plotly_chart(gender_count2, use_container_width = True)


st.title("GRAPH REPRESENTATION")
import plotly.express as px

# Example assuming you have a DataFrame with columns 'gender' and 'netflix_hours'
netflix_hours = px.pie(df, names="gender", values="netflix_hours", title="Netflix Hours by Gender")
netflix_hours.show()
st.plotly_chart(netflix_hours, use_container_width = True)



