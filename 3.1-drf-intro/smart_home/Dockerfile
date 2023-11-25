FROM python:3.10-alpine
WORKDIR src
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 3000
RUN python manage.py migrate
CMD python manage.py runserver 