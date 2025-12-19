import requests
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from threading import RLock
st.title(':violet[Spend]:red[Sense]')
st.markdown('## Expense Tracker and Visualization App')
st.markdown('Welcome to SpendSense, your personal expense tracker and visualization app! This tool helps you categorize your expenses from SMS transaction messages and provides insightful visualizations to help you manage your finances better.')
st.markdown('Upload your SMS data in string format in Chat Input to categorize and visualize your expenses.')

server_url = 'http://127.0.0.1:8000/predict'


def plot_result(predicted_data: dict):
    pred_data = predicted_data['Prediction']
    prob = np.mean(predicted_data['Probabilities'])
    amounts = predicted_data['amounts']
    masked_sms = predicted_data['Masked_SMS_Text']
    pred_cat = {}
    for cls,amt in zip(pred_data,amounts):
        if cls not in pred_cat:
            pred_cat[cls] = amt
        else:
            pred_cat[cls] += amt
    df = pd.DataFrame({'Category':list(pred_cat.keys()),'Total_Amount':list(pred_cat.values())})
    maps = {
        0:'Food',
        1:'Groceries',
        2:'Travel',
        3:'Medical',
        4:'Bills',
        5: 'Others'
    }
    df['Category'] = df['Category'].map(maps).fillna('Unknown')

    return df, prob,masked_sms



        #st.write(sms_text)

with st.sidebar.markdown('Have sms in a file?'): 
    uploaded_file = st.sidebar.file_uploader("Upload your file here", type=["txt","csv"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith('.txt'):
                content = uploaded_file.read().decode('utf-8')
                ls_sms_messages = [content]
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                if 'sms_text' in df.columns:
                    ls_sms_messages = df['sms_text'].to_list()
                else:
                    st.sidebar.error("CSV file must contain 'sms_text' column.")
                    ls_sms_messages = []
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")
            ls_sms_messages = []

if sms_text := st.chat_input('Enter your SMS message(s) here'):
    if ',' in sms_text:
        ls_sms_messages = [i.strip() for i in sms_text.split(',')]
    # if we only want to categorize the single sms (input).
    elif isinstance(sms_text,str)  and (not sms_text.startswith('[') and not sms_text.endswith(']')):
        ls_sms_messages = [sms_text]
    #elif isinstance(sms_text,list):
    #    ls_sms_messages = [ for]
    else:
        st.error('For chat Input only string is supported.eg: "sms_text1" or "sms_text1","sms_text2" ')



try:
    if ls_sms_messages:
        #st.matkdown(type(ls_sms_messages))
        send_data = {'sms_text': ls_sms_messages}
    response = requests.post(server_url,json=send_data)
    response_data = response.json()
    df, avg_prob,masked_sms = plot_result(response_data)
    st.dataframe({'Masked_SMS_Text': masked_sms})
    st.markdown('### Spend Category Summary')
    st.dataframe(df)
    st.markdown('### Expense Chart Overview')
    _lock = RLock()
    with _lock:
        fig,ax = plt.subplots()
        ax.pie(df['Total_Amount'],labels=df['Category'],autopct='%1.1f%%',startangle=140)
        st.pyplot(fig)        
    st.markdown(f'### Average Prediction Confidence: {avg_prob:.2f}')

    
except:
    st.markdown("SpendSense Accepts SMS Transcation Via Chat Input or File Upload (TXT/CSV).')")
    send_data = None





