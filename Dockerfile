FROM python:3.8-slim

# 作業ディレクトリを設定
WORKDIR /app

RUN apt update && apt install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt app.py heic_converter.py /app

# 依存関係をインストール
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD streamlit run --server.port 8501 app.py
