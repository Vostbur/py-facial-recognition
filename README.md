# py-facial-recognition

Web-server for people verification by face recognition.

## Usage

Build Docker image `docker-compose build` then run container `docker-compose up -d`

or single command `docker-compose up -d --build`

Check `docker-compose logs -f` if errors

Stop container `docker-compose down`

For add admin user:

```
docker ps -a
docker exec -it CONTAINER ID bash
python manage.py createsuperuser
```

## Specification

Back-end: Django

DB: PostgreSQL

Recognition engine: face_recognition