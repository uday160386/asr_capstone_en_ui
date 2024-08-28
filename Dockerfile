FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y ffmpeg curl qemu-system-arm\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./requirements.txt .
COPY ./app .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501"]