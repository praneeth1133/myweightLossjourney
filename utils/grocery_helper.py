import streamlit as st
from data.sample_meal_plan import MEAL_PLAN

def generate_grocery_list():
    """Generate weekly grocery list from meal plan"""
    grocery_list = {}
    
    # Combine ingredients from all meals
    for meal_info in MEAL_PLAN.values():
        for ingredient, amount in meal_info['ingredients'].items():
            if ingredient in grocery_list:
                # Simple multiplication for weekly amount
                grocery_list[ingredient] = f"{7}x {amount}"
            else:
                grocery_list[ingredient] = f"{7}x {amount}"

    return grocery_list

def display_grocery_list():
    """Display weekly grocery list with estimated prices"""
    st.subheader("Weekly Grocery List")
    
    grocery_list = generate_grocery_list()
    
    # Display grocery items in a clean format
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Item**")
        for item in grocery_list.keys():
            st.write(item)
    
    with col2:
        st.write("**Quantity**")
        for quantity in grocery_list.values():
            st.write(quantity)
    
    with col3:
        st.write("**Estimated Price Range**")
        # Dummy price ranges for demonstration
        for _ in grocery_list:
            st.write("$5-15")
    
    st.info("💡 Tip: Prices are estimated ranges. Check your local stores for actual prices.")
