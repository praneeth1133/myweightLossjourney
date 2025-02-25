import streamlit as st
import pandas as pd
from data.sample_meal_plan import MEAL_PLAN
from io import BytesIO

# Define measurement units and conversions
INGREDIENT_UNITS = {
    'Oatmeal': {'unit': 'lbs', 'conversion': 0.0625},  # 1 cup = 0.0625 lbs
    'Mixed berries': {'unit': 'lbs', 'conversion': 0.3125},  # 1 cup = 0.3125 lbs
    'Almonds': {'unit': 'lbs', 'conversion': 0.0625},  # 1 oz = 0.0625 lbs
    'Honey': {'unit': 'fl oz', 'conversion': 0.17},  # 1 tsp = 0.17 fl oz
    'Chicken breast': {'unit': 'lbs', 'conversion': 0.0625},  # 1 oz = 0.0625 lbs
    'Mixed greens': {'unit': 'lbs', 'conversion': 0.125},  # 1 cup = 0.125 lbs
    'Olive oil': {'unit': 'fl oz', 'conversion': 0.5},  # 1 tbsp = 0.5 fl oz
    'Cherry tomatoes': {'unit': 'lbs', 'conversion': 0.3125},  # 1 cup = 0.3125 lbs
    'Salmon fillet': {'unit': 'lbs', 'conversion': 0.0625},  # 1 oz = 0.0625 lbs
    'Broccoli': {'unit': 'lbs', 'conversion': 0.15},  # 1 cup = 0.15 lbs
    'Brown rice': {'unit': 'lbs', 'conversion': 0.5},  # 1 cup = 0.5 lbs
    'Lemon': {'unit': 'pieces', 'conversion': 1},  # 1 piece = 1 piece
    'Apple': {'unit': 'pieces', 'conversion': 1},  # 1 medium = 1 piece
    'Peanut butter': {'unit': 'fl oz', 'conversion': 1}  # 1 tbsp = 0.5 fl oz
}

def convert_to_standard_unit(ingredient, amount):
    """Convert ingredient amounts to standard units"""
    # Extract numeric value and unit from amount string
    import re
    numeric = float(re.findall(r'[\d.]+', amount)[0])

    if ingredient in INGREDIENT_UNITS:
        conversion = INGREDIENT_UNITS[ingredient]['conversion']
        unit = INGREDIENT_UNITS[ingredient]['unit']
        converted_amount = numeric * conversion
        return f"{converted_amount:.2f} {unit}"
    return amount

def generate_grocery_list():
    """Generate weekly grocery list with both original and standardized units"""
    grocery_list = {}
    original_quantities = {}

    # Combine ingredients from all meals
    for meal_info in MEAL_PLAN.values():
        for ingredient, amount in meal_info['ingredients'].items():
            weekly_amount = convert_to_standard_unit(ingredient, amount)
            daily_amount = amount

            if ingredient in grocery_list:
                # Extract numeric value for weekly calculation
                current = float(grocery_list[ingredient].split()[0])
                new = float(weekly_amount.split()[0])
                unit = weekly_amount.split()[1]
                grocery_list[ingredient] = f"{(current + new) * 7:.2f} {unit}"
                original_quantities[ingredient] = f"{7}x {daily_amount}"
            else:
                # Initialize with weekly amount
                numeric = float(weekly_amount.split()[0])
                unit = weekly_amount.split()[1]
                grocery_list[ingredient] = f"{numeric * 7:.2f} {unit}"
                original_quantities[ingredient] = f"{7}x {daily_amount}"

    return grocery_list, original_quantities

def export_to_excel():
    """Generate Excel file for grocery list"""
    grocery_list, original_quantities = generate_grocery_list()

    df = pd.DataFrame({
        'Item': grocery_list.keys(),
        'Recipe Quantity': original_quantities.values(),
        'Total Quantity (Standard Units)': grocery_list.values(),
        'Estimated Price Range': ['$5-15' for _ in grocery_list]
    })

    # Create Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Grocery List')

    return output.getvalue()

def display_grocery_list():
    """Display weekly grocery list with both original and standardized units"""
    st.subheader("Weekly Grocery List")

    grocery_list, original_quantities = generate_grocery_list()

    # Create a DataFrame for better display
    df = pd.DataFrame({
        'Item': grocery_list.keys(),
        'Recipe Quantity': original_quantities.values(),
        'Total Quantity (Standard Units)': grocery_list.values(),
        'Estimated Price Range': ['$5-15' for _ in grocery_list]  # Placeholder prices
    })

    # Display the DataFrame
    st.dataframe(
        df,
        hide_index=True,
        column_config={
            'Item': st.column_config.TextColumn('Item'),
            'Recipe Quantity': st.column_config.TextColumn('Recipe Quantity'),
            'Total Quantity (Standard Units)': st.column_config.TextColumn('Total Quantity (Standard Units)'),
            'Estimated Price Range': st.column_config.TextColumn('Estimated Price Range')
        }
    )

    # Excel export button
    excel_file = export_to_excel()
    st.download_button(
        label="📥 Download Grocery List as Excel",
        data=excel_file,
        file_name="weekly_grocery_list.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.info("💡 Tip: Standard units are in pounds (lbs), fluid ounces (fl oz), or pieces")