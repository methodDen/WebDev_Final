#!/bin/sh


if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

#echo "Flush database"
#python manage.py flush --no-input
echo "Make migrations"
python manage.py makemigrations
echo "Apply migrations"
python manage.py migrate

exec "$@"