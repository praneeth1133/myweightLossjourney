import streamlit as st
import random
from utils.meal_planner import display_meal_plan, setup_meal_notifications
from utils.weight_tracker import initialize_weight_data, display_weight_tracker
from utils.grocery_helper import display_grocery_list

# Page configuration
st.set_page_config(
    page_title="Praneeth's Weight Management Dashboard",
    page_icon="🏋️",
    layout="wide"
)

# Motivational quotes
QUOTES = [
    {"text": "The only bad workout is the one that didn't happen.", "author": "Unknown"},
    {"text": "Your body can stand almost anything. It's your mind you have to convince.", "author": "Unknown"},
    {"text": "Weight loss is a journey, not a destination.", "author": "Unknown"},
    {"text": "Success is walking from failure to failure with no loss of enthusiasm.", "author": "Winston Churchill"},
    {"text": "The difference between try and triumph is just a little umph!", "author": "Marvin Phillips"}
]

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stMetric {
        background-color: #252526;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s ease;
    }
    .stMetric:hover {
        transform: translateY(-5px);
    }
    .quote-card {
        background-color: #252526;
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .quote-text {
        font-size: 1.5rem;
        font-style: italic;
        margin-bottom: 1rem;
        color: #4CAF50;
    }
    .quote-author {
        font-size: 1rem;
        color: #888;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #252526;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Header with animation
st.markdown("""
    <div style='text-align: center; animation: fadeIn 1s ease-in;'>
        <h1>🏋️ Praneeth's Weight Management Dashboard</h1>
        <p style='font-size: 1.2rem; color: #4CAF50;'>Your journey to a healthier you starts here!</p>
    </div>
""", unsafe_allow_html=True)

# Daily motivational quote
daily_quote = random.choice(QUOTES)
st.markdown(f"""
    <div class="quote-card">
        <div class="quote-text">"{daily_quote['text']}"</div>
        <div class="quote-author">- {daily_quote['author']}</div>
    </div>
""", unsafe_allow_html=True)

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

# Footer with progress visualization
st.markdown("---")
st.markdown("""
    <div style='text-align: center; animation: fadeIn 1s ease-in;'>
        <h3>Your Weight Loss Journey</h3>
        <div style='background: #252526; border-radius: 10px; padding: 20px; margin: 20px 0;'>
            <p>Starting Weight: 325 lbs → Target Weight: 220 lbs</p>
            <p>Keep pushing forward! Every step counts! 💪</p>
        </div>
    </div>
""", unsafe_allow_html=True)