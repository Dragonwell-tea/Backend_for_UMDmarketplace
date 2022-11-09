FROM python:3

RUN mkdir /app
WORKDIR /app

RUN pip install --no-cache-dir --quiet --upgrade \
    pip \
    setuptools \
    wheel

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --quiet --upgrade \
    -r ./requirements.txt

COPY . .
ENV FLASK_DEBUG=1
ENV FLASK_APP=app/__init__.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]