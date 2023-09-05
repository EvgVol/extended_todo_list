# Extended ToDo list

## Project Structure

```
.
├── .env                   # Environment variables for the project
├── .gitignore.py          # A list of files and directories to ignore in Git version control
├── docker-compose.yml     # Docker Compose configuration for deployment
├── data                   # Special folder for web server settings
|   └── nginx
└── app
    ├── api                # APP - API
    |   └── ...       
    ├── users              # APP - USERS
    |   └── ...       
    ├── tasks              # APP - TASKS
    |   └── ...
    ├── send_emails        # Email server for token receipt
    |   └── ...
    ├── tests              # A few tests 
    |   └── ...
    ├── app                # Setting up the project
    |   └── ...                   
    ├── Dockerfile         # Dockerfile for building application image
    ├── requirements.txt   # Project dependencies
    ├── manage.py          # Command-line interface for managing the application (migrations, etc) 
    └── pytest.ini         # Configuration file for pytest (testing framework)
```

## Technologies Used
* Python 3.10 or later
* Django 4.2
* Django Rest Framework 3.14
* PostgreSQL 13.0
* PyTest 7.4
* Gunicorn 21.2
* Docker
* Docker Compose
* Nginx

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


7. Sig Up & Auth users 

*The project is designed to authenticate users via a token, which is obtained upon registration and stored in the 'send_emails' folder. To view the email, follow the procedure below:*

* 1. Open a new terminal if the current terminal is busy with "docker-compose up".

* 2. Find the container ID for your backend using the command:
```
docker ps
```
* 3. Locate your container by name, which will likely be in the form <directory_name>_backend_1. Write down its CONTAINER ID.

* 4. Connect to the container with the backend using the container ID:
```bash
docker exec -it <CONTAINER_ID> bash
# Replace <CONTAINER_ID> with the previously found container identifier.
```

* 5. Now you are inside the container. Change to the send_emails directory:
```
cd send_emails
```
* 6. List the files:
```
ls -l
```
* 7. You need to find the last created file with messages. Files created earlier will have older timestamps. Use the cat command to view the contents of the file:
```
cat <email_file_name>
```
* 8. Replace <email_file_name> with the name of the file with the last saved messages.

* 9. Now you can view the message with the registration confirmation code. You can use this code to test the operation of the application in Postman. 

P.S. Don't forget to specify `Beurer` in Value Headers. Something like this:

```bash
Bearer eyJhbGciOiJIUz.eyJ0154513bl90eXBlTA2ODYGkiOiJjNzIwM2UzNiIsInVzZXJfaWQiOjF9.rqXbs3H3tu0V9MLN72I_MdIHkXqFHw
```

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
