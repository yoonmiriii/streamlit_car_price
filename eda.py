import streamlit as st
import pandas as pd


def run_eda() :
    st.subheader('탐색적 데이터 분석')

    st.text('데이터프레임 보기 / 통계치 보기를 할 수 있습니다.')

    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    print(df)

    radio_menu = ['데이터 프레임', '통계치']
    
    choice_radio = st.radio('선택하세요.', radio_menu)

    if choice_radio == radio_menu[0] :
        st.dataframe(df.head())
    elif choice_radio == radio_menu[1] :
        st.dataframe(df.describe())

    # 각 컬럼별로 최대/최소 값을 보여주는 화면 개발.
    # 유저가 컬럼을 선택하면, 해당 컬럼의 최대/최소 데이터를 보여주도록 하자.
    
    st.text('컬럼을 선택하면, 각 컬럼별 최대/최소 데이터를 보여드립니다.')
    column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    choice_column = st.selectbox('컬럼을 선택하세요', column_list)

    st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].max(), ])

    st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')
    st.dataframe(df.loc[df[choice_column] == df[choice_column].min(), ])

    st.subheader('상관관계 분석')
    st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 상관계수를 보여드립니다.')



