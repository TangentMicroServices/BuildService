# Build Service

A service for recording and displaying Build stats

## Getting started

**Run the service**

```
docker-compose up && docker-compose logs
```

**Test**

```
docker-compose run --rm web python manage.py test
```

**Continuously run tests**

```
docker-compose run --rm web sniffer
```