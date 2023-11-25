FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3000

CMD [ "python", "manage.py", "runserver" ]