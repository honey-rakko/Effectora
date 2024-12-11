import streamlit as st

# 제목과 텍스트 출력
st.title("Streamlit 기본 예제")
st.write("Streamlit 설치 및 실행 성공!")

# 사용자 입력받기
user_input = st.text_input("검색어를 입력하세요:")
if user_input:
    st.write(f"'{user_input}'를 검색하셨습니다.")

# 간단한 데이터 시각화
import pandas as pd
import numpy as np
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["A", "B", "C"]
)
st.line_chart(data)
