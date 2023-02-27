# DJANGO GEO USERS

## Summary
- Create users and save their locations. The saved users locations are displayed on a map and user details are shown when clicking on map pins.



## Installation
- The program uses GeoDjango.  To install the dependencies for GeoDjango install the software according to the operating system you are using.
See the GeoDjango Installation page for more information on this.

```python
https://docs.djangoproject.com/en/2.1/ref/contrib/gis/install/
```  

- PostgreSQL installation
The easiest way to get the program running is by installing Docker and running this command to run PostgreSQL.
The Kartoza version of postgresql is required as there are modifications made so that Geo data can be stored.

```python
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:15-3 
```  

- Install all required libraries by running
```python
pip3 install -r requirements.txt
```

### Run program
- Navigate into directory with manage,py file and run these commands:
```python

python manage.py makemigrations 
python manage.py migrate 
```

- Now create a super user to login with
```python
python manage.py createsuperuser
```

- Start the program by running this command
```python
python manage.py runserver
```

- You can access the program by going into the site local URL:
```python
http://127.0.0.1:8000/
```

- You can access the django admin page and login with the super user:
```python
http://127.0.0.1:8000/admin
```

### Usage
- Create users and locations.  When a user is logged in the user location will be displayed on the map.




## License

[MIT](https://choosealicense.com/licenses/mit/)