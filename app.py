import cloudinary
import cloudinary.api
import os
import streamlit as st
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Cloudinary 설정
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Cloudinary 파일 검색 함수
def search_audio_files(query):
    try:
        # 'query'로 시작하는 모든 파일 검색 (video는 오디오 포함)
        results = cloudinary.api.resources(type="upload", prefix=query, resource_type="video")
        if 'resources' in results:
            # 파일 URL 반환
            return [
                {"name": file["public_id"], "url": file["secure_url"]}
                for file in results["resources"]
            ]
        return []  # 검색 결과가 없을 경우 빈 리스트 반환
    except Exception as e:
        st.error(f"파일 검색 중 오류 발생: {e}")
        return []

# Streamlit UI
st.set_page_config(page_title="Effectora", page_icon="🔊")
st.title("Effectora")

# 사용자 입력 받기
user_input = st.text_input("찾고 싶은 효과음을 검색하세요:")

if user_input:
    st.write(f"'{user_input}'를 검색하셨습니다.")
    audio_files = search_audio_files(user_input)

    if audio_files:
        for audio in audio_files:
            st.write(f"파일 이름: {audio['name']}")
            st.audio(audio['url'], format="audio/mp3")  # 재생 버튼 표시
    else:
        st.warning("검색 결과가 없습니다.")
