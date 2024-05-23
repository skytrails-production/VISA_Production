#!/bin/bash
set -e


echo "Deployment started ..."

# Pull the latest version of the app
echo "Copying New changes...."
git pull origin main
echo "New changes copied to server !"

# Activate Virtual Env
#Syntax:- source virtual_env_name/bin/activate
source env/bin/activate
echo "Virtual env 'env' Activated !"

echo "Clearing Cache..."
python manage.py clean_pyc
python manage.py clear_cache

echo "Installing Dependencies..."
pip install -r requirements.txt 

echo "Serving Static Files..."
python manage.py collectstatic --noinput

echo "Running Database migration..."
python manage.py makemigrations
python manage.py migrate

# Deactivate Virtual Env
deactivate
echo "Virtual env 'env' Deactivated !"

echo "Reloading App..."

echo "Listing all gunicorn processes:"
ps aux | grep gunicorn

echo "Finding gunicorn_visa_project processes:"
ps aux | grep gunicorn_visa_project | grep -v grep


#kill -HUP ps -C gunicorn fch -o pid | head -n 1
# Extract PIDs and send HUP signal
echo "Sending HUP signal to PIDs:"
ps aux |grep gunicorn_visa_project |grep VisaWeb | awk '{ print $2 }' |xargs kill -HUP

echo "Deployment Finished !"