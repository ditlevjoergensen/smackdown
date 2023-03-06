import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(page_title="Smackdown", page_icon="🍺")
# Paths
#current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = Path.cwd() / "styles" / "style.css"


# Variables


# Styles
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

dict = {"Tid": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"
                , "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"], 
        "Activity": ["Ankomst", "","","","","","","","Alex Optagelse","","","","","",""]}

df = pd.DataFrame.from_dict(dict,orient='columns')

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.markdown(
            f"""
            <p class="title">
                ACTIVITIES
            </p>
            """, unsafe_allow_html=True)

st.table(df)