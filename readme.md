## prereqs: 
1. make sure docker is running
1. make sure you have an internet connection

## useful commands:

1. run the backend: 
docker-compose up --build

1. run other commands inside the container:
docker-compose exec web python manage.py makemigrations

1. restart everything (server, db, etc.)
docker-compose down;docker-compose up --build

1. restart the server:
docker-compose restart web

1. hit server with browser
localhost:8000/

1. seed the database
docker-compose exec web python manage.py seed_categories_and_products