import streamlit as st
import base64
from pathlib import Path

# Lørdag 13 maj kl 10:00
st.set_page_config(page_title="Smackdown", page_icon="🍺")

# Helper Functions
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


# Paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
background = current_dir / "images" / "silkeborg.jpg"


# Variables


# Styles
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


#Page
set_background(background)

st.title("SMACKDOWN")
st.title("2023")
st.title("SURVIVAL")
st.title("EDITION")




