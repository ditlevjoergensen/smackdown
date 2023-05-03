import streamlit as st
import pandas as pd
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Smackdown", page_icon="🍺")
# Paths
#current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = Path.cwd() / "styles" / "style.css"
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()



# Styles
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ---------------- images
mj_alexander_image_file = current_dir.parent / "images" / "mj_alexander.jpg"
mj_andreas_image_file = current_dir.parent / "images" / "mj_andreas.jpg"
mj_ditlev_image_file = current_dir.parent / "images" / "mj_ditlev.jpg"
mj_jonas_image_file = current_dir.parent / "images" / "mj_jonas.jpg"
mj_rene_image_file = current_dir.parent / "images" / "mj_Rene2.jpg"

mj_alexander_image = Image.open(mj_alexander_image_file)
mj_andreas_image = Image.open(mj_andreas_image_file)
mj_ditlev_image = Image.open(mj_ditlev_image_file)
mj_jonas_image = Image.open(mj_jonas_image_file)
mj_rene_image = Image.open(mj_rene_image_file)

st.title("Årets Deltagere")

col1, col2 = st.columns(2)

with col1:
    st.image(mj_alexander_image, caption="Ridder Alexander den Vilde")
    st.image(mj_andreas_image, caption="Ridder Andreas den Galante")
    st.image(mj_jonas_image, caption="Ridder Jonas den Stærke")

with col2:
    st.image(mj_rene_image, caption="Ridder René den Modige")
    st.image(mj_ditlev_image, caption="Ridder Ditlev den Kloge")