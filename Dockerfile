FROM python:3.12

WORKDIR /mnt/markdown_to_html_converter

RUN apt-get update &&\
    apt-get install -y bash

COPY requirements.txt .
RUN pip install --upgrade pip &&\
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["bash"] 