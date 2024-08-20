import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Projects", "Contact"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Main content based on selection
if selected == "Home":
    st.title(f"You have selected {selected}")
    st.header('Propertydata.lv dashboard')
    st.markdown('Some markdown text goes here')

    # Create two columns
    column1, column2 = st.columns(2)

    # Populate first column
    with column1:
        st.write("First column content")

    # Populate second column with a bar chart
    with column2:
        chart_data = pd.DataFrame(np.random.randn(60, 3), columns=["a", "b", "c"])
        st.bar_chart(chart_data)

