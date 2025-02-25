# Weight Management Dashboard

A comprehensive weight management and wellness dashboard that empowers health-conscious individuals with personalized tracking, interactive insights, and motivational tools.

## Features
- Daily meal planning with calorie tracking
- Weight progress visualization
- Grocery list generation with Excel export
- Motivational quotes
- Light/Dark theme support

## Setup Instructions

1. Install dependencies:
```bash
pip install streamlit pandas plotly openpyxl
```

2. Run the application:
```bash
streamlit run main.py
```

## Deployment
This application can be deployed on Streamlit Community Cloud:
1. Fork this repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Deploy using your forked repository

## Using as a Mobile App
1. Deploy the app on Streamlit Community Cloud
2. On your Android phone:
   - Open Chrome browser
   - Visit your app's URL
   - Tap menu (3 dots)
   - Select "Add to Home Screen"
   - The app will appear as an icon on your home screen

## Project Structure
- `main.py`: Main application file
- `utils/`: Utility functions
  - `meal_planner.py`: Meal planning functionality
  - `weight_tracker.py`: Weight tracking and visualization
  - `grocery_helper.py`: Grocery list management
- `data/`: Data files
  - `sample_meal_plan.py`: Sample meal plan data
