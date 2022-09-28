# R10521517 鍾慕捷

import streamlit as st
import seaborn as sns 
import matplotlib.pyplot as plt 
import pandas as pd 
import pickle 
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from textblob import TextBlob
from snownlp import SnowNLP
import time


st.title('Sentiment Analyzer')
st.image('InsideOut.png')
st.write('Analyze Your Sentiment From What You Said!')


menu = ['Home', 'About']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Home':
    st.subheader('Home')
    with st.form(key='nlpForm'):
        raw_text = st.text_area('Enter Text Here')
        submit_button = st.form_submit_button(label='Analyze')

        # layout
        if submit_button:
            with st.spinner('Wait for it...'):
                time.sleep(2)
            st.success('Done!')
            st.info('Result')
            s = SnowNLP(raw_text)
            value = s.sentiments
            st.write(value)
