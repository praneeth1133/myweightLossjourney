import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

def initialize_weight_data():
    """Initialize weight tracking data in session state"""
    if 'weight_data' not in st.session_state:
        st.session_state.weight_data = pd.DataFrame(
            columns=['Date', 'Weight'],
            data=[[pd.to_datetime('2024-01-01'), 325]]  # Starting weight with proper datetime
        )

def add_weight_entry(date, weight):
    """Add a new weight entry to the tracking data"""
    new_entry = pd.DataFrame([[pd.to_datetime(date), weight]], columns=['Date', 'Weight'])
    st.session_state.weight_data = pd.concat([st.session_state.weight_data, new_entry], ignore_index=True)

def display_weight_tracker():
    """Display weight tracking interface and visualizations"""
    st.subheader("Weight Tracker")

    # Weight input form
    col1, col2 = st.columns(2)
    with col1:
        input_date = st.date_input("Date", datetime.now())
    with col2:
        input_weight = st.number_input("Weight (lbs)", min_value=100.0, max_value=400.0, value=325.0, step=0.1)

    if st.button("Add Weight Entry"):
        add_weight_entry(input_date, input_weight)
        st.success("Weight entry added successfully!")

    # Display weight progress graph
    if len(st.session_state.weight_data) > 0:
        # Ensure dates are datetime
        st.session_state.weight_data['Date'] = pd.to_datetime(st.session_state.weight_data['Date'])

        fig = px.line(
            st.session_state.weight_data,
            x='Date',
            y='Weight',
            title='Weight Progress'
        )
        fig.add_hline(y=220, line_dash="dash", annotation_text="Goal: 220 lbs")
        st.plotly_chart(fig)

        # Display weight history table with formatted dates
        st.subheader("Weight History")
        display_df = st.session_state.weight_data.copy()
        display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
        st.dataframe(
            display_df.sort_values(by='Date', ascending=False),
            hide_index=True
        )