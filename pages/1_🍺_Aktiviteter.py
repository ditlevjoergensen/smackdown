import streamlit as st
import pandas as pd
from pathlib import Path
st.set_page_config(page_title="Smackdown", page_icon="🍺")
# Paths
#current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = Path.cwd() / "styles" / "style.css"


# Variables
def color_coding(row):

    if row.Activity == "Åbningscermoni Tusindfryd 141":
        return ['background-color:purple'] * len(row)
    
    if row.Activity in ("Kano", "Frokost", "Alex Optagelse"):
        return ['background-color:green'] * len(row)

    if row.Activity == "Aftensmad på Tusindfryd 141":
        return ['background-color:teal'] * len(row)

    if row.Activity in ("Bowl & Fun","Bodega Fun"):
        return ['background-color:orange'] * len(row)

    if row.Activity == "Tak for i dag":
        return ['background-color:red'] * len(row)


# Styles
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

dict = {"Tid": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"
                , "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"], 
        "Activity": ["Åbningscermoni Tusindfryd 141", "Transport til Kano","Kano","Frokost","Alex Optagelse","Kano","Kano",
                     "Aftensmad på Tusindfryd 141","Aftensmad på Tusindfryd 141","Aftensmad på Tusindfryd 141",
                     "Bowl & Fun","Bowl & Fun","Bodega Fun","Bodega Fun","Tak for i dag"]}

df = pd.DataFrame.from_dict(dict,orient='columns')

st.title("Aktiviteter")
st.table(df.style.apply(color_coding, axis=1))
#st.table(df)

st.title("Pakkeliste")

dict = {"Pakkeliste": ["Badetøj", "Håndklæde","Sovepose/Dyne","Lagen","Udendørs tøj til kano","Udendørs sko til kano"]}

df = pd.DataFrame.from_dict(dict,orient='columns')

st.table(df)
