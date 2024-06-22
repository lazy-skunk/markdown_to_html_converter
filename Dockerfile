FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y bash

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash"]
