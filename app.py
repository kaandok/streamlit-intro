import streamlit as st
import pandas as pd
import numpy as np

st.title('My First Streamlit App')
st.write("Hello World!!!")

# Add a slider to your app:
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Add a text input:
name = st.text_input('Name')
st.write('Your name is', name)

data = pd.DataFrame({'numbers': [1, 2, 3, 4, 5], 'squares': [1, 4, 9, 16, 25]})
st.write(data)

st.table(data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

import matplotlib.pyplot as plt

# Plotting with Matplotlib:
fig, ax = plt.subplots()
ax.plot(data['numbers'], data['squares'])
st.pyplot(fig)

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")