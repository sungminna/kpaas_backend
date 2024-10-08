FROM python:3
LABEL authors="sungm"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "usr.asgi:application"]