import streamlit as st

if "meals" not in st.session_state:
    st.session_state.meals = []

#inputting sentence
new_meal = st.text_input("What did you eat?:", key="clear")

#puts latest meal in slot 0 (the top)
if new_meal:
    st.session_state.meals.insert(0, new_meal)


#counter (counts backwards)
mealCounter = len(st.session_state.meals)

#loop that displays the list of meals
for meal in st.session_state.meals:
    st.write("Meal", str(mealCounter), ":", meal)
    mealCounter -= 1