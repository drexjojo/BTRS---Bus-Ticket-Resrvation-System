Initial configurations

mysql
drop database bus_reservation
create database bus_reservation
python2 manage.py makemigrations
python2 manage.py migrate
mysql -u root bus_reservation < seed.sql
(from Database folder)

Run

python2 manage.py runserver

