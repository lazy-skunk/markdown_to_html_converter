FROM python:3.12

WORKDIR /app

RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["bash"] 