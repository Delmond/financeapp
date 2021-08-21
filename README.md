# Financal App

This is an small app written in django that's used as a skill showcase. It's main functionality is querying the yahoo finance rss feed for financial using a particular symbol which it stores for later viewing.
## Features

- Contains  a RESTful CRUD API
- Usees pagination to browse list endpoints
- Scrapes Yahoo finance RSS in periodic intervals
- Stores data in a Postgres database
- Has documentation in OpenAPI, Swagger UI or redocs forms
- App is containared in docker and set-up using docker compose

## Installation
You need to have docker and docker-compose installed to run this app, after cloning it's sufficient to run the following command in the project root folder:
```sh
docker-compose build
```
## Running 
Achieved using the following command:
```sh
docker-compose run
````

## Dependencies
The application uses the following packages:
- django - as a python backend framework
- django rest framework - for easier handling of the RESTful API
- celery - for task execution
- feedparser - to fetch and parse rss feeds
- drf-spectacular - for the construction of the API docs


## Documentation
Start the app and go to the following routes for documentation:
- \docs - OpenAPI documentation
- \docs\swagger-ui - Browsable and Executable API
- \docs\redocs - Same as Swagger but with different look

## Testing
To run the tests simply run the following command:
```sh
docker-compose run backend ./manage.py tests
```

