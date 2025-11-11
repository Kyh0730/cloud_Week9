FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]# 1. Python 기본 이미지 불러오기
FROM python:3.10

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 로컬 파일 전체 복사 (app.py, templates/, data/ 등)
COPY . .

# 4. 필요한 패키지 설치
RUN pip install -r requirements.txt

# 5. Flask 실행 포트 개방
EXPOSE 5000

# 6. Flask 앱 실행 명령
CMD ["python", "app.py"]
