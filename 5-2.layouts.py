import streamlit as st
st.caption('참조사이트: https://docs.streamlit.io/library/get-started/multipage-apps/create-a-multipage-app')

# 페이지 선언 (🎈 ❄️ 🎉)
def main_page():


def page2():


def page3():


    
# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, 'Page 2': page2, 'Page 3': page3}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox(                   )

# 해당 페이지 부르기
page_names_to_funcs[            ]()

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\5-2.layouts.py