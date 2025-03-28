
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import requests

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiemail(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()




# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")


# ---- LOAD ASSETS ----
lottie_mail = load_lottiemail("https://lottie.host/4b2a2dd7-decf-4def-9299-0134d740ca39/89n9CeLaZZ.json")
lottie_coding = load_lottieurl("https://lottie.host/e564a336-69ba-43a8-8d74-12e4137c8931/uqsx8KUEEX.json")
img_contact_form = Image.open("mymage.jpg")
img_lottie_animation = Image.open("myimage.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Kenula :wave:")
    st.title("A Data Analyst From Sri Lanka")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I Can Recommend A Youtube channel To who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!

    contact_form = """
    <form action="https://formsubmit.co/kenulasadew07@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_mail,height=400,key="mail")



# Streamlit Page Configuration


# Sign-In Section
with st.container():
    st.write("---")
    st.header("To Sign in!")
    st.write("##")
    sign_in_form = """
      <form action="https://formsubmit.co/kenulasadew07@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="email" name="email" placeholder="Your email" required>
        <input type="text" name="password" placeholder="Your password" required>
        <input type="text" name="password" placeholder="Conform Your password" required>
        <button type="submit">Sign in</button>
    </form>


"""
    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(sign_in_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
       



