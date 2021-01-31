# py-facial-recognition

_Web-server for people verification by face recognition._

Min hardware requirements for *face_recognition* compilation: **2Gb** 
RAM

### URLs:

`/` for POST requests

`/upload` web-form for manual image upload

`/admin` regular Django admin interface

---

### For develop (server is availabled on port 8000)

```
docker-compose up -d --build
docker-compose -f docker-compose.yml exec web python manage.py createsuperuser
```
### Check with curl

```
curl -i -X POST -F "imgfile=@person-photo.jpg" http://localhost:8000/
```
---

### For production (server is availabled on port 1337)

```
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

add your server IP address or domain name to variable _DJANGO_ALLOWED_HOSTS_ at _.env.prod_

---
### Usefull docker commands

__Check logs__
```
docker-compose logs -f
```

__List all working conteiners__
```
docker ps
```

__List ALL conteiners__
```
docker ps -a
```

__Stop container__
```
docker-compose down
```
for nginx
```
docker-compose down --remove-orphans
```
or
```
docker stop CONTAINER ID 
```

__Delete containers with volums__
```
docker-compose down -v
```

__Start container after STOP__
```
docker start CONTAINER ID
```

__Restart container__
```
docker restart CONTAINER ID
```

__List of all images__
```
docker images
```

__Delete image__
```
docker rmi CONTAINER ID
```
or
```
docker rmi -f CONTAINER ID
```

__Exec comand within working container__
```
docker exec -it CONTAINER ID bash
```

__Prune docker system and remove all containers, images, volumes with one command__
```
docker system prune -a
```
---
### Specification

Back-end: __Django__

Application server: __gunicorn__

Front-end server: __nginx__

DB: __PostgreSQL__

Recognition engine: __face_recognition__