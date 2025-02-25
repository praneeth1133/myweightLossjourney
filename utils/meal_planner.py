from datetime import datetime, timedelta
import streamlit as st
from data.sample_meal_plan import MEAL_PLAN

def calculate_daily_calories():
    """Calculate total daily calories from meal plan"""
    return sum(meal["calories"] for meal in MEAL_PLAN.values())

def get_next_meal():
    """Get the next upcoming meal based on current time"""
    current_time = datetime.now()
    for meal_name, meal_info in MEAL_PLAN.items():
        meal_time = datetime.strptime(meal_info["time"], "%H:%M").time()
        meal_datetime = datetime.combine(datetime.today(), meal_time)
        if meal_datetime > current_time:
            return meal_name, meal_info
    return None, None

def display_meal_plan():
    """Display the daily meal plan"""
    st.subheader("Today's Meal Plan")
    
    total_calories = calculate_daily_calories()
    
    # Display total calories
    st.metric("Total Daily Calories", f"{total_calories} kcal")
    
    # Display each meal in an expandable section
    for meal_name, meal_info in MEAL_PLAN.items():
        with st.expander(f"{meal_name} - {meal_info['time']} ({meal_info['calories']} kcal)"):
            st.write(f"**Meal:** {meal_info['meal']}")
            st.write("**Ingredients:**")
            for ingredient, amount in meal_info['ingredients'].items():
                st.write(f"- {ingredient}: {amount}")

def setup_meal_notifications():
    """Setup browser notifications for meals"""
    st.subheader("Meal Reminders")
    
    # JavaScript for notifications
    notification_js = """
    <script>
    function requestNotificationPermission() {
        if (!("Notification" in window)) {
            alert("This browser does not support desktop notifications");
        } else {
            Notification.requestPermission();
        }
    }
    </script>
    """
    
    st.components.v1.html(notification_js, height=0)
    
    if st.button("Enable Meal Reminders"):
        st.write("Notifications enabled! You'll receive reminders 1 hour before each meal.")
