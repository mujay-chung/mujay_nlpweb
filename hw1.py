# R10521517 鍾慕捷

import streamlit as st
import matplotlib.pyplot as plt 
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
