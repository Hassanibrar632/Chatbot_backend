echo off

:: making migrations
echo make migrations
call python manage.py makemigrations

:: migrate the data
echo migrating the data
call python manage.py migrate

:: Running the server
echo Start the server
call python manage.py runserver

:: Program is closing
echo Closing the process
call pause