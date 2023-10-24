# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if



st.header('2. Radio button')
genre = 

if genre ==  





st.header('3. Checkbox')    # 😄
agree = 
if 


st.header('4. Select box')
option =


st.header('5. Multi select')
options = 





st.header('6. Input: Text/Number')

st.subheader('**_text_input_**')
title =


st.subheader('**_number_input_**')
number = 


st.header('7. Date input')
ymd = 


st.header('8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = 


st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = 


st.subheader('**_년 월 일 사이 구간_**')

slider_date = 






# 년 월 일 시 사이 구간
# slider_time = st.slider(
#     'Select a range of datetime?',
#     datetime(2022, 1, 1, 0, 30), datetime(2022, 12, 31, 0, 30),
#     value=(datetime(2022, 7, 1, 0, 30), datetime(2022, 10, 31, 9, 30)),
#     format='MM/DD/YY - hh:mm')
# st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py