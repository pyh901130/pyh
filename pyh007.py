import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title(':blue[P.yonghun] is back :sunglasses: ')


#plt.figure(figsize=(12,8))

money = pd.read_csv("money_data7.csv")

#st.sidebar.success("Select a demo above.")

# 년도 선택 박스 넣기
import streamlit as st


def  plotting_demo():
        money = pd.read_csv("money_data7.csv")
    option = st.selectbox(
        'How would you like to choice year ?',
        ('2020', '2021', '2022'))

    option2 = int(option)

    st.write('You selected:', option)

    money = money[:] [money['A_YEAR']== option2]

    fig, ax = plt.subplots(2,2, figsize=(12,8))

    plt.subplot(221)
    plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='red' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('america rate')


    plt.subplot(222)
    plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='blue' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('korea rate')

    plt.subplot(223)
    plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('kospi')

    plt.subplot(224)
    plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('house price')

    st.pyplot(fig)
    st.dataframe(money)
    
with st.form(key ='Form1'):
    with st.sidebar:
        
        select_language = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie'))
        
        
if select_language =='line':        
    plotting_demo()   
