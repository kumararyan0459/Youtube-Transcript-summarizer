import pickle
from pathlib import Path
import streamlit as st
import pandas as pd
import pytube as  YouTube
import base64
from io import BytesIO
from transc import get_transcript
import streamlit_authenticator as stauth
# from connect import connect
from transformers import pipeline
# import Registration 

# ----------------------------------------------------------------------------

# def creds_entered():
#     if st.session_state["user"].strip()=="admin" and st.session_state["password"].strip()=="password":
#         st.session_state["authenticated"]= True
    
#     else:
#         st.session_state["authenticated"]= False
#         if not st.session_state["password"]:
#             st.warning("Please enter your password")
#         elif not st.session_state["user"]:
#             st.warning("Please enter your username")
#         else:
#             st.warning("Incorrect username or password ")
            
# def authenticate_user():
#     if "authenticated" not in st.session_state:
#         st.header("Please Authenticate to login")
#         st.text_input(label="Username :",value="", key="user", on_change=creds_entered)
#         st.text_input(label="Password :",value="", key="password",type="password", on_change=creds_entered)
#         st.button("Login")
#         return False
    
#     else:
#         if st.session_state["authenticated"]:
#             return True
#         else:
#             st.text_input(label="Username :",value="",key="user",on_change=creds_entered)
#             st.text_input(label="Password :",value="",key="password",type="password",on_change=creds_entered)
#             st.button("Login")
#             return False
        
            
        
    
# if authenticate_user():
#     st.sidebar.header("Navigation")
#     if st.sidebar.button("Reload Home Page"):
#      st.write("Page Refreshed!!!")

# ----------------------------------------------------------------------------

st.sidebar.header("Navigation")
if st.sidebar.button("Refresh Page"):
    st.write("Page Refreshed!!!")


# ----------------------------------------------------------------------------

st.header(" Video Summarizer 🎬")
st.markdown("<h1 style='text-align: center;>Video Summarizer 🎬</h1>",unsafe_allow_html=True)
st.subheader("Summarize youtube video with a single click!")

full_yt = st.text_input("Enter video link", "")

if st.button("Get Summary"):
    with st.spinner("Summarizing Video..."):
     video_id = full_yt.split("=")[1]
     get_transcript(video_id)
     pass

    progressbar = st.progress(0)
    for prec_complete in range(100):
        progressbar.progress(prec_complete+1)
    # ----------------------------------------------------------------------------

    st.header("Summary")
    with open("ms_kitco.txt", "r") as f:
        tx = f.read()

    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    x3 = summarizer(tx[:4000], max_length=230)

    res = x3[0]["summary_text"]


    # ----------------------------------------------------------------------------
    st.write("Summary:")
    st.write(res)
    st.markdown("""
    <div style="border: 1px solid black; padding: 10px;">
    """, unsafe_allow_html=True)
    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------------------
st.write("Summary:")
option = st.selectbox(
    'Select type of download',
    ('audio', 'highest_resolution', 'lowest_resolution'))

if st.button("Download"):
    if full_yt:
        try:
            video_object = YouTube(full_yt)
            
            st.write("Title of Video: " + video_object.title)
            st.write("Number of Views: " + str(video_object.views))
            
            if option == 'audio':
                stream = video_object.streams.get_audio_only()
                
            elif option == 'highest_resolution':
                stream = video_object.streams.get_highest_resolution()
                
            elif option == 'lowest_resolution':
                stream = video_object.streams.get_lowest_resolution()

            # Download the selected stream
            stream.download()
            st.success("Download completed!")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL.")

if st.button("View"):

    st.video("C:\Users\deves\Downloads")
  # ----------------------------------------------------------------------------

if st.sidebar.button("Contact Us"):
  st.header("Contact Us !!!")
  st.markdown("---")
  st.write("Hey if you want to follow us or having any query")
  st.write("You can contact us diectly using the below links")


  st.button("WhatsApp")
  st.write("https://wa.me/9350734673")
    
  st.button("Instagram")
  st.write("https://www.instagram.com/kumar_aryan_0/")

  st.button("Github")
  st.write("https://github.com/aryankumar007")
  
  #------------------------------------------------------------------------------------------
  
if st.sidebar.button("About Us"):
    st.header("About Us!!!")
    st.write("---")
    st.write("Thanks for showing us the interest of knowing us more. ")
    st.write("We are a group of students from YMCA Faridabad and we made our project on the topic of YouTube Summary Generator.")
    st.write("In our project after providing a YouTube Url ,We will provide you with the summary of the YouTube video that you are looking for.")
    st.write("We hope that you like our project. ")
    st.write("You can know more about us by contacting us.")
    st.write("We are always open to suggestions and feedback.")
    st.write("Thanks!!!")

