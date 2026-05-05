import streamlit as st
import pandas as pd
import plotly.express as px

# Page settings
st.set_page_config(page_title="Student Productivity Dashboard", layout="wide")

# Title
st.title("📚 Student Productivity Dashboard")
st.markdown("Analyze student study habits and productivity")

# Load dataset
df = pd.read_csv(r"student-productivity-dashboard/student_productivity_data.csv")

# Show data
st.subheader("Student Productivity Dataset")
st.dataframe(df)

# KPI Section
st.subheader("Overall Performance")

col1, col2, col3 = st.columns(3)

col1.metric("Average Study Hours", round(df["Study_Hours"].mean(), 2))
col2.metric("Average Attendance", round(df["Attendance"].mean(), 2))
col3.metric("Average Productivity Score", round(df["Productivity_Score"].mean(), 2))

# Productivity Distribution
st.subheader("Productivity Score Distribution")
fig1 = px.histogram(df, x="Productivity_Score", nbins=10)
st.plotly_chart(fig1, use_container_width=True)

# Study Hours vs Productivity
st.subheader("Study Hours vs Productivity")
fig2 = px.scatter(
    df,
    x="Study_Hours",
    y="Productivity_Score",
    color="Attendance",
    size="Assignments_Completed",
    hover_data=["Student_ID"]
)
st.plotly_chart(fig2, use_container_width=True)

# Attendance Chart
st.subheader("Attendance of Students")
fig3 = px.bar(df, x="Student_ID", y="Attendance", color="Attendance")
st.plotly_chart(fig3, use_container_width=True)

# Sleep vs Productivity
st.subheader("Sleep Hours vs Productivity")
fig4 = px.line(df, x="Sleep_Hours", y="Productivity_Score", markers=True)
st.plotly_chart(fig4, use_container_width=True)