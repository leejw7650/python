import streamlit as st
import pandas as pd
from datetime import datetime  

st.header('날짜 구간으로 데이터 조회하기')

# streamlit\data_subway_in_seoul.csv  
# 한글 encoding='cp949' 추가하여 읽어오고 확인하기 
df = 
# 날짜 필드의 데이터 형식 확인하기
st.write('날짜 필드 형식: ',  )
# 데이터프레임 내용 확인하기


# 날짜 컬럼을 string에서 datetime으로 변환하기

# 날짜 필드의 데이터 형식 확인하기
st.write('날짜 필드 형식: ',  )
# 데이터프레임 내용 확인하기


# slider를 사용하여 날짜 구간 설정하기
slider_date =    (
    '날짜 구간을 선택하세요 ',
                                               # 날짜 전체 구간 : 2021.1.1~2021.12.31
                                               # 초기 설정 구간 : 2021.7.1~2021.7.31
                     )                         # 날짜 형식: YY/MM/DD

# slider_date의 구간 날짜 확인하기


# slider_date의 선택된 시작, 종료 날짜를 start_date, end_date에 저장하기
start_date = 
end_date = 

# slider 날짜 구간으로 df를 읽어서 새 sel_df 으로 저장하고 확인하기
sel_df = 



# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-2.input.py