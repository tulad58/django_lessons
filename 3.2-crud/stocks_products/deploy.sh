#!/bin/bash

cd /home/vlad/django_lessons/3.2-crud/stocks_products
git pull 
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
sudo systemctl restart gunicorn
