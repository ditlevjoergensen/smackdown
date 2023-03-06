import streamlit as st
import asyncio
import datetime
from pathlib import Path
import base64

#Variables
smackdown_start = datetime.datetime(year=2023,day=13,month=5, hour=10, minute=0)
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
#current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = Path.cwd() / "styles" / "style.css"
background = Path.cwd() / "images" / "silkeborg.jpg"


# Variables


# Styles
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

st.markdown(
            f"""
            <p class="title">
                COUNTDOWN
            </p>
            """, unsafe_allow_html=True)

#Page
set_background(background)
# Countdown Timer
async def watch(test):
    while True:
        time_left_till_smackdown = smackdown_start-datetime.datetime.now()
        s = time_left_till_smackdown // datetime.timedelta(seconds=1)
        days, remainder_hours = divmod(s, 3600*24)
        hours, remainder = divmod(remainder_hours, 3600)
        minutes, seconds = divmod(remainder, 60)

        test.markdown(
            f"""
            <p class="time">
                {'{:02}:{:02}:{:02}:{:02}'.format(int(days), int(hours), int(minutes), int(seconds))}
            </p>
            """, unsafe_allow_html=True)
        r = await asyncio.sleep(0.2)

test = st.empty()

asyncio.run(watch(test))