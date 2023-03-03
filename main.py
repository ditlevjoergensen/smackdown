import streamlit as st
import datetime
import asyncio
import base64

# Lørdag 13 maj kl 10:00
st.set_page_config(page_title="Smackdown", layout="wide")

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







# Variables
smackdown_start = datetime.datetime(year=2023,day=13,month=5, hour=10, minute=0)


#Page
set_background('images/silkeborg.jpg')
st.markdown(
    """
    <style>
    .time {
        font-size: 130px !important;
        font-weight: 700 !important;
        color: #ec5953 !important;
        text-align: center;
    }
    </style>
    
    """,
    unsafe_allow_html=True
)

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

