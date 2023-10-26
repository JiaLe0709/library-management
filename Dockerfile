FROM python:3.12
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
WORKDIR /app
CMD [ "gunicorn", "--chdir", "app", "app:app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:5000"]