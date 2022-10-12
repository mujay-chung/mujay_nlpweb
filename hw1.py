'''
R10521517 鍾慕捷
NLP and Web Applications hw1
'''

import streamlit as st
import time
from snownlp import SnowNLP
from ckiptagger import WS, POS, NER
import requests
from bs4 import BeautifulSoup


# crawl function
def crawl(keyword, num_of_paragraphs):
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

    output = ''
    output_ls = []

    n = 0
    while n < num_of_paragraphs:
        web = requests.get(url, cookies={'over18':'1'})
        soup = BeautifulSoup(web.text, 'html.parser')
        titles = soup.find_all('div', class_='title')

        # store titles
        for i in titles:
            if i.find('a') != None and (keyword in i.find('a').get_text()):
                if n < num_of_paragraphs:
                    output += i.find('a').get_text() + '\n' + url + i.find('a')['href'] + '\n\n'
                    output_ls.append(i.find('a').get_text())
                    n += 1
        
        # to next page
        btn = soup.select('div.btn-group > a')
        up_page_href = btn[3]['href']
        next_page_url = 'https://www.ptt.cc' + up_page_href
        url = next_page_url

    return output_ls, output

# download data
# from ckiptagger import data_utils
# data_utils.download_data_gdown("./")
ws = WS("./data")
pos = POS("./data")
ner = NER("./data")

# streamlit arrange
st.title('PTT Gossiping Search Engine')

menu = ['Sentiment Analysis', 'NLP Pipeline']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Sentiment Analysis':
    st.write('Sentiment Analysis')
    with st.form(key='nlpForm'):
        keyword = st.text_area('Enter Your Keyword Here')
        submit_button = st.form_submit_button(label='Analyze')

        if submit_button:
            with st.spinner('Wait for it...'):
                output_ls, output = crawl(keyword=keyword, num_of_paragraphs=10)
                values = []
                for t in output_ls:
                    values.append(SnowNLP(t).sentiments)
                ave = sum(values) / len(output_ls)
            st.success('Done!')
            st.info('Result')
            st.write('Average Sentiment = {:.2f}'.format(ave))
            for i in range(len(output_ls)):
                st.write('{} : sentiment={:.2f}'.format(output_ls[i], values[i]))

elif choice == 'NLP Pipeline':
    st.write('NLP Pipeline')
    with st.form(key='nlpForm'):
        keyword = st.text_area('Enter Your Keyword Here')
        submit_button = st.form_submit_button(label='Analyze')

        if submit_button:
            with st.spinner('Wait for it...'):
                output_ls, output = crawl(keyword=keyword, num_of_paragraphs=1)
                text = output_ls[0]
                ws_results = ws([text]) # 斷詞
                pos_results = pos(ws_results) # 詞性標記
                # ner_results = ner(ws_results, pos_results) # 命名實體識別
            st.success('Done!')
            st.info('Result')
            st.write(text)
            st.write('斷詞分析')
            st.write(ws_results)
            st.write('詞性標記')
            st.write(pos_results)