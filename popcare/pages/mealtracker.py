from ast import Pass
from queue import Empty
import streamlit as st

st.write("Welcome to the Meal Tracker! Here, you can input your meal and receive the relevant nutrition data.")

class Today:
    def __init__(self):
        self.todays_cals = 0
        self.todays_protein = 0

    def addcals(self, calsfrommeal):
        self.todays_cals += calsfrommeal

    def addprotein(self, proteinfrommeal):
        self.todays_protein += proteinfrommeal

Day1 = Today()

cal_goal = 2000
protein_goal = 100

calories_placeholder = st.empty()
calories_W_placeholder = st.empty()
calories_placeholder.write(f"Total Calories Today: {Day1.todays_cals}/{cal_goal}")

protein_placeholder = st.empty()
protein_W_placeholder = st.empty()
protein_placeholder.write(f"Total Protein Today: {Day1.todays_protein}/{protein_goal}")

# meal registry format is 'meal' : [calories, protein(grams), [ingredients]]

meal_registry = {'mac and cheese':[300, 2, ['cheese', 'mac']], \
                 'pizza':[150, 3, ['cheese', 'tomato', 'dough']], \
                 'cake':[1000, 5, ['flour','egg','milk']], \
                 'beans':[500, 7, ['beans']], \
                 'salad': [200, 3,['lettuce, tomato, ceasar dressing']], \
                 'apple': [95, 0, ['apple']], \
                 'cranberries': [46, 0, ['cranberries']]
                 }

try:
    for meal in st.session_state.meals:
        if meal in meal_registry:
            st.write("----------")
            st.write("MEAL =", meal)
            st.write("calories =", meal_registry[meal][0])
            Day1.addcals(meal_registry[meal][0])
            st.write("protein (grams) =", meal_registry[meal][1])
            Day1.addprotein(meal_registry[meal][1])
            st.write("ingredients =", meal_registry[meal][2])

            calories_placeholder.write(f"Total Calories Today: {Day1.todays_cals}/{cal_goal}")
            if Day1.todays_cals >= cal_goal:
                calories_W_placeholder.write("WOOOOOOO Cal Goal MET")

            protein_placeholder.write(f"Total Protein Today: {Day1.todays_protein}/{protein_goal}")
            if Day1.todays_protein >= protein_goal:
                protein_W_placeholder.write("WOOOOOOO Protein Goal MET")

        else:
            st.write("sorry this isn't in our registry")
except:
    "No Meals Today"
