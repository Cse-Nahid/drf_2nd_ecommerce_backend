FROM python:3.12

ENV PYTHONUNBUFFERED 1
RUN mkdir /ecommerce_backend
WORKDIR /ecommerce_backend
COPY . /ecommerce_backend/
RUN pip install -r requirements.txt