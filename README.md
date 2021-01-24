# py-facial-recognition

_Web-server for people verification by face recognition._

---

### For develop (server is availabled on port 8000)

```
docker-compose up -d --build
```

### For production (server is availabled on port 1337)

```
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

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
docker-compose down -v
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

DB: __PostgreSQL__, Redis (caсhing, _not implemented yet_)

Recognition engine: __face_recognition__