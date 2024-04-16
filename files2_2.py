import streamlit as st
import pandas as pd

# let's see how we will load Products.csv file present in streamlit folder.

st.subheader('Uploading the CSV file')
# there are 2 ways of doing it and the first one is:

# first way:
df = st.file_uploader('Upload the csv file: ',type=['csv','xlsx'])

st.header('Loading the CSV File')

if df is not None:
    st.dataframe(df)


# Second Way: 

# displaying the above data in csv format and for that we are using pandas.

df2 = pd.read_csv('Products.csv')
# st.table(df2.head())

if df2 is not None:
    st.table(df2.head())

# Combining the above 2 ways: 

df3 = st.file_uploader('Upload the file here: ',type=['csv','xlsx'])
if df3 is not None:
    data = pd.read_csv(df3)
    if data is not None:
        st.table(data.head())


st.subheader('Dealing with Images: ')

# first Way:

# st.image('Streamlit/img.png')

# Second Way: 
img = st.file_uploader('Upload the image Here: ',type=['jpeg','png'])

if img is not None:
    st.image(img)


st.header('wkrking with videos: ')

# first way: 
# st.video('Streamlit/song.mp3')

# second way:
vid = st.file_uploader('upload the video file here: ',type=['mp3','mkv','mp4'])

if(vid is not None):
    st.video(vid,start_time=60)


st.subheader('Working with Audio files: ')
# st.audio('Streamlit/song.mp3')

aud = st.file_uploader('Upload Audio file Here: ',type=['mp3','mp4'])
if aud is not None:
    st.audio(aud.read())

