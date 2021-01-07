FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -U pip setuptools wheel
RUN python -m spacy download en_core_web_sm

COPY . .

CMD ["python", "run.py"]
