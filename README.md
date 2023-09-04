# Extended ToDo list

## Project Structure

```
.
├── .env                   # Environment variables for the project
├── .gitignore.py          # A list of files and directories to ignore in Git version control
├── docker-compose.yml     # Docker Compose configuration for deployment
└── app
    ├── api                # APP - API
    |   └── ...       
    ├── users              # APP - USERS
    |   └── ...       
    ├── tasks              # APP - TASKS
    |   └── ...
    ├── send_emails        # email server for token receipt
    |   └── ...
    ├── tests              # A few tests 
    |   └── ...             
    ├── Dockerfile         # Dockerfile for building application image
    ├── requirements.txt   # Project dependencies
    ├── manage.py          # Command-line interface for managing the application (migrations, etc) 
    ├── pytest.ini         # Configuration file for pytest (testing framework)


## Technologies Used
* Python 3.10 or later
* Django
* Docker
* Docker Compose
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
DB_HOST='db'
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
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```

The project is now available at http://127.0.0.1/.


## Tests

1. Ensure that the Docker containers are running. If they aren't, start them by running the following command from the extended_todo_list/app directory:
```bash
docker-compose up
```

2. Run the tests using the following command:
```bash
docker-compose exec backend pytest
```

3. Once the tests are complete, you should see the test results output in the terminal.

## Contributing

If you have any questions, suggestions, requests, or comments, please feel free to open [issues or pull requests](https://github.com/EvgVol/extended_todo_list/issues) in this repository.
