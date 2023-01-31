# CashApp
Simple app for balance management.

# Install locally
### Activate your venv:
```
> python -m venv venv && source venv/bin/activate
```
### Install dependencies
```
> pip install -r requirements.txt
```
### Run migrations and start server
```
> python manage.py migrate
> python manage.py runserver
```

# Deploy with Docker
### Create .env file with production ready variables
```
> copy .env.example .env
```
And change default variables.

### Build docker containers
```
> docker-compose build
```

### Run containers in the background
```
> docker-compose up -d
```
This will start the server on port 8000 (default).

### Run migrate if needed
```
> docker-compose exec server python manage.py migrate
```
