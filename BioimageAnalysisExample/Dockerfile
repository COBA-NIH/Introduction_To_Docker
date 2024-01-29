FROM python:3.9

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY Dockerfile ./Dockerfile.txt
COPY BioimageAnalysis.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./BioimageAnalysis.py" ]