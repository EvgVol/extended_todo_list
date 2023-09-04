# Extended ToDo list


## Technologies Used
* Django
* Docker
* Nginx
* Django Rest Framework
* PostgreSQL
* Gunicorn

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository using:
```bash
git clone https://github.com/EvgVol/extended_todo_list
```
2. Create a .env file in the root directory of the project.

3. Add the following environment variables to the .env file:
```bash
SECRET_KEY='django-insecure-th0&v=@7m$)i-4jo^9^$i*9f45=ysgksx&p)*-4g=y)q0)-8i%'
DEBUG=True
ALLOWED_HOSTS='127.0.0.1, localhost'
DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
DB_HOST='127.0.0.1'
DB_PORT=5432
```
4. Navigate to the project directory using:
```bash
cd extended_todo_list/app
```
5. Start the Django development server using the following command:
```bash
docker-compose up
```
6. Execute the commands one by one:

```bash
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input
```

The project is now available at http://127.0.0.1/.


## Tests

