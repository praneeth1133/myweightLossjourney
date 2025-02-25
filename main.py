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

# Initialize theme state
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# Dynamic theme colors
THEME = {
    'dark': {
        'bg': '#1E1E1E',
        'secondary_bg': '#252526',
        'text': '#FFFFFF',
        'primary': '#4CAF50',
        'secondary_text': '#888888'
    },
    'light': {
        'bg': '#FFFFFF',
        'secondary_bg': '#F0F2F6',
        'text': '#262730',
        'primary': '#2E7D32',
        'accent': '#4CAF50',
        'secondary_text': '#666666'
    }
}

current_theme = THEME[st.session_state.theme]

# Custom CSS with dynamic theming
st.markdown(f"""
    <style>
    .theme-toggle {{
        position: fixed;
        top: 0.5rem;
        right: 1rem;
        z-index: 1000;
        background: transparent;
        border: none;
        cursor: pointer;
        font-size: 1.2rem;
        padding: 0.3rem;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.3s;
        opacity: 0.8;
    }}
    .theme-toggle:hover {{
        opacity: 1;
        background: {current_theme['secondary_bg']};
    }}
    .header-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.5rem 1rem;
        margin-bottom: 1rem;
        background: {current_theme['bg']};
    }}
    .header-title {{
        font-size: 1.5rem;
        margin: 0;
        color: {current_theme['text']};
    }}
    .header-subtitle {{
        font-size: 0.9rem;
        color: {current_theme['primary']};
        margin: 0;
    }}
    .quote-card {{
        background: linear-gradient(
            {'rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)' if current_theme['bg'] == '#FFFFFF' else 
             'rgba(30, 30, 30, 0.9), rgba(30, 30, 30, 0.9)'}), 
            url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiPjxkZWZzPjxwYXR0ZXJuIGlkPSJwYXR0ZXJuIiBwYXR0ZXJuVW5pdHM9InVzZXJTcGFjZU9uVXNlIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+PHJlY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IiNmOGY5ZmEiLz48Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjgwIiBmaWxsPSJub25lIiBzdHJva2U9IiNlY2VkZWUiIHN0cm9rZS13aWR0aD0iMiIvPjxwYXRoIGQ9Ik0wIDAgTDIwMCAyMDAgTTAgMjAwIEwyMDAgMCIgc3Ryb2tlPSIjZTBlMmU2IiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiLz48cGF0aCBkPSJNMTAwIDAgTDEwMCAyMDAgTTAgMTAwIEwyMDAgMTAwIiBzdHJva2U9IiNlMGUyZTYiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIvPjwvcGF0dGVybj48L2RlZnM+PHJlY3Qgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0idXJsKCNwYXR0ZXJuKSIvPjwvc3ZnPg==');
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        animation: fadeIn 0.8s ease-in;
        border: 1px solid {current_theme['secondary_text']}22;
        backdrop-filter: blur(5px);
        position: relative;
        overflow: hidden;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }}
    .quote-text {{
        font-size: 1.2rem;
        font-style: italic;
        margin-bottom: 0.8rem;
        color: {current_theme['primary']};
        line-height: 1.4;
        position: relative;
        z-index: 1;
    }}
    .quote-author {{
        font-size: 0.9rem;
        color: {current_theme['secondary_text']};
        font-weight: 500;
        position: relative;
        z-index: 1;
        padding-top: 0.3rem;
        border-top: 1px solid {current_theme['secondary_text']}22;
        display: inline-block;
    }}
    .stApp {{
        background-color: {current_theme['bg']} !important;
    }}
    </style>
""", unsafe_allow_html=True)

# Theme toggle button
st.markdown(f"""
    <div class="theme-toggle" onclick="
        var event = new CustomEvent('theme_toggle');
        window.dispatchEvent(event);
    ">
        {'🌙' if st.session_state.theme == 'light' else '☀️'}
    </div>
    <script>
        window.addEventListener('theme_toggle', function() {{
            var form = document.createElement('form');
            form.method = 'POST';
            form.action = '';
            var input = document.createElement('input');
            input.type = 'hidden';
            input.name = '🌓 Toggle Theme';
            input.value = 'true';
            form.appendChild(input);
            document.body.appendChild(form);
            form.submit();
        }});
    </script>
""", unsafe_allow_html=True)

# Handle theme toggle
if st.button('🌓 Toggle Theme', key='theme_toggle', type='primary'):
    st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'
    st.rerun()

# Motivational quotes
QUOTES = [
    {"text": "The only bad workout is the one that didn't happen.", "author": "Unknown"},
    {"text": "Your body can stand almost anything. It's your mind you have to convince.", "author": "Unknown"},
    {"text": "Weight loss is a journey, not a destination.", "author": "Unknown"},
    {"text": "Success is walking from failure to failure with no loss of enthusiasm.", "author": "Winston Churchill"},
    {"text": "The difference between try and triumph is just a little umph!", "author": "Marvin Phillips"}
]

# Header and quote
st.markdown(f"""
    <div class="header-container">
        <div>
            <h1 class="header-title">🏋️ Weight Management Dashboard</h1>
            <p class="header-subtitle">Your journey to a healthier you starts here!</p>
        </div>
    </div>
    <div class="quote-card">
        <div class="quote-text">"{random.choice(QUOTES)['text']}"</div>
        <div class="quote-author">- {random.choice(QUOTES)['author']}</div>
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
st.markdown(f"""
    <div style='text-align: center; animation: fadeIn 1s ease-in;'>
        <h3>Your Weight Loss Journey</h3>
        <div style='background: {current_theme['secondary_bg']}; border-radius: 10px; padding: 20px; margin: 20px 0;'>
            <p>Starting Weight: 325 lbs → Target Weight: 220 lbs</p>
            <p>Keep pushing forward! Every step counts! 💪</p>
        </div>
    </div>
""", unsafe_allow_html=True)