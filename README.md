# DJANGO GEO USERS

## Summary
- Create users and save their locations. The saved users locations are displayed on a map and user details are shown when clicking on map pins.


## Requirements
- Docker


## Installation and Running the program
- In your terminal navigate into the program root folder with the docker-compose.yml file in it

```python
docker-compose up
```

- Access the program via URL: http://127.0.0.1:8000/


### Access django admin
- Access the django container by using

docker ps -a 

- This will show a list of containers. Get the container ID.
- A example of a contaner id is: 355efa8c36c2

- Access the container with this command (Replace with own container ID):
```python
geousers % docker exec -it 355efa8c36c2 /bin/bash
```

- Now create a super user to login with
```python
python manage.py createsuperuser
```

- Exit the contaner
```python
exit
```

-  To Access django admin go to url: http://127.0.0.1:8000/admin/





## License

[MIT](https://choosealicense.com/licenses/mit/)