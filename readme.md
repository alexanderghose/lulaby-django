## prereqs: 
1. make sure docker is running
2. make sure you have an internet connection

## useful commands:

1. run the backend: 
docker-compose up --build

2. restart everything (server, db, etc.)
docker-compose down;docker-compose up --build

3. restart the server:
docker-compose restart web

4. hit server with browser
localhost:8000/