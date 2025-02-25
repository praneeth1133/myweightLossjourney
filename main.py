import streamlit as st
from utils.meal_planner import display_meal_plan, setup_meal_notifications
from utils.weight_tracker import initialize_weight_data, display_weight_tracker
from utils.grocery_helper import display_grocery_list

# Page configuration
st.set_page_config(
    page_title="Praneeth's Weight Management Dashboard",
    page_icon="🏋️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🏋️ Praneeth's Weight Management Dashboard")
st.write("Welcome to your personalized weight management journey!")

# Initialize session state for weight tracking
initialize_weight_data()

# Main navigation
tab1, tab2, tab3 = st.tabs(["📋 Meal Plan", "⚖️ Weight Tracker", "🛒 Grocery List"])

with tab1:
    display_meal_plan()
    setup_meal_notifications()

with tab2:
    display_weight_tracker()

with tab3:
    display_grocery_list()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        Target Weight: 220 lbs by End of 2025<br>
        Stay consistent and committed to your goals! 💪
    </div>
""", unsafe_allow_html=True)
