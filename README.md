# DRF-seed
A seed project for create a Django Rest Framework-based API


# Getting started

## On a mac/linuxy system:

Download and run the startup script

```bash
wget https://raw.githubusercontent.com/TangentSolutions/DRF-seed/master/start.sh
sh ./start.sh {project_name}
# answer the prompts .. 
```

Where `{project_name}` is something like `UserService`, `TodoService` .. etc

> .. This might take quite a while to run the first time .. so perhaps go grab yourself a coffee while you wait for this to finish.

Once this has run: 

```bash
cd {project_name}
docker-compose up
```

Check out your website on `docker-machine ip default`:8000. 

**You might want to create a superuser:**

```
docker-compose run --rm web python manage.py createsuperuser
```


You might also be interested in: 

**Run python manage.py commands as per normal, you just prefix them with**

```
docker-compose run --rm web python manage.py ...
```

**Other things you can do:**

**Run the tests automatically**

```
docker-compose run --rm web sniffer
```

## Some quick notes on docker: 

* Every time you `run docker-compose run ...` docker spins up a new container in the background to run your command. By specifying the `--rm` switch we clean up this container once the command has finished running. 
* The Kitematic UI is a nice easy way to see which containers are running set. 
* Once you've finished your `docker-compose` session, I'd recommend you run: `docker-compose rm -f` (this deletes the containers your app has been running in. Don't worry, you can create them again easily with: `docker-compose up`. Containers are cheap. 

**Understanding docker-compose `run`**

```
docker-compose run --rm web python manage.py shell
```

we can break that down as: 

```
docker-compose run --rm {service_name} {command}
```



