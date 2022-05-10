FROM ubuntu:18.04
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip libpq-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]